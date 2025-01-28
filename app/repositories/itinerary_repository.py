from sqlalchemy.orm import Session
from app.models.itinerary import Itinerary
from app.dtos.itinerary_dto import ItineraryCreateDTO, ItineraryUpdateDTO

class ItineraryRepository:
    
    @staticmethod
    def create_itinerary(db: Session, itinerary_data: ItineraryCreateDTO) -> Itinerary:
        """Create a new itinerary."""
        itinerary = Itinerary(**itinerary_data.model_dump())
        db.add(itinerary)
        db.commit()
        db.refresh(itinerary)
        return itinerary

    @staticmethod
    def get_itinerary_by_id(db: Session, itinerary_id: int) -> Itinerary:
        """Retrieve an itinerary by its ID."""
        return db.query(Itinerary).filter(Itinerary.id == itinerary_id).first()

    @staticmethod
    def get_all_itineraries(db: Session):
        """Retrieve all itineraries."""
        return db.query(Itinerary).all()

    @staticmethod
    def update_itinerary(db: Session, itinerary_id: int, itinerary_data: ItineraryUpdateDTO) -> Itinerary:
        """Update an existing itinerary."""
        itinerary = db.query(Itinerary).filter(Itinerary.id == itinerary_id).first()
        if itinerary:
            for key, value in itinerary_data.model_dump(exclude_unset=True).items():
                setattr(itinerary, key, value)
            db.commit()
            db.refresh(itinerary)
        return itinerary

    @staticmethod
    def delete_itinerary(db: Session, itinerary_id: int) -> bool:
        """Delete an itinerary by its ID."""
        itinerary = db.query(Itinerary).filter(Itinerary.id == itinerary_id).first()
        if itinerary:
            db.delete(itinerary)
            db.commit()
            return True
        return False
