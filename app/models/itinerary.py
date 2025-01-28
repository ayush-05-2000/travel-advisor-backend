from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Itinerary(Base):
    __tablename__ = "itineraries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    destination = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    budget = Column(Integer, nullable=False)
    preferences = Column(String)  # JSON string (adventure, culture, etc.)
    status = Column(String, default="pending")  # pending, confirmed, completed
    created_at = Column(DateTime, default=func.now())
  
