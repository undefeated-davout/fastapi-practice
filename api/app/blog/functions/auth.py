from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..domain.models import User
from ..utils import hashing, token


def login(oauth_req: OAuth2PasswordRequestForm, db: Session):
    db_user = db.query(User).filter(User.email == oauth_req.username).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials",
        )
    if not hashing.Hash.verify(db_user.password, oauth_req.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
        )
    access_token = token.create_access_token(
        claims={"id": db_user.id, "email": oauth_req.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}
