from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    itinerary_id = Column(Integer, ForeignKey("itineraries.id", ondelete="CASCADE"))
    rating = Column(Integer, nullable=False)  # 1-5 rating
    comments = Column(String)
    created_at = Column(DateTime, default=func.now())
