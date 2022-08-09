from fastapi import FastAPI, status, HTTPException, Response, Depends, APIRouter
from typing import List, Optional
from sqlalchemy.orm import Session
import models, oauth2, crud
from crud import Crud
from database import get_db
# import schemas
from schemas.post import PostCreate, PostOut


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)


@router.get("/", response_model=List[PostOut]) 
def get_posts(db: Session = Depends(get_db)):
     # posts = crud.get_item(data_base= db, model=models.Post)
     posts = Crud.get_items(data_base=db,self=models.Post)
     return posts


@router.get("/{id}", response_model=PostOut) 
def get_post(id:int, db: Session = Depends(get_db)):
     post = db.query(models.Post).filter(models.Post.id == id).first()

     if post == None:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
          detail=f"post with id: {id} was not found or does not exist")
     return post

# def get_posts(db: Session = Depends(get_db)):
#      posts = db.query(models.Post).all()
#      return posts

@router.post("/",   status_code=status.HTTP_201_CREATED)
def  create_post(post:PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
     # new_post = models.Post(**post.dict())
     new_post = models.Post(owner_id=current_user.id,**post.dict())
     db.add(new_post)
     db.commit()
     db.refresh(new_post)
     return new_post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def  delete_post(id:int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
     post_query = db.query(models.Post).filter(models.Post.id == id)
     post = post_query.first()
     if post == None:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
          detail=f"post with id: {id} was not found or does not exist")

     # if post.owner_id != current_user.id:
     #      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

     post_query.delete(synchronize_session=False)
     db.commit()

     return Response(status_code=status.HTTP_204_NO_CONTENT)

