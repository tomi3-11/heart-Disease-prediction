# Heart Disease Prediction Backend API

## Overview

This document describes the backend API for the Heart Disease Prediction System.

### Technology Stack

- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic
- JWT Authentication
- scikit-learn
- Docker

---

# Base URL

Development

```
http://localhost:8000
```

---

# Authentication

Authentication uses JWT Bearer Tokens.

## Register

**POST**

```
/auth/register
```

### Request

```json
{
    "email": "doctor@example.com",
    "password": "password123",
    "role": "doctor"
}
```

### Response

```json
{
    "id": 1,
    "email": "doctor@example.com",
    "role": "doctor"
}
```

---

## Login

**POST**

```
/auth/login
```

### Request

```json
{
    "email": "doctor@example.com",
    "password": "password123"
}
```

### Response

```json
{
    "access_token": "<jwt_token>",
    "token_type": "bearer"
}
```

---

# Authorization

All protected endpoints require the following header.

```
Authorization: Bearer <jwt_token>
```

Example

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

---

# User Roles

Available roles

- admin
- doctor
- nurse

---

# Patients

---

## Create Patient

**POST**

```
/patients/
```

Authentication Required

### Request

```json
{
    "age": 40,
    "sex": "M",
    "chest_pain_type": "ATA",
    "resting_bp": 120,
    "cholesterol": 250,
    "fasting_bs": 0,
    "resting_ecg": "Normal",
    "max_hr": 170,
    "exercise_angina": "N",
    "oldpeak": 0,
    "st_slope": "Up"
}
```

### Response

```json
{
    "id": 1,
    "age": 40,
    "sex": "M",
    "chest_pain_type": "ATA",
    "resting_bp": 120,
    "cholesterol": 250,
    "fasting_bs": 0,
    "resting_ecg": "Normal",
    "max_hr": 170,
    "exercise_angina": "N",
    "oldpeak": 0,
    "st_slope": "Up"
}
```

---

## List Patients

**GET**

```
/patients/
```

Authentication Required

### Response

```json
[
    {
        "id": 1,
        "age": 40,
        "sex": "M",
        "chest_pain_type": "ATA",
        "resting_bp": 120,
        "cholesterol": 250,
        "fasting_bs": 0,
        "resting_ecg": "Normal",
        "max_hr": 170,
        "exercise_angina": "N",
        "oldpeak": 0,
        "st_slope": "Up"
    }
]
```

---

## Get Patient

**GET**

```
/patients/{patient_id}
```

Authentication Required

### Response

```json
{
    "id": 1,
    "age": 40,
    "sex": "M",
    "chest_pain_type": "ATA",
    "resting_bp": 120,
    "cholesterol": 250,
    "fasting_bs": 0,
    "resting_ecg": "Normal",
    "max_hr": 170,
    "exercise_angina": "N",
    "oldpeak": 0,
    "st_slope": "Up"
}
```

---

## Update Patient

**PUT**

```
/patients/{patient_id}
```

Authentication Required

### Request

```json
{
    "age": 45,
    "sex": "M",
    "chest_pain_type": "ASY",
    "resting_bp": 130,
    "cholesterol": 260,
    "fasting_bs": 0,
    "resting_ecg": "Normal",
    "max_hr": 165,
    "exercise_angina": "N",
    "oldpeak": 0.5,
    "st_slope": "Flat"
}
```

### Response

```json
{
    "id": 1,
    "age": 45,
    "sex": "M",
    "chest_pain_type": "ASY",
    "resting_bp": 130,
    "cholesterol": 260,
    "fasting_bs": 0,
    "resting_ecg": "Normal",
    "max_hr": 165,
    "exercise_angina": "N",
    "oldpeak": 0.5,
    "st_slope": "Flat"
}
```

---

## Delete Patient

**DELETE**

```
/patients/{patient_id}
```

Admin Only

### Response

```
204 No Content
```

---

# Predictions

---

## Create Prediction

**POST**

```
/predictions/
```

Authentication Required

### Request

```json
{
    "patient_id": 1
}
```

### Response

```json
{
    "id": 1,
    "patient_id": 1,
    "prediction": 0,
    "probability": 0.995,
    "input_snapshot": {
        "age": 40,
        "sex": "M",
        "chest_pain_type": "ATA",
        "resting_bp": 120,
        "cholesterol": 250,
        "fasting_bs": 0,
        "resting_ecg": "Normal",
        "max_hr": 170,
        "exercise_angina": "N",
        "oldpeak": 0,
        "st_slope": "Up"
    },
    "created_at": "2026-08-02T13:45:00"
}
```

---

## List Predictions

**GET**

```
/predictions/
```

Authentication Required

### Response

```json
[
    {
        "id": 1,
        "patient_id": 1,
        "prediction": 0,
        "probability": 0.995,
        "created_at": "2026-08-02T13:45:00"
    }
]
```

---

## Get Prediction

**GET**

```
/predictions/{prediction_id}
```

Authentication Required

### Response

```json
{
    "id": 1,
    "patient_id": 1,
    "prediction": 0,
    "probability": 0.995,
    "input_snapshot": {},
    "created_at": "2026-08-02T13:45:00"
}
```

---

# HTTP Status Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 201 | Resource Created |
| 204 | Resource Deleted |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Resource Not Found |
| 422 | Validation Error |
| 500 | Internal Server Error |

---

# Role Permissions

| Endpoint | Public | Doctor | Nurse | Admin |
|----------|:------:|:------:|:-----:|:-----:|
| POST /auth/register | ✓ | ✓ | ✓ | ✓ |
| POST /auth/login | ✓ | ✓ | ✓ | ✓ |
| POST /patients | ✗ | ✓ | ✗ | ✓ |
| GET /patients | ✗ | ✓ | ✓ | ✓ |
| GET /patients/{id} | ✗ | ✓ | ✓ | ✓ |
| PUT /patients/{id} | ✗ | ✓ | ✗ | ✓ |
| DELETE /patients/{id} | ✗ | ✗ | ✗ | ✓ |
| POST /predictions | ✗ | ✓ | ✗ | ✓ |
| GET /predictions | ✗ | ✓ | ✓ | ✓ |
| GET /predictions/{id} | ✗ | ✓ | ✓ | ✓ |

---

# Error Response Format

```json
{
    "detail": "Error message"
}
```

Examples

```json
{
    "detail": "Not authenticated"
}
```

```json
{
    "detail": "Invalid token"
}
```

```json
{
    "detail": "Permission denied"
}
```

```json
{
    "detail": "Patient not found"
}
```

---

# Frontend Authentication Flow

1. Register a user.
2. Login using email and password.
3. Store the returned JWT.
4. Include the JWT in every protected request.

```
Authorization: Bearer <jwt_token>
```

5. Redirect the user to the login page if a `401 Unauthorized` response is received.

---

# Upcoming Features

The following features are planned and are **not yet available**:

- SHAP explainability
- Dashboard analytics
- Report generation
- Model versioning
- Refresh tokens
- Pagination
- Filtering
- Search endpoints
