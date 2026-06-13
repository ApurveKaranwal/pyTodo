from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base

class Todo(Base):
    __tablename__ = "todos"

    id =  Column(Integer, primary_key = True, index = True)
    title = Column(String, nullable =  False)
    body = Column(String, nullable = True)
    completed = Column(Boolean, default =  False)

class Auth(Base):
    __tablename__ = "auth"

    id = Column(Integer, primary_key = True, index =  True)
    name = Column(String, nullable = False)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)