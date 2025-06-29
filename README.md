## UniForum Backend (Microservices)

This repository contains 15 microservices distributed as follows:
•	Spring Boot (Java): 3 microservices
•	FastAPI (Python): 11 microservices
•	Node.js (Express): 1 microservice

How to start everything with Docker
1.	Make sure you have Docker and Docker Compose installed.
2.	Place the source code for each microservice in its corresponding folder.
3.	Run the following command:

    docker-compose up --build


## Services 

•Database: PostgreSQL (5432)
•Microservices: Exposed from port 8001 to 8011, and from 8081 to 8083.


## Organization


UNIFORUM
├── fastapi-services
│   ├── course-service
│   ├── discussion-service
│   ├── enrollment-service
│   ├── history-service
│   ├── moderation-service
│   ├── notification-service
│   ├── password-service
│   ├── perfil-service
│   ├── reply-service
│   ├── tagging-service
│   └── voting-service
├── init
│   └── init.sql
├── node-services
│   └── course-forum-link-service
│       ├── config
│       ├── controllers
│       ├── models
│       ├── routes
│       ├── Dockerfile
│       ├── index.js
│       ├── package-lock.json
│       └── package.json
├── springboot-services
│   ├── auth-service-final
│   ├── authorization-service
│   └── registro-usuarios-correcto
├── .gitignore
├── docker-compose.yml
├── README.md
└── UniForum.docx
