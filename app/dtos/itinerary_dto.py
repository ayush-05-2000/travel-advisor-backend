from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# DTO for creating an itinerary (incoming request)
class ItineraryCreateDTO(BaseModel):
    user_id: int
    destination: str
    start_date: datetime
    end_date: datetime
    budget: int
    preferences: Optional[str] = None  # JSON string (adventure, culture, etc.)
    status: Optional[str] = "pending"  # Default status if not provided

# DTO for updating an itinerary (incoming request)
class ItineraryUpdateDTO(BaseModel):
    destination: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    budget: Optional[int] = None
    preferences: Optional[str] = None
    status: Optional[str] = None

# DTO for sending itinerary data as a response
class ItineraryResponseDTO(BaseModel):
    id: int
    user_id: int
    destination: str
    start_date: datetime
    end_date: datetime
    budget: int
    preferences: Optional[str] = None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True  # Enables automatic conversion from ORM models
