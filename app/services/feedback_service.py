from sqlalchemy.orm import Session
from app.repositories.feedback_repository import FeedbackRepository
from app.dtos.feedback_dto import FeedbackCreateDTO, FeedbackUpdateDTO, FeedbackResponseDTO
from app.models.feedback import Feedback
from typing import List, Optional

class FeedbackService:
    def __init__(self, db: Session):
        self.feedback_repo = FeedbackRepository(db)

    def create_feedback(self, feedback_data: FeedbackCreateDTO) -> FeedbackResponseDTO:
        """Business logic for creating a feedback entry."""
        feedback = self.feedback_repo.create_feedback(feedback_data)
        return FeedbackResponseDTO.from_orm(feedback)

    def get_feedback_by_id(self, feedback_id: int) -> Optional[FeedbackResponseDTO]:
        """Retrieve feedback details by ID."""
        feedback = self.feedback_repo.get_feedback_by_id(feedback_id)
        if feedback:
            return FeedbackResponseDTO.from_orm(feedback)
        return None

    def get_feedback_by_itinerary(self, itinerary_id: int) -> List[FeedbackResponseDTO]:
        """Retrieve all feedback for a specific itinerary."""
        feedback_list = self.feedback_repo.get_feedback_by_itinerary(itinerary_id)
        return [FeedbackResponseDTO.from_orm(feedback) for feedback in feedback_list]

    def get_all_feedback(self) -> List[FeedbackResponseDTO]:
        """Retrieve all feedback records."""
        feedback_list = self.feedback_repo.get_all_feedback()
        return [FeedbackResponseDTO.from_orm(feedback) for feedback in feedback_list]

    def update_feedback(self, feedback_id: int, feedback_data: FeedbackUpdateDTO) -> Optional[FeedbackResponseDTO]:
        """Business logic for updating feedback details."""
        feedback = self.feedback_repo.update_feedback(feedback_id, feedback_data)
        if feedback:
            return FeedbackResponseDTO.from_orm(feedback)
        return None

    def delete_feedback(self, feedback_id: int) -> bool:
        """Delete feedback entry and return status."""
        feedback = self.feedback_repo.delete_feedback(feedback_id)
        return feedback is not None
