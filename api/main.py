from typing import Optional
from fastapi import FastAPI, Response , status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange



app = FastAPI()

my_users=[{"user1":"First User","email":"abc@gmail.com","id":1},
          {"user2":"Second User","email":"xyz@gmail.com","id":2}]

def find_post(id):
    for i in my_users:
        if i["id"]==id:
            return i

def find_index(id):
    for i, p in enumerate(my_users):
        if p["id"]==id:
            return i

class Post(BaseModel):
    user:str
    email:str
    age:Optional[int] =None

@app.get("/")
async def root():
    return {"message":"Hello,Welcome to my API"}

@app.get("/posts")
async def posts():
    return {"data":my_users}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create(payload: Post):
    payload_dict=payload.dict()
    payload_dict['id']=randrange(0,100000)
    my_users.append(payload_dict)
    return {"Data":payload_dict}   

@app.get("/posts/latest")
def get_latest():
    post=my_users[len(my_users)-1]
    return {"detail": post}

@app.get("/posts/{id}")
def get_post(id: int,response: Response):
    post=find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Id with {id} was not found")
        #response.status_code=status.HTTP_404_NOT_FOUND
        #return {f"Id with {id} was not found"}
    return {"data":post}

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int):
    index=find_index(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"post with {id} doesnt exist")
    my_users.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_posts(id: int, post:Post):
    index=find_index(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"post with {id} doesnt exist")
    post_dict=post.dict()
    post_dict['id']=id
    my_users[index]=post_dict
    return {'data': post_dict}