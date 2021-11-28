from fastapi import FastAPI
from .schemas import Blog

app = FastAPI()

@app.post("/")
def create(blog: Blog):
    return {'data': blog}
