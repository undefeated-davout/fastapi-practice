from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import hashing, models, schemas, token


def login(user: schemas.User, db: Session):
    db_user = (
        db.query(models.User).filter(models.User.email == user.email).first()
    )
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials",
        )
    if not hashing.Hash.verify(db_user.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
        )
    access_token = token.create_access_token(claims={"email": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
