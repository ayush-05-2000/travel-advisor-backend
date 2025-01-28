from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.services.place_service import PlaceService
from app.dtos.place_dto import PlaceCreateDTO, PlaceUpdateDTO, PlaceResponseDTO

router = APIRouter(
    prefix="/places",
    tags=["Places"]
)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new place
@router.post("/", response_model=PlaceResponseDTO)
def create_place(place_data: PlaceCreateDTO, db: Session = Depends(get_db)):
    """Create a new place."""
    place_service = PlaceService(db)
    new_place = place_service.create_place(place_data)
    return new_place

# Get a place by ID
@router.get("/{place_id}", response_model=PlaceResponseDTO)
def get_place(place_id: int, db: Session = Depends(get_db)):
    """Retrieve a place by ID."""
    place_service = PlaceService(db)
    place = place_service.get_place_by_id(place_id)
    if place is None:
        raise HTTPException(status_code=404, detail="Place not found")
    return place

# Get all places
@router.get("/", response_model=List[PlaceResponseDTO])
def get_all_places(db: Session = Depends(get_db)):
    """Retrieve all places."""
    place_service = PlaceService(db)
    return place_service.get_all_places()

# Update a place
@router.put("/{place_id}", response_model=PlaceResponseDTO)
def update_place(place_id: int, place_data: PlaceUpdateDTO, db: Session = Depends(get_db)):
    """Update a place record."""
    place_service = PlaceService(db)
    updated_place = place_service.update_place(place_id, place_data)
    if updated_place is None:
        raise HTTPException(status_code=404, detail="Place not found")
    return updated_place

# Delete a place
@router.delete("/{place_id}")
def delete_place(place_id: int, db: Session = Depends(get_db)):
    """Delete a place."""
    place_service = PlaceService(db)
    if not place_service.delete_place(place_id):
        raise HTTPException(status_code=404, detail="Place not found")
    return {"message": "Place deleted successfully"}
