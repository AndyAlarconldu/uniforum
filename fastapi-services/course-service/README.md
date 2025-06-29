📘 UniForum - Course Service
This microservice manages the course information available in the UniForum platform. It's built using Python and FastAPI.

🧱 Project Structure
course-service/
├── app/
│   ├── crud.py          # CRUD operations using SQLAlchemy
│   ├── database.py      # Database connection settings
│   ├── main.py          # FastAPI app entry point
│   ├── models.py        # Course model
│   ├── routes.py        # API routes for course handling
│   └── schemas.py       # Input/output schemas using Pydantic
├── Dockerfile           # Docker image for this microservice
└── requirements.txt     # Python dependencies

🔄 Main Features
Create a new course (POST /courses)

Get all courses (GET /courses)

Get courses by university (GET /courses/university/{university_id})

🐳 How to Run with Docker
docker build -t course-service .
docker run -p 8009:8009 course-service