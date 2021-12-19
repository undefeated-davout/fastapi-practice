from fastapi import FastAPI

from .routes import auth, blog, common, user

app = FastAPI()

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(common.router)
app.include_router(user.router)
