Reply Service

This microservice is responsible for handling user comments (replies) to posts within the UniForum platform. It allows creating new replies and retrieving all replies associated with a specific post. Replies are stored in a PostgreSQL database using SQLAlchemy.

📁 Project Structure
reply-service/
├── app/
│   ├── main.py           # FastAPI app and router setup
│   ├── crud.py           # Functions to create and fetch comments
│   ├── database.py       # PostgreSQL connection via SQLAlchemy
│   ├── models.py         # SQLAlchemy models for Comment
│   ├── routes.py         # Defines endpoints for comment operations
│   └── schemas.py        # Pydantic models for request/response
├── Dockerfile            # Container configuration
└── requirements.txt      # Python dependencies

📌 Endpoints
Method	Path	Description
POST	/replies/	Creates a new reply
GET	/replies/post/{id}	Gets all replies for a given post ID

🔄 Request Example
POST /replies/
{
  "id_comment": "abc123",
  "content": "This is a comment.",
  "post_id": "post001",
  "student_id": "user001"
}

✅ Response Example
GET /replies/post/post001
[
  {
    "id_comment": "abc123",
    "content": "This is a comment.",
    "post_id": "post001",
    "student_id": "user001",
    "comment_date": "2025-06-29T10:20:30"
  }
]

