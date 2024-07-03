# this is used to store some utility functions

from passlib.context import CryptContext

#this will be telling to use bcrypt algorithm
pwd_context= CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password,hashed_password)