from typing import List

from pydantic import BaseModel


# --- base ---
class BlogBase(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


# --- response ---
class BlogRes(BlogBase):
    creator: UserBase


class LoginRes(BaseModel):
    access_token: str
    token_type: str


class UserRes(UserBase):
    blogs: List[BlogBase] = []
