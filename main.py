from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from db import get_db
from models import Workout,Users,Nutrition,Progress
from schema import UserCreate,WorkoutCreate,NutritionCreate

app = FastAPI()

@app.post("/auth/register")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/auth/login")
def get_users(db: Session = Depends(get_db),user: UserCreate):
    return db.query(user).all()


@app.get("/auth/user/{user_id}")
def get_profile(user_id:int):
    return db.query({User:user_id})


@app.post("/create/workout")
def create_user(workout: WorkoutCreate, db: Session = Depends(get_db)):
    db_workout = Workout(**workout.dict())
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout    


@app.post("/create/nutrition")
def create_user(workout: WorkoutCreate, db: Session = Depends(get_db)):
    db_nutrition = Nutrition(**nutrition.dict())
    db.add(db_nutrition)
    db.commit()
    db.refresh(db_nutrition)
    return db_nutrition  















