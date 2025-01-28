from sqlalchemy.orm import Session
from app.repositories.download_repository import DownloadRepository
from app.dtos.download_dto import DownloadCreateDTO, DownloadUpdateDTO, DownloadResponseDTO
from typing import List, Optional

class DownloadService:
    def __init__(self, db: Session):
        self.download_repo = DownloadRepository(db)

    def create_download(self, download_data: DownloadCreateDTO) -> DownloadResponseDTO:
        """Business logic to create a new download and return a response DTO."""
        download = self.download_repo.create_download(download_data)
        return DownloadResponseDTO.from_orm(download)

    def get_download_by_id(self, download_id: int) -> Optional[DownloadResponseDTO]:
        """Fetch download by ID and return response DTO."""
        download = self.download_repo.get_download_by_id(download_id)
        if download:
            return DownloadResponseDTO.from_orm(download)
        return None

    def get_all_downloads(self) -> List[DownloadResponseDTO]:
        """Retrieve all downloads and return response DTOs."""
        downloads = self.download_repo.get_all_downloads()
        return [DownloadResponseDTO.from_orm(download) for download in downloads]

    def get_downloads_by_user(self, user_id: int) -> List[DownloadResponseDTO]:
        """Retrieve all downloads for a specific user."""
        downloads = self.download_repo.get_downloads_by_user(user_id)
        return [DownloadResponseDTO.from_orm(download) for download in downloads]

    def update_download(self, download_id: int, download_data: DownloadUpdateDTO) -> Optional[DownloadResponseDTO]:
        """Update a download and return the updated response DTO."""
        updated_download = self.download_repo.update_download(download_id, download_data)
        if updated_download:
            return DownloadResponseDTO.from_orm(updated_download)
        return None

    def delete_download(self, download_id: int) -> bool:
        """Delete a download and return success status."""
        return self.download_repo.delete_download(download_id)
