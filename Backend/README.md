# Heart Disease Prediction Backend

Backend API for the Heart Disease Prediction System.

The backend provides:

- User authentication using JWT
- Role-based access control
- Patient management
- Heart disease prediction using a trained Random Forest model
- Prediction history storage
- PostgreSQL database integration

---

# Technology Stack

- Python 3.13+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- scikit-learn
- Joblib
- Passlib (bcrypt)
- Python-JOSE
- Docker
- Docker Compose

---

# Project Structure

```
Backend/
├── app/
│   ├── core/
│   ├── db/
│   ├── ml/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── ml_artifacts/
│   ├── random_forest_model.joblib
│   ├── label_encoders.joblib
│   └── feature_order.joblib
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── API.md
└── ARCHITECTURE.md
```

---

# Features

## Authentication

- User registration
- User login
- JWT access tokens
- Password hashing
- Protected endpoints

---

## Authorization

Supported roles

- Admin
- Doctor
- Nurse

Role-based access is enforced on protected endpoints.

---

## Patient Management

- Create patient
- Retrieve patient
- List patients
- Update patient
- Delete patient

---

## Heart Disease Prediction

- Random Forest model
- Probability score
- Prediction history
- Input snapshot storage

---

## Database

- PostgreSQL
- SQLAlchemy ORM
- Persistent storage

---

# Machine Learning

The trained model is stored separately from the notebook.

```
ml_artifacts/
```

Contains

- Random Forest model
- Label encoders
- Feature order

The model is loaded once during application startup.

---

# Requirements

- Docker
- Docker Compose

or

- Python 3.13+
- PostgreSQL

---

# Installation

## Clone the repository

```bash
git clone <repository-url>
cd Backend
```

---

## Create a virtual environment

```bash
python -m venv .venv
```

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

Example

```env
DATABASE_URL=postgresql://postgres:password@db:5432/heart_db

SECRET_KEY=change_this_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

MODEL_PATH=ml_artifacts/random_forest_model.joblib

ENCODER_PATH=ml_artifacts/label_encoders.joblib

FEATURE_PATH=ml_artifacts/feature_order.joblib
```

---

# Running with Docker

Build containers

```bash
docker compose build
```

Start services

```bash
docker compose up
```

Detached mode

```bash
docker compose up -d
```

Stop services

```bash
docker compose down
```

View logs

```bash
docker compose logs -f
```

---

# Running Locally

Start PostgreSQL.

Run the application.

```bash
uvicorn app.main:app --reload
```

The API will be available at

```
http://localhost:8000
```

---

# Interactive Documentation

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# API Documentation

See

```
API.md
```

---

# Architecture Documentation

See

```
ARCHITECTURE.md
```

---

# API Overview

## Authentication

```
POST /auth/register

POST /auth/login
```

---

## Patients

```
GET    /patients/

GET    /patients/{id}

POST   /patients/

PUT    /patients/{id}

DELETE /patients/{id}
```

---

## Predictions

```
POST /predictions/

GET  /predictions/

GET  /predictions/{id}
```

---

# Authentication

Protected endpoints require a JWT.

Example

```
Authorization: Bearer <access_token>
```

---

# Development Workflow

1. Train the model in the notebook.
2. Export the model artifacts.
3. Copy the artifacts into `ml_artifacts/`.
4. Start the backend.
5. The model is loaded during application startup.
6. Predictions are served through the API.

---

# Testing

Run all tests.

```bash
pytest
```

Run a specific test.

```bash
pytest tests/test_predictions.py
```

---

# Future Enhancements

- SHAP explainability
- Dashboard analytics
- Report generation
- Pagination
- Search
- Filtering
- Refresh tokens
- Audit logging
- Model versioning
- Alembic migrations
- CI/CD pipeline

---

# License

Specify the project's license here.

---

# Contributors

project contributors to be added here.
