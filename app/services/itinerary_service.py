from sqlalchemy.orm import Session
from app.repositories.itinerary_repository import ItineraryRepository
from app.dtos.itinerary_dto import ItineraryCreateDTO, ItineraryUpdateDTO, ItineraryResponseDTO

class ItineraryService:

    @staticmethod
    def create_itinerary(db: Session, itinerary_data: ItineraryCreateDTO) -> ItineraryResponseDTO:
        """Create a new itinerary and return the response DTO."""
        itinerary = ItineraryRepository.create_itinerary(db, itinerary_data)
        return ItineraryResponseDTO.from_orm(itinerary)

    @staticmethod
    def get_itinerary_by_id(db: Session, itinerary_id: int) -> ItineraryResponseDTO:
        """Retrieve an itinerary by its ID."""
        itinerary = ItineraryRepository.get_itinerary_by_id(db, itinerary_id)
        if not itinerary:
            return None
        return ItineraryResponseDTO.from_orm(itinerary)

    @staticmethod
    def get_all_itineraries(db: Session) -> list[ItineraryResponseDTO]:
        """Retrieve all itineraries."""
        itineraries = ItineraryRepository.get_all_itineraries(db)
        return [ItineraryResponseDTO.from_orm(itinerary) for itinerary in itineraries]

    @staticmethod
    def update_itinerary(db: Session, itinerary_id: int, itinerary_data: ItineraryUpdateDTO) -> ItineraryResponseDTO:
        """Update an existing itinerary and return the updated response DTO."""
        itinerary = ItineraryRepository.update_itinerary(db, itinerary_id, itinerary_data)
        if not itinerary:
            return None
        return ItineraryResponseDTO.from_orm(itinerary)

    @staticmethod
    def delete_itinerary(db: Session, itinerary_id: int) -> bool:
        """Delete an itinerary by ID and return success status."""
        return ItineraryRepository.delete_itinerary(db, itinerary_id)
  
