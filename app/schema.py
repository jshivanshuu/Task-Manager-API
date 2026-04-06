#for input and output data validation and serialization
from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class Config:
        from_attributes = True