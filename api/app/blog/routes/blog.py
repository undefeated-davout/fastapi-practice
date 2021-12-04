from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import database
from .. import models
from .. import schemas

router = APIRouter()


@router.get('/blogs/{id}',
            status_code=status.HTTP_200_OK,
            response_model=schemas.ShowBlog,
            tags=['blogs'])
def show_blog(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    return blog


@router.get('/blogs', response_model=List[schemas.ShowBlog], tags=['blogs'])
def index_blogs(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.post('/blogs', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create_blog(req: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title=req.title, body=req.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.put('/blogs/{id}',
            status_code=status.HTTP_202_ACCEPTED,
            tags=['blogs'])
def update_blog(id: int,
                req: schemas.Blog,
                db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    print('req.dict()', req.dict())
    print('req', req)
    blog.update(req.dict())
    db.commit()
    return 'Update completed'


@router.delete('/blogs/{id}',
               status_code=status.HTTP_204_NO_CONTENT,
               tags=['blogs'])
def destroy_blog(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Deletion completed'