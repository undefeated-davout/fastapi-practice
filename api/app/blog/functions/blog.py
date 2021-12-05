from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models
from .. import schemas


def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    return blog


def index(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(blog: schemas.Blog, db: Session):
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def update(id: int, new_blog: schemas.Blog, db: Session):
    old_blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not old_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    old_blog.update(new_blog.dict())
    db.commit()
    return 'Update completed'


def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Deletion completed'
