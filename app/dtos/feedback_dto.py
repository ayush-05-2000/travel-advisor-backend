from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional

# DTO for creating feedback (incoming request)
class FeedbackCreateDTO(BaseModel):
    user_id: int
    itinerary_id: int
    rating: Optional[int] = None  # Declare as Optional, constraints applied via validator
    comments: Optional[str] = None

    @field_validator("rating")
    def validate_rating(cls, v):
        if v is not None and (v < 1 or v > 5):
            raise ValueError("Rating must be between 1 and 5")
        return v

# DTO for updating feedback (incoming request)
class FeedbackUpdateDTO(BaseModel):
    rating: Optional[int] = None
    comments: Optional[str] = None

    @field_validator("rating")
    def validate_rating(cls, v):
        if v is not None and (v < 1 or v > 5):
            raise ValueError("Rating must be between 1 and 5")
        return v

# DTO for sending feedback data as a response
class FeedbackResponseDTO(BaseModel):
    id: int
    user_id: int
    itinerary_id: int
    rating: int
    comments: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True  # Ensures compatibility with ORM models
