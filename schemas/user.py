from pydantic import BaseModel, EmailStr

# Properties to recieve user create by client
class UserCreate(BaseModel):
     password : str
     email: EmailStr

     class Config:
          orm_mode = True

#Properties sent out to client 
class UserOut(BaseModel):
     email: EmailStr

     class Config:
          orm_mode = True