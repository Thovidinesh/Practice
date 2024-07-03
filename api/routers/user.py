from fastapi import FastAPI, Response , status,HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import  engine, get_db
from .. import schemas,utils,models


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def get_user(db:Session=Depends(get_db)):
    users=db.query(models.User).all()
    return users

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserResponse)
def create_user(user:schemas.UserCreate, db:Session=Depends(get_db)):

    #hash the password - user.password
    hashed_password= utils.hash(user.password)
    user.password = hashed_password
    new_user=models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}",response_model=schemas.UserResponse)
def get_user(id: int,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with {id} not exist")
    
    return user

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int,db:Session=Depends(get_db)):
    user_delete=db.query(models.User).filter(models.User.id==id)
    if user_delete.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with {id} not exists")
    
    user_delete.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)