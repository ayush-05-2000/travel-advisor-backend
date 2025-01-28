from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    itinerary_id = Column(Integer, ForeignKey("itineraries.id", ondelete="CASCADE"))
    category = Column(String, nullable=False)  # transport, food, accommodation
    amount = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=func.now())
