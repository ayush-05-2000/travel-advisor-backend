from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.services.destination_service import DestinationService
from app.dtos.destination_dto import DestinationCreateDTO, DestinationUpdateDTO, DestinationResponseDTO

router = APIRouter(
    prefix="/destinations",
    tags=["Destinations"]
)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new destination
@router.post("/", response_model=DestinationResponseDTO)
def create_destination(destination_data: DestinationCreateDTO, db: Session = Depends(get_db)):
    """Create a new destination entry with places."""
    destination_service = DestinationService(db)
    new_destination = destination_service.create_destination(destination_data)
    return new_destination

# Get a destination by ID
@router.get("/{destination_id}", response_model=DestinationResponseDTO)
def get_destination(destination_id: int, db: Session = Depends(get_db)):
    """Retrieve a destination by ID with places."""
    destination_service = DestinationService(db)
    destination = destination_service.get_destination_by_id(destination_id)
    if destination is None:
        raise HTTPException(status_code=404, detail="Destination not found")
    return destination

# Get all destinations
@router.get("/", response_model=List[DestinationResponseDTO])
def get_all_destinations(db: Session = Depends(get_db)):
    """Retrieve all destination records with places."""
    destination_service = DestinationService(db)
    return destination_service.get_all_destinations()

# Update a destination by ID
@router.put("/{destination_id}", response_model=DestinationResponseDTO)
def update_destination(destination_id: int, destination_data: DestinationUpdateDTO, db: Session = Depends(get_db)):
    """Update a destination by ID."""
    destination_service = DestinationService(db)
    updated_destination = destination_service.update_destination(destination_id, destination_data)
    if updated_destination is None:
        raise HTTPException(status_code=404, detail="Destination not found")
    return updated_destination

# Delete a destination by ID
@router.delete("/{destination_id}")
def delete_destination(destination_id: int, db: Session = Depends(get_db)):
    """Delete a destination by ID."""
    destination_service = DestinationService(db)
    if not destination_service.delete_destination(destination_id):
        raise HTTPException(status_code=404, detail="Destination not found")
    return {"message": "Destination deleted successfully"}
