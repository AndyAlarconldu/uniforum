from sqlalchemy.orm import Session
from app.models import Comment
from app.schemas import CommentCreate

def create_comment(db: Session, data: CommentCreate):
    comment = Comment(**data.dict())
    db.add(comment)
    db.commit()
    print(f"✅ Comentario creado: ID={comment.id_comment}, Post={comment.post_id}")

    db.refresh(comment)
    return comment

def get_comments_by_post(db: Session, post_id: str):
    return db.query(Comment).filter(Comment.post_id == post_id).order_by(Comment.comment_date.desc()).all()
