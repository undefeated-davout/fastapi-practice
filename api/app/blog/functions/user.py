from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import hashing, models, schemas


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id {id} is not available",
        )
    return user


def create(user: schemas.User, db: Session):
    hashed_password = hashing.Hash.bcrypt(user.password)
    new_user = models.User(
        name=user.name, email=user.email, password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
