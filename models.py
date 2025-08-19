from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    age = Column(Integer)
    weight = Column(Integer)
    height = Column(Integer)
    goals = Column(String)

class Workout(Base):
    __tablename__ = "workout"
    id = Column(Integer, primary_key=True)
    plan_name = Column(String)
    name = Column(String, unique=True)
    user_id = Column(Integer, Foreign_Key=True)
    date = Column(Date)
    exercises = Column(Integer)
    duration = Column(String)

class Nutrition(Base):
    __tablename__ = "nutrition"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    name = Column(String, unique=True)
    user_id = Column(Integer, Foreign_Key=True)
    meals = Column(Integer)
    calories = Column(Integer)
    macros = Column(String)

class Progress(Base):
    Progress: id, user_id, workout_id, sets, reps, weights, notes  
    __tablename__ = "progress"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, Foreign_Key=True)
    sets = Column(Integer)
    workout_id = Column(Integer)
    notes = Column(String)
    weights = Column(Integer)
    reps = Column(Integer)
  

Base.metadata.create_all(bind=engine)