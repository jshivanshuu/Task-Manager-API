from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, auth
from app.dependencies import get_db

router = APIRouter()

@router.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed = auth.hash_password(user.password)
    db_user = models.User(email=user.email, password=hashed)
    db.add(db_user)
    db.commit()
    return {"msg": "User created"}

@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    
    if not db_user or not auth.verify_password(user.password, db_user.password):
        return {"error": "Invalid credentials"}
    
    token = auth.create_token({"user_id": db_user.id})
    return {"access_token": token}