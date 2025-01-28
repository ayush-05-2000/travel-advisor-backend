from pydantic import BaseModel, conint, confloat
from datetime import datetime
from typing import List, Optional
from app.dtos.place_dto import PlaceCreateDTO, PlaceUpdateDTO, PlaceResponseDTO


class DestinationCreateDTO(BaseModel):
    name: str
    country: str
    description: Optional[str] = None
    best_season: Optional[str] = None
    average_cost: Optional[int] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    places: Optional[List["PlaceCreateDTO"]] = None  # Nested PlaceCreateDTO

    class Config:
        arbitrary_types_allowed = True

# DTO for updating a destination (incoming request)
class DestinationUpdateDTO(BaseModel):
    name: Optional[str] = None
    country: Optional[str] = None
    description: Optional[str] = None
    best_season: Optional[str] = None
    average_cost: Optional[int] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    places: Optional[List["PlaceUpdateDTO"]] = None  # Nested PlaceUpdateDTO

    class Config:
        arbitrary_types_allowed = True


# DTO for sending destination data as a response
class DestinationResponseDTO(BaseModel):
    id: int
    name: str
    country: str
    description: Optional[str] = None
    best_season: Optional[str] = None
    average_cost: Optional[int] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    created_at: datetime
    places: List["PlaceResponseDTO"]  # Nested PlaceResponseDTO for associated places

    class Config:
        from_attributes = True  # Ensures compatibility with ORM models