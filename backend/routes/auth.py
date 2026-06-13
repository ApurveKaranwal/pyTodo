from backend.main import AuthModel
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import Base, engine, SessionLocal
from model.model import Auth as Authmodel
from schema.todo import Auth

router =  APIRouter()

Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(
    auth : Auth,
    db: Session = Depends(get_db)
):
    new_user = AuthModel(
        name = auth.name,
        email = auth.email,
        password = auth.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/signin")
def signin(
    auth: Auth,
    db: Session = Depends(get_db)
):
    user = db.query(AuthModel).filter(
        AuthModel.email == auth.email
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="No user found with this email"
        )

    return{
        "message" : "User found",
        "email": user.email
            
        }