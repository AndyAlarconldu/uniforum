from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Post(Base):
    __tablename__ = "post"

    id_post = Column(String, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    post_date = Column(DateTime, server_default=func.now())
    student_id = Column(String, nullable=False)
