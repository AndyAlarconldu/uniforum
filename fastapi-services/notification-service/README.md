📣 Notification Service
This microservice handles the creation and management of user notifications, including message delivery and logging. It uses RabbitMQ for event-driven message processing and FastAPI for the REST API.
📁 Project Structure
notification-service/
└── app/
    ├── routes/
    │   └── notification.py       # API endpoints
    ├── consumer.py               # Message queue consumer (RabbitMQ)
    ├── crud.py                   # DB interaction functions
    ├── database.py               # SQLAlchemy setup
    ├── email_sender.py           # SMTP email sending logic
    ├── main.py                   # App initialization
    ├── models.py                 # SQLAlchemy models
    └── schemas.py                # Pydantic models
├── Dockerfile                   # Docker build config
├── requirements.txt             # Dependencies
└── start_consumer.py            # Entry point to start RabbitMQ consumer
🚀 Main Endpoints
Send Notification
POST /notifications/

Saves and sends a notification (via email too, using RabbitMQ).

Payload example:
{
  "recipient": "user@example.com",
  "subject": "Welcome",
  "message": "Thanks for joining!"
}

List Notifications
GET /notifications/

Returns a list of all stored notifications (ordered by timestamp).

🐳 How to Run with Docker
docker build -t notification-service .
docker run -p 8001:8001 notification-service

📦 Requirements
fastapi
uvicorn
sqlalchemy
psycopg2-binary
python-dotenv
pika
