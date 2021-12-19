from app.functions.user import create_user, show_user
from app.http.request import UserReq
from app.http.response import UserRes
from app.utils.database import get_db
from app.utils.oauth2 import get_current_user
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["users"])


@router.get(
    "/me",
    status_code=status.HTTP_200_OK,
    response_model=UserRes,
)
def read_users_me(
    db: Session = Depends(get_db),
    current_user: UserReq = Depends(get_current_user),
):
    return current_user


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=UserRes,
)
def show(id: int, db: Session = Depends(get_db)):
    user = show_user(id, db)
    return user


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserRes)
def create(req: UserReq, db: Session = Depends(get_db)):
    user = create_user(req, db)
    return user
