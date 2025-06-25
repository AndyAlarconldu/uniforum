from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Comment(Base):
    __tablename__ = "comment"

    id_comment = Column(String, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    comment_date = Column(DateTime(timezone=True), server_default=func.now())
    post_id = Column(String, nullable=False)
    student_id = Column(String, nullable=False)
