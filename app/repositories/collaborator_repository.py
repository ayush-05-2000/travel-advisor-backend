from sqlalchemy.orm import Session
from app.models.collaborator import Collaborator
from app.dtos.collaborator_dto import CollaboratorCreateDTO, CollaboratorUpdateDTO

class CollaboratorRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_collaborator(self, collaborator_data: CollaboratorCreateDTO) -> Collaborator:
        """Creates a new collaborator record."""
        new_collaborator = Collaborator(**collaborator_data.model_dump())
        self.db.add(new_collaborator)
        self.db.commit()
        self.db.refresh(new_collaborator)
        return new_collaborator

    def get_collaborator_by_id(self, collaborator_id: int) -> Collaborator:
        """Fetch a collaborator by ID."""
        return self.db.query(Collaborator).filter(Collaborator.id == collaborator_id).first()

    def get_all_collaborators(self):
        """Retrieve all collaborator records."""
        return self.db.query(Collaborator).all()

    def get_collaborators_by_itinerary(self, itinerary_id: int):
        """Retrieve all collaborators associated with a specific itinerary."""
        return self.db.query(Collaborator).filter(Collaborator.itinerary_id == itinerary_id).all()

    def update_collaborator(self, collaborator_id: int, collaborator_data: CollaboratorUpdateDTO) -> Collaborator:
        """Updates an existing collaborator record."""
        db_collaborator = self.get_collaborator_by_id(collaborator_id)
        if db_collaborator:
            update_data = collaborator_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_collaborator, key, value)
            self.db.commit()
            self.db.refresh(db_collaborator)
        return db_collaborator

    def delete_collaborator(self, collaborator_id: int) -> bool:
        """Deletes a collaborator by ID."""
        db_collaborator = self.get_collaborator_by_id(collaborator_id)
        if db_collaborator:
            self.db.delete(db_collaborator)
            self.db.commit()
            return True
        return False
