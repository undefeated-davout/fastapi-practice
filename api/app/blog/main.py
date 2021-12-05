from fastapi import FastAPI

from .routes import auth, blog, user
from .utils import database

app = FastAPI()

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)

database.Base.metadata.create_all(database.engine)
