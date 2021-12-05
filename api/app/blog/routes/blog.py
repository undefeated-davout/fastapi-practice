from typing import List

from fastapi import APIRouter, Depends, status
from pydantic.main import BaseModel
from sqlalchemy.orm import Session

from ..functions.blog import (
    create_blog,
    destroy_blog,
    index_blog,
    show_blog,
    update_blog,
)
from ..http.request import BlogReq, UserReq
from ..http.response import BlogRes
from ..utils import database, oauth2

router = APIRouter(prefix="/blogs", tags=["blogs"])


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=BlogReq,
)
def show(id: int, db: Session = Depends(database.get_db)):
    blog = show_blog(id, db)
    return blog


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[BlogRes],
)
def index(db: Session = Depends(database.get_db)):
    blogs = index_blog(db)
    return blogs


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BlogReq)
def create(
    req: BlogReq,
    db: Session = Depends(database.get_db),
    current_user: UserReq = Depends(oauth2.get_current_user),
):
    blog = create_blog(req, current_user, db)
    return blog


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(
    id: int,
    req: BlogReq,
    db: Session = Depends(database.get_db),
    current_user: UserReq = Depends(oauth2.get_current_user),
):
    update_blog(id, req, db)
    return {}


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: UserReq = Depends(oauth2.get_current_user),
):
    destroy_blog(id, db)
    return {}
