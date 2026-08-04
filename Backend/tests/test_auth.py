from .conftest import client


def test_register_user():
    response = client.post(
        "/auth/register",
        json={
            "email": "doctor@example.com",
            "password": "password123",
            "role": "doctor",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["email"] == "doctor@example.com"
    assert data["role"] == "doctor"
    assert "id" in data


def test_duplicate_email():
    client.post(
        "/auth/register",
        json={
            "email": "duplicate@example.com",
            "password": "password123",
            "role": "doctor",
        },
    )

    response = client.post(
        "/auth/register",
        json={
            "email": "duplicate@example.com",
            "password": "password123",
            "role": "doctor",
        },
    )

    assert response.status_code in [400, 409]


def test_login_success():
    client.post(
        "/auth/register",
        json={
            "email": "login@example.com",
            "password": "password123",
            "role": "doctor",
        },
    )

    response = client.post(
        "/auth/login",
        json={
            "email": "login@example.com",
            "password": "password123",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_password():
    client.post(
        "/auth/register",
        json={
            "email": "wrongpass@example.com",
            "password": "password123",
            "role": "doctor",
        },
    )

    response = client.post(
        "/auth/login",
        json={
            "email": "wrongpass@example.com",
            "password": "wrongpassword",
        },
    )

    assert response.status_code == 401
