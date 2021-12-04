from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import database
from .. import hashing
from .. import models
from .. import schemas

router = APIRouter()


@router.get('/users/{id}',
            status_code=status.HTTP_200_OK,
            response_model=schemas.ShowUser,
            tags=['users'])
def show_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not available')
    return user


@router.post('/users', status_code=status.HTTP_201_CREATED, tags=['users'])
def create_user(req: schemas.User, db: Session = Depends(database.get_db)):
    hashed_password = hashing.Hash.bcrypt(req.password)
    new_user = models.User(name=req.name,
                           email=req.email,
                           password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
