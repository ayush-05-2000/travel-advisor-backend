from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Destination(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    description = Column(String)
    best_season = Column(String)
    average_cost = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    created_at = Column(DateTime, default=func.now())

    # Relationship to places
    places = relationship("Place", back_populates="destination")


class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    destination_id = Column(Integer, ForeignKey("destinations.id"))
    created_at = Column(DateTime, default=func.now())
    destination = relationship("Destination", back_populates="places")
