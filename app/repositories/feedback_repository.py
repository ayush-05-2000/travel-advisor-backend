from sqlalchemy.orm import Session
from app.models.feedback import Feedback
from app.dtos.feedback_dto import FeedbackCreateDTO, FeedbackUpdateDTO

class FeedbackRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_feedback(self, feedback_data: FeedbackCreateDTO) -> Feedback:
        """Create new feedback entry."""
        feedback = Feedback(**feedback_data.model_dump())
        self.db.add(feedback)
        self.db.commit()
        self.db.refresh(feedback)
        return feedback

    def get_feedback_by_id(self, feedback_id: int) -> Feedback:
        """Retrieve feedback by ID."""
        return self.db.query(Feedback).filter(Feedback.id == feedback_id).first()

    def get_feedback_by_itinerary(self, itinerary_id: int):
        """Retrieve all feedback for a specific itinerary."""
        return self.db.query(Feedback).filter(Feedback.itinerary_id == itinerary_id).all()

    def get_all_feedback(self):
        """Retrieve all feedback records."""
        return self.db.query(Feedback).all()

    def update_feedback(self, feedback_id: int, feedback_data: FeedbackUpdateDTO) -> Feedback:
        """Update feedback details."""
        feedback = self.get_feedback_by_id(feedback_id)
        if feedback:
            update_data = feedback_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(feedback, key, value)
            self.db.commit()
            self.db.refresh(feedback)
        return feedback

    def delete_feedback(self, feedback_id: int):
        """Delete feedback by ID."""
        feedback = self.get_feedback_by_id(feedback_id)
        if feedback:
            self.db.delete(feedback)
            self.db.commit()
        return feedback
