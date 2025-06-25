from pydantic import BaseModel
from datetime import datetime

class PostCreate(BaseModel):
    id_post: str
    title: str
    content: str
    student_id: str

class PostOut(PostCreate):
    post_date: datetime

    model_config = {
        "from_attributes": True
    }
