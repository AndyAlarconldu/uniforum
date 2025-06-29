agging Service

This microservice is responsible for managing post tags in the UniForum platform. It allows the creation of new tags, their assignment to posts, and retrieval of tags by post. It uses a PostgreSQL database to store the relationships.

📁 Project Structure
tagging-service/
├── app/
│   ├── main.py          # FastAPI app and router setup
│   ├── crud.py          # Business logic for tags and assignments
│   ├── database.py      # PostgreSQL connection and base setup
│   ├── models.py        # SQLAlchemy models for Tag and PostTag
│   ├── routes.py        # Defines the /tags endpoints
│   ├── schemas.py       # Pydantic models for request and response
├── Dockerfile           # Container configuration
├── requirements.txt     # Python dependencies

📡 Endpoints
Method	Path	Description
POST	/tags/	Create a new tag
POST	/tags/assign	Assign an existing tag to a post
GET	/tags/post/{id}	Get tags assigned to a specific post
GET	/tags/	Get all tags