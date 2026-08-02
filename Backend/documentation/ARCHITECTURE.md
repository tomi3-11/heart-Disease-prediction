# Backend Architecture

## Overview

The backend follows a layered architecture that separates responsibilities into independent modules. Each layer has a single responsibility and communicates only with adjacent layers.

```
                Client
                   │
                   ▼
             FastAPI Router
                   │
                   ▼
              Service Layer
          ┌────────┴────────┐
          ▼                 ▼
     Machine Learning    Database
          │                 │
          ▼                 ▼
   Prediction Result   SQLAlchemy ORM
          │                 │
          └────────┬────────┘
                   ▼
              JSON Response
```

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
│
├── tests/
│
├── Dockerfile
├── requirements.txt
└── docker-compose.yml
```

---

# Directory Responsibilities

## app/main.py

Application entry point.

Responsibilities

- Create FastAPI application
- Register routers
- Load ML artifacts during startup
- Configure middleware
- Configure application lifespan

---

## app/core/

Application configuration and security.

```
core/
├── config.py
├── dependencies.py
├── permissions.py
└── security.py
```

### config.py

Stores application configuration.

Examples

- Database URL
- JWT Secret Key
- JWT Expiration
- Model paths
- Encoder paths

---

### security.py

Handles authentication.

Responsibilities

- Password hashing
- Password verification
- JWT creation
- JWT validation

---

### dependencies.py

Contains reusable FastAPI dependencies.

Examples

- OAuth2PasswordBearer

---

### permissions.py

Role-based authorization.

Responsibilities

- Verify user roles
- Restrict endpoint access

---

# app/db/

Database configuration.

```
db/
├── base.py
├── dependencies.py
└── session.py
```

---

## session.py

Creates the SQLAlchemy engine and session factory.

Responsible for

- Database connection
- Session management

---

## base.py

Contains the SQLAlchemy Base class.

All ORM models inherit from this class.

---

## dependencies.py

Provides reusable database sessions.

Example

```python
db: Session = Depends(get_db)
```

---

# app/models/

Database tables.

```
models/
├── patient.py
├── prediction.py
└── user.py
```

Each file defines one database table.

---

## User

Stores user accounts.

Fields

- id
- email
- hashed_password
- role

---

## Patient

Stores patient information.

Fields

- id
- age
- sex
- chest_pain_type
- resting_bp
- cholesterol
- fasting_bs
- resting_ecg
- max_hr
- exercise_angina
- oldpeak
- st_slope

---

## Prediction

Stores prediction history.

Fields

- id
- patient_id
- prediction
- probability
- input_snapshot
- created_at

---

# app/schemas/

Pydantic models.

```
schemas/
├── auth.py
├── patient.py
└── prediction.py
```

Responsibilities

- Request validation
- Response serialization

Schemas are independent from database models.

---

# app/routers/

HTTP endpoints.

```
routers/
├── auth.py
├── patients.py
└── predictions.py
```

Responsibilities

- Receive HTTP requests
- Validate input
- Call services
- Return JSON responses

Routers do not contain business logic.

---

# app/services/

Business logic.

```
services/
├── auth_service.py
├── patient_service.py
└── prediction_service.py
```

Responsibilities

- Coordinate database operations
- Call ML components
- Process application logic

Services isolate business rules from HTTP routes.

---

# app/ml/

Machine learning components.

```
ml/
├── explainer.py
├── model_loader.py
├── predictor.py
└── preprocessing.py
```

This layer has no knowledge of HTTP or databases.

---

## model_loader.py

Loads ML artifacts.

Artifacts

- Random Forest model
- Label encoders
- Feature order

Artifacts are loaded once during application startup.

---

## preprocessing.py

Transforms raw patient data into the format expected by the model.

Responsibilities

- Encode categorical variables
- Arrange feature order
- Produce model-ready input

---

## predictor.py

Runs model inference.

Responsibilities

- Predict heart disease
- Calculate prediction probability

---

## explainer.py

Responsible for model explainability.

Planned functionality

- SHAP values
- Feature importance
- Prediction explanations

---

# ML Artifacts

```
ml_artifacts/
├── feature_order.joblib
├── label_encoders.joblib
└── random_forest_model.joblib
```

These artifacts are generated during model training and loaded during application startup.

---

# Request Flow

## Create Patient

```
Client
    │
    ▼
POST /patients
    │
    ▼
Patient Router
    │
    ▼
Patient Service
    │
    ▼
SQLAlchemy
    │
    ▼
PostgreSQL
    │
    ▼
Response
```

---

## Prediction

```
Client
    │
    ▼
POST /predictions
    │
    ▼
Prediction Router
    │
    ▼
Prediction Service
    │
    ├───────────────┐
    ▼               ▼
Database      ML Preprocessing
                      │
                      ▼
                Random Forest
                      │
                      ▼
               Prediction Result
                      │
                      ▼
              Save Prediction
                      │
                      ▼
                 JSON Response
```

---

# Authentication Flow

```
User
 │
 ▼
POST /auth/login
 │
 ▼
Verify Password
 │
 ▼
Generate JWT
 │
 ▼
Return Access Token
 │
 ▼
Client Stores Token
 │
 ▼
Authorization Header
 │
 ▼
Protected Endpoint
 │
 ▼
JWT Validation
 │
 ▼
Access Granted
```

---

# Authorization Flow

```
Incoming Request
        │
        ▼
JWT Validation
        │
        ▼
Current User
        │
        ▼
Role Verification
        │
        ├─────────────┐
        ▼             ▼
Authorized      Permission Denied
```

---

# Layer Communication

Allowed

```
Router
    ↓
Service
    ↓
ML

Router
    ↓
Service
    ↓
Database
```

Not Allowed

```
Router → Database

Router → ML

ML → Database

ML → Router

Database → Router
```

All communication passes through the service layer.

---

# Design Principles

- Separation of concerns
- Single responsibility
- Layered architecture
- Dependency injection
- Stateless API
- JWT-based authentication
- Role-based authorization
- Reusable business logic
- Modular machine learning components

---

# Current Features

- JWT authentication
- Password hashing
- Role-based authorization
- Patient CRUD
- Prediction endpoint
- Prediction history
- PostgreSQL persistence
- SQLAlchemy ORM
- Docker deployment

---

# Planned Features

- SHAP explainability
- Dashboard analytics
- Reporting
- Model versioning
- Refresh tokens
- Audit logging
- Pagination
- Search
- Filtering
- API versioning
- Alembic database migrations
- Automated testing
- CI/CD pipeline
