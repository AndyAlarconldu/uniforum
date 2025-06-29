 Voting Service

This microservice manages voting on discussion posts. Students can upvote or downvote posts. Each student can vote only once per post. It also provides vote scoring and retrieval by student.

📁 Project Structure
voting-service/
├── app/
│   ├── crud.py         # Logic for creating and querying votes
│   ├── database.py     # PostgreSQL database setup
│   ├── main.py         # FastAPI app and route registration
│   ├── models.py       # SQLAlchemy model (PostVote)
│   ├── routes.py       # Defines the /votes endpoints
│   └── schemas.py      # Pydantic input/output models
├── Dockerfile
└── requirements.txt

🔗 Endpoints
Method	Path	Description
POST	/votes/	Registers a new vote (up/down)
GET	/votes/post/{post_id}	Returns the score (upvotes-downvotes)
GET	/votes/student/{student_id}	Retrieves votes made by a student

📝 Request Example (POST /votes/)
{
  "id_vote": "v001",
  "student_id": "stu456",
  "post_id": "post123",
  "vote_type": "upvote"
}
