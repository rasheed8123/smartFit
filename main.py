from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from db import get_db

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)


Base.metadata.create_all(bind=engine)

class UserCreate(BaseModel):
    name: str
    email: str

app = FastAPI()


@app.post("/auth/register")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users")
def get_users(db: Session = Depends(get_db),user: UserCreate):
    return db.query(user).all()


@app.get("/auth/user/{user_id}")
def get_profile(user_id:int):
    return db.query({User:user_id})








