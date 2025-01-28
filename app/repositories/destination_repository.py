from sqlalchemy.orm import Session
from app.models.destination import Destination, Place
from app.dtos.destination_dto import DestinationCreateDTO, DestinationUpdateDTO
from app.dtos.place_dto import PlaceCreateDTO

class DestinationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_destination(self, destination_data: DestinationCreateDTO) -> Destination:
        """Creates a new destination record along with associated places."""
        new_destination = Destination(
            name=destination_data.name,
            country=destination_data.country,
            description=destination_data.description,
            best_season=destination_data.best_season,
            average_cost=destination_data.average_cost,
            latitude=destination_data.latitude,
            longitude=destination_data.longitude,
        )
        # Add associated places if provided
        if destination_data.places:
            for place_data in destination_data.places:
                new_place = Place(**place_data.model_dump())
                new_destination.places.append(new_place)
        
        self.db.add(new_destination)
        self.db.commit()
        self.db.refresh(new_destination)
        return new_destination

    def get_destination_by_id(self, destination_id: int) -> Destination:
        """Fetch a destination by ID, including associated places."""
        return self.db.query(Destination).filter(Destination.id == destination_id).first()

    def get_all_destinations(self):
        """Retrieve all destination records with associated places."""
        return self.db.query(Destination).all()

    def update_destination(self, destination_id: int, destination_data: DestinationUpdateDTO) -> Destination:
        """Updates an existing destination record along with associated places."""
        db_destination = self.get_destination_by_id(destination_id)
        if db_destination:
            # Update destination fields
            update_data = destination_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                if key != "places":  # Handle places separately
                    setattr(db_destination, key, value)
            
            # Handle updating places
            if destination_data.places:
                db_destination.places.clear()  # Clear existing places
                for place_data in destination_data.places:
                    new_place = Place(**place_data.model_dump())
                    db_destination.places.append(new_place)

            self.db.commit()
            self.db.refresh(db_destination)
        return db_destination

    def delete_destination(self, destination_id: int) -> bool:
        """Deletes a destination by ID."""
        db_destination = self.get_destination_by_id(destination_id)
        if db_destination:
            self.db.delete(db_destination)
            self.db.commit()
            return True
        return False
