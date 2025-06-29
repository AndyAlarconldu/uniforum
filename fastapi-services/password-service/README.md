- Password Service

This microservice is responsible for managing password recovery via email in the UniForum platform. It publishes password reset messages to a RabbitMQ queue, which are then consumed by the notification-service to send the actual email to the user.

📂 Project Structure
password-service/
├── app/
│   ├── main.py                # FastAPI app and router setup
│   ├── rabbitmq.py            # Publishes messages to the queue
│   ├── routes.py              # Defines the /recover endpoint
│   ├── schemas.py             # Pydantic model for request body
├── Dockerfile                 # Container configuration
├── requirements.txt           # Python dependencies

🔁 Endpoint
Method	Path	Description
POST	/recover	Sends a password recovery email via RabbitMQ

Request Example:
{
  "email": "user@example.com"
}
Response Example:
{
  "message": "Correo de recuperación enviado"
}
The message published includes:
{
  "recipient": "user@example.com",
  "subject": "Recuperación de contraseña - UniForum",
  "message": "Haz clic en el siguiente enlace para restablecer tu contraseña: https://uniform.edu/reset-password?email=user@example.com"
}

🐳 How to Run with Docker
docker build -t password-service .
docker run -p 8002:8002 password-service
