from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database
from ..functions import auth

router = APIRouter(tags=["auth"])


@router.post("/login", status_code=status.HTTP_200_OK)
def login(
    req: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):
    return auth.login(req, db)
