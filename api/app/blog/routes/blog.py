from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from .. import database
from .. import schemas
from ..functions import blog

router = APIRouter(prefix='/blogs', tags=['blogs'])


@router.get('/{id}',
            status_code=status.HTTP_200_OK,
            response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(database.get_db)):
    return blog.show(id, db)


@router.get('/',
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.ShowBlog])
def index(db: Session = Depends(database.get_db)):
    return blog.index(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(req: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(req, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, req: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update(id, req, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db)):
    return blog.destroy(id, db)
