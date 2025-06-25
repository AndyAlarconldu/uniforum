from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import PostCreate, PostOut
from app.crud import create_post, get_posts

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PostOut)
def create(data: PostCreate, db: Session = Depends(get_db)):
    return create_post(db, data)

@router.get("/", response_model=list[PostOut])
def list_all(db: Session = Depends(get_db)):
    return get_posts(db)
