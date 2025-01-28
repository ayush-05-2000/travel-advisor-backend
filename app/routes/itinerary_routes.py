from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.itinerary_service import ItineraryService
from app.dtos.itinerary_dto import ItineraryCreateDTO, ItineraryUpdateDTO, ItineraryResponseDTO
from typing import List,Optional
from app.services.openai_service import generate_itinerary 

# Create router instance
router = APIRouter(
    prefix="/itineraries",
    tags=["Itineraries"]
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# AI-Generated Itinerary Route
@router.post("/generate-ai-itinerary/")
def get_ai_itinerary(
    budget: int,
    num_people: int,
    places: Optional[List[str]] = None
):
    """
    Generate an AI-based itinerary using OpenAI API.
    """
    try:
        itinerary = generate_itinerary(budget, num_people, places)
        return {"itinerary": itinerary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Create a new itinerary
@router.post("/", response_model=ItineraryResponseDTO)
def create_itinerary(itinerary_data: ItineraryCreateDTO, db: Session = Depends(get_db)):
    new_itinerary = ItineraryService.create_itinerary(db, itinerary_data)
    if not new_itinerary:
        raise HTTPException(status_code=400, detail="Failed to create itinerary")
    return new_itinerary

# Get an itinerary by ID
@router.get("/{itinerary_id}", response_model=ItineraryResponseDTO)
def get_itinerary(itinerary_id: int, db: Session = Depends(get_db)):
    itinerary = ItineraryService.get_itinerary_by_id(db, itinerary_id)
    if not itinerary:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    return itinerary

# Get all itineraries
@router.get("/", response_model=List[ItineraryResponseDTO])
def get_all_itineraries(db: Session = Depends(get_db)):
    return ItineraryService.get_all_itineraries(db)

# Update an itinerary by ID
@router.put("/{itinerary_id}", response_model=ItineraryResponseDTO)
def update_itinerary(itinerary_id: int, itinerary_data: ItineraryUpdateDTO, db: Session = Depends(get_db)):
    updated_itinerary = ItineraryService.update_itinerary(db, itinerary_id, itinerary_data)
    if not updated_itinerary:
        raise HTTPException(status_code=404, detail="Itinerary not found or update failed")
    return updated_itinerary

# Delete an itinerary by ID
@router.delete("/{itinerary_id}")
def delete_itinerary(itinerary_id: int, db: Session = Depends(get_db)):
    success = ItineraryService.delete_itinerary(db, itinerary_id)
    if not success:
        raise HTTPException(status_code=404, detail="Itinerary not found or deletion failed")
    return {"message": "Itinerary deleted successfully"}
  
