from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str

@app.post("/")
def create(blog: Blog):
    return {'data': blog}
