from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..domain.models import User
from ..http.request import UserReq
from ..utils import hashing


def show_user(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id {id} is not available",
        )
    return user


def create_user(user: UserReq, db: Session):
    hashed_password = hashing.Hash.bcrypt(user.password)
    new_user = User(name=user.name, email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
