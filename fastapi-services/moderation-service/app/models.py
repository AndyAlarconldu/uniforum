from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.sql import func
from app.database import Base

class ModerationReport(Base):
    __tablename__ = "moderation_report"

    id_report = Column(String, primary_key=True, index=True)
    content_type = Column(String, nullable=False)
    content_id = Column(String, nullable=False)
    reason = Column(Text, nullable=False)
    status = Column(String, default="PENDING")
    reported_by = Column(String, nullable=False)
    reviewed_by = Column(String, nullable=True)
    report_date = Column(DateTime(timezone=True), server_default=func.now())
    resolution_date = Column(DateTime(timezone=True), nullable=True)
