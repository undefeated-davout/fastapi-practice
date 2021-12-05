from pydantic import BaseModel


class BlogReq(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


class UserReq(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True
