from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional

# DTO for creating a download entry (incoming request)
class DownloadCreateDTO(BaseModel):
    user_id: int
    itinerary_id: int
    pdf_link: HttpUrl  # Ensures a valid URL is provided

# DTO for updating a download entry (incoming request)
class DownloadUpdateDTO(BaseModel):
    pdf_link: Optional[HttpUrl] = None  # Allows updating the PDF link

# DTO for sending download data as a response
class DownloadResponseDTO(BaseModel):
    id: int
    user_id: int
    itinerary_id: int
    pdf_link: HttpUrl
    created_at: datetime

    class Config:
        from_attributes = True  # Ensures compatibility with ORM models
