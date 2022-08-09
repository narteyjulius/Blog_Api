import models
from fastapi import FastAPI, status, HTTPException, Response, Depends, APIRouter
from database import get_db

from sqlalchemy.orm import Session

class Crud():
     def __init__(self, model):
          # self

          self.model = model
          # self.data_base = data_base

     def get_items(self, data_base: Session):
          return data_base.query(self).all()
     # def get_item(data_base: Session, model):

     #      return data_base.query(model).all()

     def get_item(self, data_base: Session, item_id: int):
        return data_base.query().filter(item_id).first()


     



def get_item(data_base: Session, model):
     return data_base.query(model).all()

def get_users(data_base: Session, model):
     return data_base.query(model).all()