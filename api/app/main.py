from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session

from .routes import auth, blog, user

app = FastAPI()

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)
