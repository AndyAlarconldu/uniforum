Enrollment Service
This microservice handles student enrollments in available courses. It's developed in Python using the FastAPI framework.
🧱 Project structure

enrollment-service/
├── app/
│   ├── crud.py          # Logic to create and query enrollments
│   ├── database.py      # Database connection
│   ├── main.py          # Main entry point
│   ├── models.py        # SQLAlchemy model for "enrollment" table
│   ├── routes.py        # API endpoints
│   └── schemas.py       # Input/output validation with Pydantic
├── Dockerfile           # Docker image for this service
└── requirements.txt     # Python dependencies

🔄 Main features
Create new enrollment (POST /enrollments)

Get all enrollments (GET /enrollments)

Get enrollments by student (GET /enrollments/student/{student_id})

🐳 How to run with Docker
docker build -t enrollment-service .
docker run -p 8010:8010 enrollment-service
