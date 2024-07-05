from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

#used to create columns in the database

class Post(Base):
    __tablename__= "posts"

    id=Column(Integer,primary_key=True,nullable=False)
    name=Column(String,nullable=False)
    details=Column(String,nullable=False,unique=True)
    adult=Column(Boolean,server_default='True',nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    user_id=Column(Integer,ForeignKey("users.id", on_delete="CASCADE"), nullable=False)

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,nullable=False)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))