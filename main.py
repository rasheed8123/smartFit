from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from db import get_db
from models import Workout,Users,Nutrition,Progress
from schema import UserCreate,WorkoutCreate,NutritionCreate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
import chromadb

client = chromadb.CloudClient()


vector_store_from_client = Chroma(
    client=client,
    collection_name="smart_fit",
    embedding_function=embeddings,
)

app = FastAPI()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
embeddings_model = OpenAIEmbeddings()

def embeddings_storing(data):
    for text in range(len(data)):
        embeddings = embeddings_model.embed_query(text)
        vector_store_from_client.add_documents(documents=embeddings)



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
def create_workout(workout: WorkoutCreate, db: Session = Depends(get_db)):
    db_workout = Workout(**workout.dict())
    texts = text_splitter.split_text(db_workout)
    embeddings_storing(data)
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout    


@app.post("/create/nutrition")
def create_nutrition(workout: WorkoutCreate, db: Session = Depends(get_db)):
    db_nutrition = Nutrition(**nutrition.dict())
    db.add(db_nutrition)
    db.commit()
    db.refresh(db_nutrition)
    return db_nutrition  



# @app.get("/askai/{query}")
# def get_answer(query:str):
#     results = vector_store.similarity_search_by_vector(
#     embedding=embeddings.embed_query(query), k=1)
#     return   












