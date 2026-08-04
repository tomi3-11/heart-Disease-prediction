import pytest
from fastapi.testclient import TestClient

from app.db.base import Base
from app.db.dependencies import get_db
from app.main import app
from app.ml.explainer import load_explainer
from app.ml.model_loader import load_artifacts
from tests.database import TestingSessionLocal, engine


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

Base.metadata.create_all(bind=engine)

client = TestClient(app)


@pytest.fixture(autouse=True)
def clean_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    load_artifacts()
    load_explainer()
    yield


def get_auth_headers(role="doctor"):
    email = f"{role}@example.com"

    client.post(
        "/auth/register",
        json={
            "email": email,
            "password": "password123",
            "role": role,
        },
    )

    response = client.post(
        "/auth/login",
        json={
            "email": email,
            "password": "password123",
        },
    )

    token = response.json()["access_token"]

    return {"Authorization": f"Bearer {token}"}
