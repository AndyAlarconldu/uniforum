from pydantic import BaseModel
from datetime import datetime

class CommentCreate(BaseModel):
    id_comment: str
    content: str
    post_id: str
    student_id: str

class CommentOut(CommentCreate):
    comment_date: datetime

    model_config = {
        "from_attributes": True
    }
