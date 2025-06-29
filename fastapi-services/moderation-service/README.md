Moderation Service
This microservice handles the creation, retrieval, and resolution of content moderation reports within the UniForum platform.

📦 Endpoints
✅ Create a report (POST /reports/)
Registers a new moderation report for inappropriate or suspicious content.

Request body (ReportCreate):
{
  "id_report": "uuid",
  "content_type": "post",
  "content_id": "post-123",
  "reason": "Inappropriate language",
  "reported_by": "user-789"
}
Response (ReportOut):
{
  "id_report": "uuid",
  "content_type": "post",
  "content_id": "post-123",
  "reason": "Inappropriate language",
  "reported_by": "user-789",
  "status": "PENDING",
  "reviewed_by": null,
  "report_date": "2025-06-28T15:30:00",
  "resolution_date": null
}
📄 Get all reports (GET /reports/)
Returns a list of all reports.
⏳ Get only pending reports (GET /reports/pending)
Filters and returns only the reports with "status": "PENDING".
✔️ Resolve a report (PUT /reports/{report_id}/resolve)
Allows a moderator to resolve a report by changing its status and attaching resolution details.

Request body (ReportResolve):
{
  "status": "RESOLVED",
  "reviewed_by": "moderator-1"
}
If report is found, it updates the status and adds a resolution_date.


🛠️ Technologies Used
FastAPI - RESTful API framework.

SQLAlchemy - ORM for database modeling.

PostgreSQL - Relational database.

Docker - Containerization.

Pydantic - Data validation.