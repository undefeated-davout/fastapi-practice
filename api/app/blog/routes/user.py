from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import database
from .. import schemas
from ..functions import user

router = APIRouter(prefix='/users', tags=['users'])


@router.get('/{id}',
            status_code=status.HTTP_200_OK,
            response_model=schemas.ShowUser)
def show(id: int, db: Session = Depends(database.get_db)):
    return user.show(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(req: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(req, db)
