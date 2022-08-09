from fastapi import FastAPI, status, HTTPException, Response, Depends, APIRouter
from typing import List, Optional
from sqlalchemy.orm import Session
import models
from database import get_db
# import schemas
import utils, crud
from schemas.user import UserCreate, UserOut


router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.get("/", response_model=List[UserOut]) 
def get_users(db: Session = Depends(get_db)):
     users = crud.get_item(data_base= db, model=models.User)
     return users


@router.post("/",status_code=status.HTTP_201_CREATED, response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

     # db_user = crud.get_user_by_email(db, email=user.email)

     old_users = db.query(models.User).filter(models.User.email == user.email).all()

     if old_users:
          raise HTTPException(status_code=400, detail="Email already registered")

     hashed_password = utils.hash(user.password)
     user.password = hashed_password

     new_user = models.User(**user.dict())
     db.add(new_user)
     db.commit()
     db.refresh(new_user) 
     return new_user