from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional

#used to set the request or response how it should look like or defines the structure of the req or response

class PostBase(BaseModel):
    name:str
    details:str
    adult:bool = True

class PostCreate(BaseModel):
    name:str
    details:str
    adult:bool = True

class PostResponse(PostBase):
    
    class Config:   # used for converting sqlalchemy models to pydantic models
        orm_mode = True


class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserResponse(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime

    class Config:
        orm_mode=True

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id : Optional[str]=None