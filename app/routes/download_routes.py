from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.services.download_service import DownloadService
from app.dtos.download_dto import DownloadCreateDTO, DownloadUpdateDTO, DownloadResponseDTO

router = APIRouter(
    prefix="/downloads",
    tags=["Downloads"]
)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new download
@router.post("/", response_model=DownloadResponseDTO)
def create_download(download_data: DownloadCreateDTO, db: Session = Depends(get_db)):
    """Create a new download entry."""
    download_service = DownloadService(db)
    new_download = download_service.create_download(download_data)
    return new_download

# Get a download by ID
@router.get("/{download_id}", response_model=DownloadResponseDTO)
def get_download(download_id: int, db: Session = Depends(get_db)):
    """Retrieve a download by ID."""
    download_service = DownloadService(db)
    download = download_service.get_download_by_id(download_id)
    if download is None:
        raise HTTPException(status_code=404, detail="Download not found")
    return download

# Get all downloads
@router.get("/", response_model=List[DownloadResponseDTO])
def get_all_downloads(db: Session = Depends(get_db)):
    """Retrieve all download records."""
    download_service = DownloadService(db)
    return download_service.get_all_downloads()

# Get downloads by user ID
@router.get("/user/{user_id}", response_model=List[DownloadResponseDTO])
def get_downloads_by_user(user_id: int, db: Session = Depends(get_db)):
    """Retrieve all downloads for a specific user."""
    download_service = DownloadService(db)
    return download_service.get_downloads_by_user(user_id)

# Update a download by ID
@router.put("/{download_id}", response_model=DownloadResponseDTO)
def update_download(download_id: int, download_data: DownloadUpdateDTO, db: Session = Depends(get_db)):
    """Update a download by ID."""
    download_service = DownloadService(db)
    updated_download = download_service.update_download(download_id, download_data)
    if updated_download is None:
        raise HTTPException(status_code=404, detail="Download not found")
    return updated_download

# Delete a download by ID
@router.delete("/{download_id}")
def delete_download(download_id: int, db: Session = Depends(get_db)):
    """Delete a download by ID."""
    download_service = DownloadService(db)
    if not download_service.delete_download(download_id):
        raise HTTPException(status_code=404, detail="Download not found")
    return {"message": "Download deleted successfully"}
