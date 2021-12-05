from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..domain.models import UserModel
from ..utils.hashing import Hash
from ..utils.token import create_access_token


def login(oauth_req: OAuth2PasswordRequestForm, db: Session):
    db_user = (
        db.query(UserModel)
        .filter(UserModel.email == oauth_req.username)
        .first()
    )
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials",
        )
    if not Hash.verify(db_user.password, oauth_req.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
        )
    access_token = create_access_token(
        claims={"id": db_user.id, "email": oauth_req.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}