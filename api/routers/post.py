from fastapi import FastAPI, Response , status,HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import  get_db
from .. import schemas,models,oauth2
from typing import List

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/",response_model=List[schemas.PostResponse])
async def get_posts(db:Session = Depends(get_db), current_user=Depends(oauth2.get_current_user)):
    #cursor.execute("""SELECT * FROM users""")
    #users=cursor.fetchall()
    posts= db.query(models.Post).all()
    #.filter(models.Post.user_id == current_user.id) is used to retrieve only the posts of the current user
    return posts   

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.PostResponse)
def create_post(post: schemas.PostCreate,db:Session = Depends(get_db), current_user=Depends(oauth2.get_current_user)):
    #cursor.execute("""INSERT INTO users (name,email,adult) values ( %s, %s, %s) RETURNING *""",(post.name,post.email,post.adult))
    #new_user=cursor.fetchone()
    #conn.commit()
    print(current_user.id)
    new_post=models.Post(user_id=current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}",response_model=schemas.PostResponse)
def get_post(id: int,db:Session=Depends(get_db), current_user=Depends(oauth2.get_current_user)):
    #cursor.execute("""SELECT * FROM users WHERE id= %s """, (str(id)))
    #find_user=cursor.fetchone()
    find_post=db.query(models.Post).filter(models.Post.id == id).first()
    if not find_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Id with {id} was not found")
    
    
    return find_post


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int,db:Session=Depends(get_db), current_user=Depends(oauth2.get_current_user)):
    #cursor.execute("""DELETE FROM users WHERE id= %s returning *""",(str(id),))
    #delete_user=cursor.fetchone()
    #conn.commit()
    post_query =db.query(models.Post).filter(models.Post.id==id)
    post = post_query.first()
    if post ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"post with {id} doesnt exist")
    
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform this action")
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}",response_model=schemas.PostResponse)
def update_posts(id: int, post:schemas.PostCreate,db:Session=Depends(get_db), current_user=Depends(oauth2.get_current_user)):
    #cursor.execute("""UPDATE users SET name=%s,email=%s,adult=%s WHERE id= %s RETURNING *""",(post.name,post.email,post.adult, str(id)))
    #update_user=cursor.fetchone()
    #conn.commit()
    update_query=db.query(models.Post).filter(models.Post.id==id)
    posts=update_query.first()

    if posts==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"post with {id} doesnt exist")
    
    if posts.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform this action")
    update_query.update(post.dict(),synchronize_session=False)
    db.commit()
    return  update_query.first()