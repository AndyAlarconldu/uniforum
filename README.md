# UniForum Backend (Microservicios)

Este repositorio contiene los 15 microservicios distribuidos en:

- **Spring Boot (Java)**: 3 microservicios
- **FastAPI (Python)**: 11 microservicios
- **Node.js (Express)**: 1 microservicio

## Cómo iniciar todo con Docker

1. Asegúrate de tener Docker y Docker Compose instalados.
2. Coloca el código fuente de cada microservicio en su carpeta correspondiente.
3. Ejecuta el siguiente comando:

```bash
docker-compose up --build
```

## Servicios

- **Base de datos**: PostgreSQL (`5432`)
- **Microservicios**: Se exponen desde el puerto `8001` al `8011`, y `8081` a `8083`.

## Organización

```
uniforum-backend/
├── docker-compose.yml
├── README.md
├── springboot-services/
│   ├── registro-usuarios/
│   ├── auth-service/
│   └── authorization-service/
├── fastapi-services/
│   ├── perfil-service/
│   ├── ...
│   └── enrollment-service/
└── node-services/
    └── course-forum-link-service/
```
