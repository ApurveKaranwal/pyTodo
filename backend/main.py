''' use python3 -m venv venv
    source venv/bin/activate
    uvicorn main:app --reload'''
from types import BuiltinMethodType

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from db.database import Base, engine, SessionLocal
from model.model import Todo as TodoModel
from schema.todo import Todo

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Todo API Running"}

@app.post("/todo")
def create_todo(
    todo: Todo,
    db: Session = Depends(get_db)
):
    new_todo = TodoModel(
        title = todo.title,
        body = todo.body,
        completed = todo.completed
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo

@app.get("/todos")
def get_todos(
    db: Session = Depends(get_db)
):
    return db.query(TodoModel).all()