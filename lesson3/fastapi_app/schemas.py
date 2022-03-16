from typing import List

from pydantic.main import BaseModel


class BlogBase(BaseModel):
    title: str
    content: str
    owner_id: int


class Blog(BlogBase):
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    blogs: List[Blog] = []

    class Config:
        orm_mode = True
