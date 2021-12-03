from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models
from .database import engine, sessionLocal
from .models import Base
from .schemas import Blog, ShowBlog, User

app = FastAPI()

Base.metadata.create_all(engine)


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- users ---
@app.post('/users', status_code=status.HTTP_201_CREATED)
def create_user(req: User, db: Session = Depends(get_db)):
    new_user = models.User(name=req.name,
                           email=req.email,
                           password=req.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# --- blogs ---
@app.get('/blogs/{id}',
         status_code=status.HTTP_200_OK,
         response_model=ShowBlog)
def show_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    return blog


@app.get('/blogs', response_model=List[ShowBlog])
def index_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.post('/blogs', status_code=status.HTTP_201_CREATED)
def create_blog(req: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=req.title, body=req.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.put('/blogs/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, req: Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    print('req.dict()', req.dict())
    print('req', req)
    blog.update(req.dict())
    db.commit()
    return 'Update completed'


@app.delete('/blogs/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Deletion completed'
