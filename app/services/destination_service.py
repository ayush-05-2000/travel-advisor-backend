from sqlalchemy.orm import Session
from app.repositories.destination_repository import DestinationRepository
from app.dtos.destination_dto import DestinationCreateDTO, DestinationUpdateDTO, DestinationResponseDTO
from app.dtos.place_dto import PlaceResponseDTO
from typing import List, Optional

class DestinationService:
    def __init__(self, db: Session):
        self.destination_repo = DestinationRepository(db)

    def create_destination(self, destination_data: DestinationCreateDTO) -> DestinationResponseDTO:
        """Business logic to create a new destination with places."""
        destination = self.destination_repo.create_destination(destination_data)
        return DestinationResponseDTO(
            **destination.__dict__,
            places=[PlaceResponseDTO.from_orm(place) for place in destination.places]
        )

    def get_destination_by_id(self, destination_id: int) -> Optional[DestinationResponseDTO]:
        """Fetch destination by ID and return response DTO with places."""
        destination = self.destination_repo.get_destination_by_id(destination_id)
        if destination:
            return DestinationResponseDTO(
                **destination.__dict__,
                places=[PlaceResponseDTO.from_orm(place) for place in destination.places]
            )
        return None

    def get_all_destinations(self) -> List[DestinationResponseDTO]:
        """Retrieve all destinations and return response DTOs with places."""
        destinations = self.destination_repo.get_all_destinations()
        return [
            DestinationResponseDTO(
                **destination.__dict__,
                places=[PlaceResponseDTO.from_orm(place) for place in destination.places]
            ) for destination in destinations
        ]

    def update_destination(self, destination_id: int, destination_data: DestinationUpdateDTO) -> Optional[DestinationResponseDTO]:
        """Update a destination and return the updated response DTO."""
        updated_destination = self.destination_repo.update_destination(destination_id, destination_data)
        if updated_destination:
            return DestinationResponseDTO(
                **updated_destination.__dict__,
                places=[PlaceResponseDTO.from_orm(place) for place in updated_destination.places]
            )
        return None

    def delete_destination(self, destination_id: int) -> bool:
        """Delete a destination and return success status."""
        return self.destination_repo.delete_destination(destination_id)
