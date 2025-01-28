from sqlalchemy.orm import Session
from app.models.download import Download
from app.dtos.download_dto import DownloadCreateDTO, DownloadUpdateDTO

class DownloadRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_download(self, download_data: DownloadCreateDTO) -> Download:
        """Creates a new download record."""
        new_download = Download(**download_data.model_dump())
        self.db.add(new_download)
        self.db.commit()
        self.db.refresh(new_download)
        return new_download

    def get_download_by_id(self, download_id: int) -> Download:
        """Fetches a download record by ID."""
        return self.db.query(Download).filter(Download.id == download_id).first()

    def get_all_downloads(self):
        """Retrieves all download records."""
        return self.db.query(Download).all()

    def get_downloads_by_user(self, user_id: int):
        """Retrieves all downloads associated with a specific user."""
        return self.db.query(Download).filter(Download.user_id == user_id).all()

    def update_download(self, download_id: int, download_data: DownloadUpdateDTO) -> Download:
        """Updates an existing download record."""
        db_download = self.get_download_by_id(download_id)
        if db_download:
            update_data = download_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_download, key, value)
            self.db.commit()
            self.db.refresh(db_download)
        return db_download

    def delete_download(self, download_id: int) -> bool:
        """Deletes a download record by ID."""
        db_download = self.get_download_by_id(download_id)
        if db_download:
            self.db.delete(db_download)
            self.db.commit()
            return True
        return False
