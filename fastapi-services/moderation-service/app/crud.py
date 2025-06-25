from sqlalchemy.orm import Session
from app.models import ModerationReport
from app.schemas import ReportCreate, ReportResolve
from datetime import datetime

def create_report(db: Session, data: ReportCreate):
    report = ModerationReport(**data.dict())
    db.add(report)
    db.commit()
    db.refresh(report)
    return report

def get_all_reports(db: Session):
    return db.query(ModerationReport).all()

def get_pending_reports(db: Session):
    return db.query(ModerationReport).filter(ModerationReport.status == "PENDING").all()

def resolve_report(db: Session, report_id: str, data: ReportResolve):
    report = db.query(ModerationReport).filter_by(id_report=report_id).first()
    if report:
        report.status = data.status
        report.reviewed_by = data.reviewed_by
        report.resolution_date = datetime.utcnow()
        db.commit()
        db.refresh(report)
    return report
