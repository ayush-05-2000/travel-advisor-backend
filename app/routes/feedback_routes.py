from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.services.feedback_service import FeedbackService
from app.dtos.feedback_dto import FeedbackCreateDTO, FeedbackUpdateDTO, FeedbackResponseDTO

router = APIRouter(prefix="/feedbacks", tags=["Feedback"])

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=FeedbackResponseDTO)
def create_feedback(feedback_data: FeedbackCreateDTO, db: Session = Depends(get_db)):
    """Create new feedback."""
    feedback_service = FeedbackService(db)
    return feedback_service.create_feedback(feedback_data)

@router.get("/{feedback_id}", response_model=FeedbackResponseDTO)
def get_feedback(feedback_id: int, db: Session = Depends(get_db)):
    """Get feedback by ID."""
    feedback_service = FeedbackService(db)
    feedback = feedback_service.get_feedback_by_id(feedback_id)
    if feedback is None:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return feedback

@router.get("/", response_model=List[FeedbackResponseDTO])
def get_all_feedbacks(db: Session = Depends(get_db)):
    """Retrieve all feedback records."""
    feedback_service = FeedbackService(db)
    return feedback_service.get_all_feedback()

@router.get("/itinerary/{itinerary_id}", response_model=List[FeedbackResponseDTO])
def get_feedback_by_itinerary(itinerary_id: int, db: Session = Depends(get_db)):
    """Retrieve feedback for a specific itinerary."""
    feedback_service = FeedbackService(db)
    return feedback_service.get_feedback_by_itinerary(itinerary_id)

@router.put("/{feedback_id}", response_model=FeedbackResponseDTO)
def update_feedback(feedback_id: int, feedback_data: FeedbackUpdateDTO, db: Session = Depends(get_db)):
    """Update existing feedback."""
    feedback_service = FeedbackService(db)
    updated_feedback = feedback_service.update_feedback(feedback_id, feedback_data)
    if updated_feedback is None:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return updated_feedback

@router.delete("/{feedback_id}")
def delete_feedback(feedback_id: int, db: Session = Depends(get_db)):
    """Delete feedback by ID."""
    feedback_service = FeedbackService(db)
    if not feedback_service.delete_feedback(feedback_id):
        raise HTTPException(status_code=404, detail="Feedback not found")
    return {"message": "Feedback deleted successfully"}
