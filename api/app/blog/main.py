from fastapi import FastAPI, Depends
from .schemas import Blog
from .models import Base
from . import models
from .database import engine, sessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(engine)


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blog")
def create(blog: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
