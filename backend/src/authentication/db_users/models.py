from sqlalchemy import Column,Integer, String

from .database import Base

class User(Base):
    __tablename__ = "usersprofiles"
    user_id = Column(Integer,primary_key=True,index=True)
    username = Column(String(255),unique=True,index=True)
    password = Column(String(255),index=True)