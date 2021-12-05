from typing import List

from pydantic import BaseModel


# --- bases ---
class UserBase(BaseModel):
    name: str
    email: str


class BlogBase(BaseModel):
    title: str
    body: str


# --- models ---
class Login(BaseModel):
    email: str
    password: str


class User(UserBase):
    password: str

    class Config:
        orm_mode = True


class Blog(BlogBase):
    class Config:
        orm_mode = True


# --- shows ---
class ShowUser(UserBase):
    blogs: List[Blog] = []

    class Config:
        orm_mode = True


class ShowBlog(BlogBase):
    creator: ShowUser

    class Config:
        orm_mode = True
