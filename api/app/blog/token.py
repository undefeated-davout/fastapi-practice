import os
from datetime import datetime, timedelta
from typing import Optional

from jose import jwt

SECRET_KEY = os.environ["API_SECRET_KEY"]
ALGORITHM = "HS256"
EXPIRE_MINUTES = 30


def create_access_token(
    claims: dict, expires_delta: Optional[timedelta] = None
):
    if expires_delta:
        expired_time = datetime.utcnow() + expires_delta
    else:
        expired_time = datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTES)
    to_encode = claims.copy()
    to_encode.update({"exp": expired_time})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
