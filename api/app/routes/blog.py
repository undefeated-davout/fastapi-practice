from typing import List

from app.functions.blog import (
    create_blog,
    destroy_blog,
    index_blog,
    show_blog,
    update_blog,
)
from app.http.request import BlogReq, UserReq
from app.http.response import BlogRes
from app.models.user import UserModel
from app.utils.database import get_db
from app.utils.oauth2 import get_current_user
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/blogs", tags=["blogs"])


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=BlogRes,
)
def show(id: int, db: Session = Depends(get_db)):
    blog = show_blog(id, db)
    return blog


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[BlogRes],
)
def index(db: Session = Depends(get_db)):
    blogs = index_blog(db)
    return blogs


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BlogRes)
def create(
    req: BlogReq,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    blog = create_blog(req, current_user, db)
    return blog


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(
    id: int,
    req: BlogReq,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    update_blog(id, req, db)
    return {}


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    destroy_blog(id, db)
    return {}
