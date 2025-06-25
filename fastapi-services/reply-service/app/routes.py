from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import CommentCreate, CommentOut
from app.crud import create_comment, get_comments_by_post

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CommentOut)
def create(data: CommentCreate, db: Session = Depends(get_db)):
    return create_comment(db, data)

@router.get("/post/{post_id}", response_model=list[CommentOut])
def get_by_post(post_id: str, db: Session = Depends(get_db)):
    return get_comments_by_post(db, post_id)
