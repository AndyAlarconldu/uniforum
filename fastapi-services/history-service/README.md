History Service
This microservice is part of the UniForum platform and is responsible for storing and retrieving the edit history of student posts.

🧱 Project Structure

history-service/
├── app/
│   ├── crud.py          # Logic for creating and retrieving history entries
│   ├── database.py      # PostgreSQL database connection
│   ├── main.py          # FastAPI initialization and route inclusion
│   ├── models.py        # SQLAlchemy model definition (PostHistory)
│   ├── routes.py        # HTTP endpoints
│   └── schemas.py       # Pydantic schemas (input/output)
├── Dockerfile           # Docker container definition
├── requirements.txt     # Project dependencies

🗃️ Data Model
The PostHistory model represents an edit made to a post:
class PostHistory(Base):
    __tablename__ = "post_history"
    id_history: str
    post_id: str
    title: str
    content: str
    edited_by: str
    edited_at: datetime (default: now)

🔁 Available Endpoints
Create a post edit history
POST /history/

Request Body:
{
  "id_history": "uuid",
  "post_id": "string",
  "title": "string",
  "content": "string",
  "edited_by": "string"
}

Get post history by post ID
GET /history/post/{post_id}

Response:
[
  {
    "id_history": "uuid",
    "post_id": "string",
    "title": "string",
    "content": "string",
    "edited_by": "string",
    "edited_at": "2025-06-27T15:34:00"
  }
]


🐳 How to Run with Docker
docker build -t history-service .
docker run -p 8008:8008 history-service

📦 Requirements
fastapi
uvicorn
sqlalchemy
psycopg2-binary
python-dotenv

