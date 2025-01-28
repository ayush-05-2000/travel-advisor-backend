from sqlalchemy.orm import Session
from app.repositories.collaborator_repository import CollaboratorRepository
from app.dtos.collaborator_dto import CollaboratorCreateDTO, CollaboratorUpdateDTO, CollaboratorResponseDTO
from typing import List, Optional

class CollaboratorService:
    def __init__(self, db: Session):
        self.collaborator_repo = CollaboratorRepository(db)

    def create_collaborator(self, collaborator_data: CollaboratorCreateDTO) -> CollaboratorResponseDTO:
        """Business logic to create a new collaborator and return a response DTO."""
        collaborator = self.collaborator_repo.create_collaborator(collaborator_data)
        return CollaboratorResponseDTO.from_orm(collaborator)

    def get_collaborator_by_id(self, collaborator_id: int) -> Optional[CollaboratorResponseDTO]:
        """Fetch collaborator by ID and return response DTO."""
        collaborator = self.collaborator_repo.get_collaborator_by_id(collaborator_id)
        if collaborator:
            return CollaboratorResponseDTO.from_orm(collaborator)
        return None

    def get_all_collaborators(self) -> List[CollaboratorResponseDTO]:
        """Retrieve all collaborators and return response DTOs."""
        collaborators = self.collaborator_repo.get_all_collaborators()
        return [CollaboratorResponseDTO.from_orm(collaborator) for collaborator in collaborators]

    def get_collaborators_by_itinerary(self, itinerary_id: int) -> List[CollaboratorResponseDTO]:
        """Retrieve all collaborators for a specific itinerary."""
        collaborators = self.collaborator_repo.get_collaborators_by_itinerary(itinerary_id)
        return [CollaboratorResponseDTO.from_orm(collaborator) for collaborator in collaborators]

    def update_collaborator(self, collaborator_id: int, collaborator_data: CollaboratorUpdateDTO) -> Optional[CollaboratorResponseDTO]:
        """Update a collaborator and return the updated response DTO."""
        updated_collaborator = self.collaborator_repo.update_collaborator(collaborator_id, collaborator_data)
        if updated_collaborator:
            return CollaboratorResponseDTO.from_orm(updated_collaborator)
        return None

    def delete_collaborator(self, collaborator_id: int) -> bool:
        """Delete a collaborator and return success status."""
        return self.collaborator_repo.delete_collaborator(collaborator_id)
