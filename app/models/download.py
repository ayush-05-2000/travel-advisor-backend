from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Download(Base):
    __tablename__ = "downloads"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    itinerary_id = Column(Integer, ForeignKey("itineraries.id", ondelete="CASCADE"))
    pdf_link = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
