from app.http.request import UserReq
from app.models.user import UserModel
from app.utils.hashing import Hash
from fastapi import HTTPException, status
from sqlalchemy.orm import Session


def show_user(id: int, db: Session):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id {id} is not available",
        )
    return user


def create_user(user: UserReq, db: Session):
    hashed_password = Hash.bcrypt(user.password)
    new_user = UserModel(
        name=user.name, email=user.email, password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
