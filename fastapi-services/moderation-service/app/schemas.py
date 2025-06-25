from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ReportCreate(BaseModel):
    id_report: str
    content_type: str
    content_id: str
    reason: str
    reported_by: str

class ReportResolve(BaseModel):
    status: str
    reviewed_by: str

class ReportOut(ReportCreate):
    status: str
    reviewed_by: Optional[str]
    report_date: datetime
    resolution_date: Optional[datetime]

    model_config = {
        "from_attributes": True
    }
