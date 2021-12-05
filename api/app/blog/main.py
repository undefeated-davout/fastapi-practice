from fastapi import FastAPI

from . import database
from .routes import auth, blog, user

app = FastAPI()

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)

database.Base.metadata.create_all(database.engine)
