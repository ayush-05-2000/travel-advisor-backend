from pydantic import BaseModel, conint
from datetime import datetime
from typing import Optional

# DTO for creating an expense (incoming request)
class ExpenseCreateDTO(BaseModel):
    itinerary_id: int
    category: str  # Categories: transport, food, accommodation
    amount: int  # Using simple int, we can validate separately using validators

# DTO for updating an expense (incoming request)
class ExpenseUpdateDTO(BaseModel):
    category: Optional[str] = None
    amount: Optional[int] = None  # Use simple int instead of conint inside Optional

# DTO for sending expense data as a response
class ExpenseResponseDTO(BaseModel):
    id: int
    itinerary_id: int
    category: str
    amount: int
    created_at: datetime

    class Config:
        from_attributes = True  # Ensures compatibility with ORM models

# Validation using Pydantic field validator
from pydantic import field_validator

class ExpenseCreateDTOValidated(ExpenseCreateDTO):
    @field_validator("amount")
    def validate_amount(cls, value):
        if value < 0:
            raise ValueError("Amount must be a non-negative value.")
        return value
