from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

# from blog.database import Base
from database import Base

class Post(Base):

     __tablename__ = "posts"

     id = Column(Integer, primary_key=True, index=True)
     title = Column(String, nullable=False)
     content = Column(String, nullable=False)
     published = Column(Boolean, server_default='TRUE', nullable=False)
     created_at = Column(TIMESTAMP(timezone=True),
                         nullable=False, server_default=text('now()'))

     owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)


    #facthing data from User model
     owner = relationship("User", back_populates="posts")


class User(Base):

     __tablename__ = "users"

     id = Column(Integer, primary_key=True, index=True)
     email = Column(String, nullable=False, unique=True)
     password = Column(String, nullable=False)
     date_joined = Column(TIMESTAMP(timezone=True),
                         nullable=False, server_default=text('now()'))

     posts = relationship("Post", back_populates="owner")