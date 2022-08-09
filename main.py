from fastapi import FastAPI
from config import settings
import database

from config import settings
from routers import post, user, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.on_event("startup")
async def startup():
     # print("connecting to database")
     print(
        f"Connecting to database........\n Database Name: {settings.database_name}\n Database Password: {settings.database_password}\n Token Expire: {settings.access_token_expire_minutes}")

     database.SQLALCHEMY_DATABASE_URL


@app.on_event("shutdown")
async def shutdown():
     print("Disconnecting database")
     database.SQLALCHEMY_DATABASE_URL


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(post.router)
app.include_router(user.router)

