from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schema
from app.dependencies import get_db

router = APIRouter()

@router.post("/tasks")
def create_task(task: schema.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(**task.dict(), owner_id=1)  # temp user
    db.add(db_task)
    db.commit()
    return db_task

@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()