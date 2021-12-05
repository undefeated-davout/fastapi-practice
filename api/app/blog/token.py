import os
from datetime import datetime, timedelta
from typing import Optional

from jose import jwt

SECRET_KEY = os.environ["API_SECRET_KEY"]
ALGORITHM = "HS256"
EXPIRE_MINUTES = 30


def create_access_token(
    password: dict, expires_delta: Optional[timedelta] = None
):
    to_encode = password.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(nimutes=EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
