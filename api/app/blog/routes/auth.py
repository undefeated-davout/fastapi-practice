from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import database, schemas
from ..functions import auth

router = APIRouter(tags=["auth"])


@router.post("/login", status_code=status.HTTP_200_OK)
def login(req: schemas.Login, db: Session = Depends(database.get_db)):
    return auth.login(req, db)
