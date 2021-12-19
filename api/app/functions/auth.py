from app.models.user import UserModel
from app.utils.hashing import Hash
from app.utils.token import create_access_token
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


def login(oauth_req: OAuth2PasswordRequestForm, db: Session) -> dict[str, str]:
    user = (
        db.query(UserModel)
        .filter(UserModel.email == oauth_req.username)
        .first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials",
        )
    if not Hash.verify(user.password, oauth_req.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
        )
    access_token = create_access_token(
        claims={"id": user.id, "email": oauth_req.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}
