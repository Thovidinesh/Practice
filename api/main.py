from typing import Optional,List
from fastapi import FastAPI, Response , status,HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from .database import  engine, get_db
from .schemas import PostBase, PostResponse, UserResponse
from api import schemas,utils,models
from .routers import post,user,auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


try:
    conn=psycopg2.connect(host='localhost' ,database='fastapi' , user='postgres', password='1812',cursor_factory=RealDictCursor)
    cursor=conn.cursor()
    print("Database Connection was successful!")
except Exception as error:
    print("Connecting to database failed")
    print("Error: ",error)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message":"Hello,Welcome to my API"}



