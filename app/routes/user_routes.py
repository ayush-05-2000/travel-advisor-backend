from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.services.user_service import UserService
from app.dtos.user_dto import UserCreateDTO, UserUpdateDTO, UserResponseDTO

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponseDTO)
def create_user(user_data: UserCreateDTO, db: Session = Depends(get_db)):
    """Endpoint to create a new user"""
    existing_user = UserService.get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = UserService.create_user(db, user_data)
    return new_user

@router.get("/{user_id}", response_model=UserResponseDTO)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Endpoint to fetch a user by ID"""
    user = UserService.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=List[UserResponseDTO])
def get_all_users(db: Session = Depends(get_db)):
    """Endpoint to fetch all users"""
    users = UserService.get_all_users(db)
    return users

@router.put("/{user_id}", response_model=UserResponseDTO)
def update_user(user_id: int, user_update: UserUpdateDTO, db: Session = Depends(get_db)):
    """Endpoint to update user details"""
    updated_user = UserService.update_user(db, user_id, user_update)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Endpoint to delete a user"""
    deleted = UserService.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
