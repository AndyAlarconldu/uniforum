🧩 Microservice: Discussion Service
This microservice allows students to post discussion topics or messages within the UniForum system. It's built using Python and FastAPI.

📂 Project Structure
discussion-service/
│
├── app/
│   ├── crud.py         # Post creation and query logic
│   ├── database.py     # Database connection and settings
│   ├── main.py         # FastAPI application entry point
│   ├── models.py       # SQLAlchemy model for Post
│   ├── routes.py       # API routes and endpoints
│   └── schemas.py      # Pydantic models for validation
│
├── Dockerfile          # Container definition
├── requirements.txt    # Required Python packages

🚀 Main Endpoints
Create post (POST /discussions)

List posts (GET /discussions)

🐳 How to Run with Docker
Make sure you have Docker installed.

Navigate to the project folder.

Run:
docker build -t discussion-service .
docker run -p 8003:8003 discussion-service

🔧 Technologies Used
Python 3.11

FastAPI

SQLAlchemy

PostgreSQL

Docker