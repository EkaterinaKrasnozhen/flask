import databases

from fastapi import FastAPI
from pydantic import BaseModel, Field

class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)
    password: str = Field(min_length=6)

class User(UserIn):
    id: int
    
class PostIn(BaseModel):
    user_id: int
    post: str = Field(max_length=128)
    
class Post(BaseModel):
    id: int
    user_id: int
    post: str = Field(max_length=128)
