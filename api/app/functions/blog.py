from typing import List

from app.http.request import BlogReq, UserReq
from app.models.blog import BlogModel
from fastapi import HTTPException, status
from sqlalchemy.orm import Session


def show_blog(id: int, db: Session) -> BlogModel:
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available",
        )
    return blog


def index_blog(db: Session) -> List[BlogModel]:
    blogs = db.query(BlogModel).all()
    return blogs


def create_blog(
    blog: BlogReq,
    current_user: UserReq,
    db: Session,
) -> BlogModel:
    new_blog = BlogModel(
        title=blog.title, body=blog.body, user_id=current_user.id
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def update_blog(id: int, blog: BlogReq, db: Session):
    db_blog = db.query(BlogModel).filter(BlogModel.id == id)
    if not db_blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available",
        )
    db_blog.update(blog.dict())
    db.commit()
    return


def destroy_blog(id: int, db: Session):
    blog = db.query(BlogModel).filter(BlogModel.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available",
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return
