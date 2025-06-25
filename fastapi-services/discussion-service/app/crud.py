from sqlalchemy.orm import Session
from app.models import Post
from app.schemas import PostCreate

def create_post(db: Session, data: PostCreate):
    post = Post(**data.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_posts(db: Session):
    return db.query(Post).order_by(Post.post_date.desc()).all()
