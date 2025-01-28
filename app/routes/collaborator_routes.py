from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.services.collaborator_service import CollaboratorService
from app.dtos.collaborator_dto import CollaboratorCreateDTO, CollaboratorUpdateDTO, CollaboratorResponseDTO

router = APIRouter(
    prefix="/collaborators",
    tags=["Collaborators"]
)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new collaborator
@router.post("/", response_model=CollaboratorResponseDTO)
def create_collaborator(collaborator_data: CollaboratorCreateDTO, db: Session = Depends(get_db)):
    """Create a new collaborator entry."""
    collaborator_service = CollaboratorService(db)
    new_collaborator = collaborator_service.create_collaborator(collaborator_data)
    return new_collaborator

# Get a collaborator by ID
@router.get("/{collaborator_id}", response_model=CollaboratorResponseDTO)
def get_collaborator(collaborator_id: int, db: Session = Depends(get_db)):
    """Retrieve a collaborator by ID."""
    collaborator_service = CollaboratorService(db)
    collaborator = collaborator_service.get_collaborator_by_id(collaborator_id)
    if collaborator is None:
        raise HTTPException(status_code=404, detail="Collaborator not found")
    return collaborator

# Get all collaborators
@router.get("/", response_model=List[CollaboratorResponseDTO])
def get_all_collaborators(db: Session = Depends(get_db)):
    """Retrieve all collaborator records."""
    collaborator_service = CollaboratorService(db)
    return collaborator_service.get_all_collaborators()

# Get collaborators by itinerary ID
@router.get("/itinerary/{itinerary_id}", response_model=List[CollaboratorResponseDTO])
def get_collaborators_by_itinerary(itinerary_id: int, db: Session = Depends(get_db)):
    """Retrieve all collaborators for a specific itinerary."""
    collaborator_service = CollaboratorService(db)
    return collaborator_service.get_collaborators_by_itinerary(itinerary_id)

# Update a collaborator by ID
@router.put("/{collaborator_id}", response_model=CollaboratorResponseDTO)
def update_collaborator(collaborator_id: int, collaborator_data: CollaboratorUpdateDTO, db: Session = Depends(get_db)):
    """Update a collaborator by ID."""
    collaborator_service = CollaboratorService(db)
    updated_collaborator = collaborator_service.update_collaborator(collaborator_id, collaborator_data)
    if updated_collaborator is None:
        raise HTTPException(status_code=404, detail="Collaborator not found")
    return updated_collaborator

# Delete a collaborator by ID
@router.delete("/{collaborator_id}")
def delete_collaborator(collaborator_id: int, db: Session = Depends(get_db)):
    """Delete a collaborator by ID."""
    collaborator_service = CollaboratorService(db)
    if not collaborator_service.delete_collaborator(collaborator_id):
        raise HTTPException(status_code=404, detail="Collaborator not found")
    return {"message": "Collaborator deleted successfully"}
