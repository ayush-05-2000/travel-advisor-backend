from sqlalchemy.orm import Session
from app.models.user import User
from app.dtos.user_dto import UserCreateDTO, UserUpdateDTO
from typing import List, Optional

class UserRepository:

    @staticmethod
    def create_user(db: Session, user_data: UserCreateDTO) -> User:
        new_user = User(
            full_name=user_data.full_name,
            email=user_data.email,
            password=user_data.password,  # Store password as plain text (no hashing)
            preferences=user_data.preferences
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_all_users(db: Session) -> List[User]:
        return db.query(User).all()

    @staticmethod
    def update_user(db: Session, user_id: int, user_update: UserUpdateDTO) -> Optional[User]:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            for key, value in user_update.model_dump().items():
                if value is not None:
                    setattr(user, key, value)
            db.commit()
            db.refresh(user)
        return user

    @staticmethod
    def delete_user(db: Session, user_id: int) -> bool:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
            return True
        return False
