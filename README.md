# training-certification-management-system
FastAPI Training &amp; Certification Management System with JWT Authentication, Training Management, Employee Enrollment, Certification Management, Reports, Search, SQLAlchemy ORM, Pagination, Logging, Docker Support, and Unit Tests.
# Training & Certification Management System

## Features

- JWT Authentication
- Training Management (CRUD)
- Employee Enrollment
- Certification Management
- Reports & Search
- SQLAlchemy ORM
- SQLite Database
- Docker Support
- Logging
- Basic Unit Tests



## Setup Instructions

### Install Dependencies


pip install -r requirements.txt


### Run Project


py -m uvicorn main:app --reload


Swagger


http://127.0.0.1:8000/docs


## Environment Variables


SECRET_KEY=training_secret_key
ALGORITHM=HS256


## API Examples

- POST `/auth/register`
- POST `/auth/login`
- POST `/trainings`
- POST `/enrollments`
- POST `/certificates`



## Docker Deployment

docker build -t training-system .
docker run -p 8000:8000 training-system


## Assumptions

- Employee cannot enroll twice in the same training.
- Completed enrollments cannot be modified.
- Training end date must be after start date.
- Certificate expiry date must be after issued date.
