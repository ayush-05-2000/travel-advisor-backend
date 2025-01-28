from sqlalchemy.orm import Session
from app.models.destination import Place
from app.dtos.place_dto import PlaceCreateDTO, PlaceUpdateDTO
from typing import List, Optional

class PlaceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_place(self, place_data: PlaceCreateDTO) -> Place:
        """Create a new place record."""
        new_place = Place(**place_data.model_dump())
        self.db.add(new_place)
        self.db.commit()
        self.db.refresh(new_place)
        return new_place

    def get_place_by_id(self, place_id: int) -> Optional[Place]:
        """Retrieve a place by its ID."""
        return self.db.query(Place).filter(Place.id == place_id).first()

    def get_all_places(self) -> List[Place]:
        """Retrieve all place records."""
        return self.db.query(Place).all()

    def update_place(self, place_id: int, place_data: PlaceUpdateDTO) -> Optional[Place]:
        """Update an existing place record."""
        db_place = self.get_place_by_id(place_id)
        if db_place:
            update_data = place_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_place, key, value)
            self.db.commit()
            self.db.refresh(db_place)
        return db_place

    def delete_place(self, place_id: int) -> bool:
        """Delete a place by its ID."""
        db_place = self.get_place_by_id(place_id)
        if db_place:
            self.db.delete(db_place)
            self.db.commit()
            return True
        return False
