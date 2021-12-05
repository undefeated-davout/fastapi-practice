from fastapi import FastAPI

from .routes import auth, blog, user
from .utils.database import Base, engine

app = FastAPI()

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)

Base.metadata.create_all(engine)  # テーブル構築
