from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str


class WorkoutCreate(BaseModel):
    plan_name: str
    exercises: int    


class NutritionCreate(BaseModel):
    meals: str
    calories: int
    macros : int