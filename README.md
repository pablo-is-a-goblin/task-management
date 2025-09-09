# Task Management System
A containerized full-stack task management platform using Django, PostgreSQL and Celery

## Quick Start
```bash
git clone "https://github.com/pablo-is-a-goblin/task-management-system.git"
cd task-management-system
cp .env.sample .env
docker compose up
```
Then go to your browser and enter `http://localhost:8080` (or another port if you changed the `ENTRY_PORT` variable)
## Documentation
- [Architecture](docs/ARCHITECTURE.md)
- [API](docs/API_DOCUMENTATION.md)
- [Decisions](docs/DECISIONS.md)

## `.env` variables
- `POSTGRES_USER`: user for connecting to the PostgreSQL database
- `POSTGRES_PASSWORD`: password for connecting to the PostgreSQL database
- `POSTGRES_DB`: name of the PostgreSQL database
- `POSTGRES_PORT` : port for connecting to PostgreSQL
- `REDIS_PORT` : port for connecting to Redis
- `BACKEND_PORT` & `ENTRY_PORT` : this pair is the port mapping to connect to the system. `BACKEND_PORT` is the port inside the container in which Django is listening and `ENTRY_PORT` is the Host Machine port that is mapped to `BACKEND_PORT`
- `EMAIL_BACKEND` : set to `'django.core.mail.backends.console.EmailBackend'` if you just want to test without sending real emails. If you want to send real emails, you have to set this variable to `'django.core.mail.backends.smtp.EmailBackend'`, as well as setting the next 2 variables
- `EMAIL_HOST_USER` : the email from where you want to send the email
- `EMAIL_HOST_PASSWORD` : the App Password of `EMAIL_HOST_PASSWORD`
