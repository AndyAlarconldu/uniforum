UniForum - Course Microservice
This microservice is part of the UniForum system and is built with FastAPI. It handles the management of university courses.

📁 Structure
crud.py: Functions to create and retrieve courses from the database.

database.py: Sets up the PostgreSQL connection using SQLAlchemy.

main.py: Entry point of the service. Initializes the app.

models.py: Defines the course table model.

routes.py: Defines endpoints for creating and fetching courses.

schemas.py: Pydantic schemas for input and output.

Dockerfile: Docker image for containerization.

requirements.txt: Python dependencies list.

How to run
docker-compose up --build

The service will be available on port 8009