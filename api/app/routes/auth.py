from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..functions.auth import login
from ..http.response import LoginRes
from ..utils.database import get_db

router = APIRouter(tags=["auth"])


@router.post("/login", status_code=status.HTTP_200_OK, response_model=LoginRes)
def login_auth(
    req: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    token_res = login(req, db)
    return token_res
