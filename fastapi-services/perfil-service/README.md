 Perfil Service
🇺🇸 English
This microservice is responsible for retrieving the authenticated student's profile in the UniForum platform. It verifies the user using a JWT token and fetches the student data along with their associated university information from the database.

Authentication is enforced using OAuth2 and JWT for secure access.
📂 Project Structure
perfil-service/
├── app/
│   ├── main.py         # FastAPI app initialization and router setup
│   ├── routes/
│   │   └── perfil.py    # Defines the /me endpoint for fetching user profile
│   ├── auth.py         # JWT authentication and user extraction
│   ├── crud.py         # Database access methods
│   ├── database.py     # PostgreSQL connection settings
│   ├── models.py       # SQLAlchemy models for Student and University
│   └── schemas.py      # Pydantic models for profile output
├── Dockerfile          # Container configuration
├── requirements.txt    # Python dependencies
🔁 Endpoint
Method	Path	Description
GET	/me	Returns the authenticated student's profile and university info

📥 Request Example
GET /perfil/me HTTP/1.1
Authorization: Bearer <your_jwt_token>


📤 Response Example
{
  "id_student": "stu001",
  "first_name": "Ana",
  "last_name": "Martínez",
  "email": "ana.martinez@uniforum.edu",
  "registration_date": "2023-09-01T12:00:00",
  "university": {
    "id_university": "uni001",
    "name": "Central University",
    "city": "Quito",
    "type": "Public"
  }
}
