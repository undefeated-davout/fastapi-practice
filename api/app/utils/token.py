import os
from datetime import datetime, timedelta
from typing import Optional

from app.models.user import UserModel
from jose import jwt
from jose.exceptions import JWTError
from sqlalchemy.orm import Session

from ..functions.user import show_user

SECRET_KEY = os.environ["JWT_SECRET_KEY"]
ALGORITHM = "HS256"
EXPIRE_MINUTES = 30


def create_access_token(
    claims: dict, expires_delta: Optional[timedelta] = None
) -> str:
    if expires_delta:
        expired_time = datetime.utcnow() + expires_delta
    else:
        expired_time = datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTES)
    to_encode = claims.copy()
    to_encode.update({"exp": expired_time})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_user_from_token(token: str, exception, db: Session) -> UserModel:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        user_id: int = payload.get("id")
        if user_id is None or email is None:
            raise exception
    except JWTError:
        raise exception
    user: UserModel = show_user(user_id, db)
    return user
