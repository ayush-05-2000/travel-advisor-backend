from pydantic import BaseModel
from typing import Optional
from datetime import datetime
    

class PlaceCreateDTO(BaseModel):
    name: str                  # Name of the place (required)
    description: Optional[str] = None  # Description of the place (optional)
    destination_id: int        # ID of the associated destination (required)


class PlaceUpdateDTO(BaseModel):
    name: Optional[str] = None          # Name of the place
    description: Optional[str] = None   # Description of the place
    destination_id: Optional[int] = None  # ID of the associated destination

class PlaceResponseDTO(BaseModel):
    id: int                    # Unique identifier of the place
    name: str                  # Name of the place
    description: Optional[str] = None
    destination_id: int        # ID of the associated destination
    created_at: datetime        # Timestamp of creation

    class Config:
        from_attributes = True  # Ensures compatibility with ORM models
