from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# DTO for creating a user (incoming request)
class UserCreateDTO(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    preferences: Optional[str] = None  # Preferences are optional

# DTO for updating a user (incoming request)
class UserUpdateDTO(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    preferences: Optional[str] = None

# DTO for sending user data as a response
class UserResponseDTO(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    preferences: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True  # Ensures compatibility with SQLAlchemy ORM
