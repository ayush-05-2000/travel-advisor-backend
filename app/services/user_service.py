from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.dtos.user_dto import UserCreateDTO, UserUpdateDTO, UserResponseDTO
from typing import List, Optional

class UserService:

    @staticmethod
    def create_user(db: Session, user_data: UserCreateDTO) -> UserResponseDTO:
        """Creates a new user and returns response DTO."""
        new_user = UserRepository.create_user(db, user_data)
        return UserResponseDTO(
            id=new_user.id,
            full_name=new_user.full_name,
            email=new_user.email,
            preferences=new_user.preferences,
            created_at=new_user.created_at
        )

    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> Optional[UserResponseDTO]:
        """Fetches a user by ID and returns response DTO if found."""
        user = UserRepository.get_user_by_id(db, user_id)
        if user:
            return UserResponseDTO(
                id=user.id,
                full_name=user.full_name,
                email=user.email,
                preferences=user.preferences,
                created_at=user.created_at
            )
        return None

    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Optional[UserResponseDTO]:
        """Fetches a user by email and returns response DTO if found."""
        user = UserRepository.get_user_by_email(db, email)
        if user:
            return UserResponseDTO(
                id=user.id,
                full_name=user.full_name,
                email=user.email,
                preferences=user.preferences,
                created_at=user.created_at
            )
        return None

    @staticmethod
    def get_all_users(db: Session) -> List[UserResponseDTO]:
        """Fetches all users and returns them as response DTOs."""
        users = UserRepository.get_all_users(db)
        return [
            UserResponseDTO(
                id=user.id,
                full_name=user.full_name,
                email=user.email,
                preferences=user.preferences,
                created_at=user.created_at
            ) for user in users
        ]

    @staticmethod
    def update_user(db: Session, user_id: int, user_update: UserUpdateDTO) -> Optional[UserResponseDTO]:
        """Updates user details and returns updated response DTO."""
        updated_user = UserRepository.update_user(db, user_id, user_update)
        if updated_user:
            return UserResponseDTO(
                id=updated_user.id,
                full_name=updated_user.full_name,
                email=updated_user.email,
                preferences=updated_user.preferences,
                created_at=updated_user.created_at
            )
        return None

    @staticmethod
    def delete_user(db: Session, user_id: int) -> bool:
        """Deletes a user and returns a boolean indicating success."""
        return UserRepository.delete_user(db, user_id)
  
