from pydantic import BaseModel, EmailStr
from .user import UserOut


#BasePost for Post 
class PostBase(BaseModel):
     id: int 
     title: str
     content: str

# Properties shared by models stored in DB
class PostOut(PostBase):
     owner : UserOut
     class Config:
        orm_mode = True



class PostCreate(BaseModel):
     title: str
     content: str

     class Config:
          orm_mode = True