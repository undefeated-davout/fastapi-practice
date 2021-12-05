from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models
from .. import hashing
from .. import schemas


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not available')
    return user


def create(req: schemas.User, db: Session):
    hashed_password = hashing.Hash.bcrypt(req.password)
    new_user = models.User(name=req.name,
                           email=req.email,
                           password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
