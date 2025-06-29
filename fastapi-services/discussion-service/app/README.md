discussion-service - Discussion Service (FastAPI)
Description
This microservice allows students to create and list discussion posts within an academic context. It uses PostgreSQL as a database and FastAPI as the web framework.

🧱 Microservice Structure
crud.py: Logic to create and retrieve posts.

database.py: PostgreSQL connection via SQLAlchemy.

main.py: FastAPI entry point.

models.py: Data model definition for posts.

routes.py: HTTP endpoints for interaction.

schemas.py: Pydantic data validation schemas.

Dockerfile: Container configuration for deployment.

How to run with Docker
docker build -t discussion-service .
docker run -p 8003:8003 discussion-service