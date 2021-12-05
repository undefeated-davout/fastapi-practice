from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..domain.models import Blog
from ..http.request import BlogReq, UserReq


def show_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available",
        )
    return blog


def index_blog(db: Session):
    blogs = db.query(Blog).all()
    return blogs


def create_blog(
    blog: BlogReq,
    current_user: UserReq,
    db: Session,
):
    new_blog = Blog(title=blog.title, body=blog.body, user_id=current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def update_blog(id: int, new_blog: BlogReq, db: Session):
    old_blog = db.query(Blog).filter(Blog.id == id)
    if not old_blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available",
        )
    old_blog.update(new_blog.dict())
    db.commit()
    return


def destroy_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available",
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return
