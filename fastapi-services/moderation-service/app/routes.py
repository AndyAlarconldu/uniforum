from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import ReportCreate, ReportResolve, ReportOut
from app.crud import create_report, get_all_reports, get_pending_reports, resolve_report

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ReportOut)
def create(data: ReportCreate, db: Session = Depends(get_db)):
    return create_report(db, data)

@router.get("/", response_model=list[ReportOut])
def all_reports(db: Session = Depends(get_db)):
    return get_all_reports(db)

@router.get("/pending", response_model=list[ReportOut])
def pending_reports(db: Session = Depends(get_db)):
    return get_pending_reports(db)

@router.put("/{report_id}/resolve", response_model=ReportOut)
def resolve(report_id: str, data: ReportResolve, db: Session = Depends(get_db)):
    result = resolve_report(db, report_id, data)
    if not result:
        raise HTTPException(status_code=404, detail="Report not found")
    return result
