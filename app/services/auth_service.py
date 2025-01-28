from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.dtos.auth_dto import LoginRequestDTO
from app.repositories.user_repository import UserRepository
from sqlalchemy.orm import Session
from fastapi import HTTPException

# Secret key and algorithm for JWT
SECRET_KEY = "your_secret_key"  # Replace with a strong secret in .env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

class AuthService:
    @staticmethod
    def authenticate_user(db: Session, login_data: LoginRequestDTO):
        user = UserRepository.get_user_by_email(db, login_data.email)
        if not user or login_data.password != user.password:  # Direct password comparison
            raise HTTPException(status_code=401, detail="Invalid email or password")
        return user

    @staticmethod
    def create_access_token(user, expires_delta: timedelta = None):
        """
        Generate JWT token with user data.
        :param user: User object containing email and full_name
        :param expires_delta: Expiration time for the token
        :return: Encoded JWT token
        """
        to_encode = {
            "sub": user.email,
            "full_name": user.full_name  # Adding full_name to the token
        }
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
