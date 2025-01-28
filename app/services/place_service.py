from sqlalchemy.orm import Session
from app.repositories.place_repository import PlaceRepository
from app.dtos.place_dto import PlaceCreateDTO, PlaceUpdateDTO, PlaceResponseDTO
from typing import List, Optional

class PlaceService:
    def __init__(self, db: Session):
        self.place_repo = PlaceRepository(db)

    def create_place(self, place_data: PlaceCreateDTO) -> PlaceResponseDTO:
        """Business logic to create a new place."""
        place = self.place_repo.create_place(place_data)
        return PlaceResponseDTO.from_orm(place)

    def get_place_by_id(self, place_id: int) -> Optional[PlaceResponseDTO]:
        """Retrieve a place by its ID."""
        place = self.place_repo.get_place_by_id(place_id)
        if place:
            return PlaceResponseDTO.from_orm(place)
        return None

    def get_all_places(self) -> List[PlaceResponseDTO]:
        """Retrieve all places."""
        places = self.place_repo.get_all_places()
        return [PlaceResponseDTO.from_orm(place) for place in places]

    def update_place(self, place_id: int, place_data: PlaceUpdateDTO) -> Optional[PlaceResponseDTO]:
        """Update a place record."""
        updated_place = self.place_repo.update_place(place_id, place_data)
        if updated_place:
            return PlaceResponseDTO.from_orm(updated_place)
        return None

    def delete_place(self, place_id: int) -> bool:
        """Delete a place."""
        return self.place_repo.delete_place(place_id)
