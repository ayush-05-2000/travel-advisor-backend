from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.auth_service import AuthService
from app.dtos.auth_dto import LoginRequestDTO, TokenResponseDTO

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login", response_model=TokenResponseDTO)
def login(login_data: LoginRequestDTO, db: Session = Depends(get_db)):
    """Handle user login and return JWT token."""
    user = AuthService.authenticate_user(db, login_data)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = AuthService.create_access_token(user)
    return {"access_token": access_token, "token_type": "bearer"}
