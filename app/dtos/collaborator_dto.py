from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# DTO for creating a collaborator (incoming request)
class CollaboratorCreateDTO(BaseModel):
    itinerary_id: int
    email: EmailStr  # Ensures valid email format
    role: Optional[str] = "viewer"  # Default role is "viewer" (options: viewer, editor)

# DTO for updating a collaborator (incoming request)
class CollaboratorUpdateDTO(BaseModel):
    role: Optional[str] = None  # Allows updating role only (optional)

# DTO for sending collaborator data as a response
class CollaboratorResponseDTO(BaseModel):
    id: int
    itinerary_id: int
    email: EmailStr
    role: str
    created_at: datetime

    class Config:
        from_attributes = True  # Ensures compatibility with ORM models
