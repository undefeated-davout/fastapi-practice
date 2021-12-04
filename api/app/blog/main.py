from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import database
from . import hashing
from . import models
from . import schemas

app = FastAPI()

database.Base.metadata.create_all(database.engine)


def get_db():
    db = database.sessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- users ---
@app.post('/users', status_code=status.HTTP_201_CREATED, tags=['users'])
def create_user(req: schemas.User, db: Session = Depends(get_db)):
    hashed_password = hashing.Hash.bcrypt(req.password)
    new_user = models.User(name=req.name,
                           email=req.email,
                           password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/users/{id}',
         status_code=status.HTTP_200_OK,
         response_model=schemas.ShowUser,
         tags=['users'])
def show_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not available')
    return user


# --- blogs ---
@app.get('/blogs/{id}',
         status_code=status.HTTP_200_OK,
         response_model=schemas.ShowBlog,
         tags=['blogs'])
def show_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    return blog


@app.get('/blogs', response_model=List[schemas.ShowBlog], tags=['blogs'])
def index_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.post('/blogs', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create_blog(req: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=req.title, body=req.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.put('/blogs/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update_blog(id: int, req: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    print('req.dict()', req.dict())
    print('req', req)
    blog.update(req.dict())
    db.commit()
    return 'Update completed'


@app.delete('/blogs/{id}',
            status_code=status.HTTP_204_NO_CONTENT,
            tags=['blogs'])
def destroy_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Deletion completed'
