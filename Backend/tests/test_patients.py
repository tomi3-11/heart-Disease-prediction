from tests.conftest import client, get_auth_headers


def create_sample_patient(headers):
    response = client.post(
        "/patients/",
        headers=headers,
        json={
            "age": 50,
            "sex": "M",
            "chest_pain_type": "TA",
            "resting_bp": 120,
            "cholesterol": 200,
            "fasting_bs": 0,
            "resting_ecg": "Normal",
            "max_hr": 150,
            "exercise_angina": "N",
            "oldpeak": 0.0,
            "st_slope": "Flat",
        },
    )

    assert response.status_code == 200
    return response.json()


def test_create_patient():
    headers = get_auth_headers()

    patient = create_sample_patient(headers)

    assert patient["age"] == 50
    assert patient["sex"] == "M"
    assert patient["chest_pain_type"] == "TA"
    assert patient["resting_bp"] == 120


def test_get_all_patients():
    headers = get_auth_headers()

    create_sample_patient(headers)

    response = client.get("/patients/")

    assert response.status_code == 200

    patients = response.json()

    assert isinstance(patients, list)
    assert len(patients) >= 1


def test_get_single_patient():
    headers = get_auth_headers()

    patient = create_sample_patient(headers)

    response = client.get(f"/patients/{patient['id']}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == patient["id"]
    assert data["age"] == 50


def test_get_missing_patient():
    response = client.get("/patients/9999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Patient not found"


def test_update_patient():
    headers = get_auth_headers()

    patient = create_sample_patient(headers)

    response = client.put(
        f"/patients/{patient['id']}",
        headers=headers,
        json={
            "age": 60,
            "sex": "F",
            "chest_pain_type": "ASY",
            "resting_bp": 140,
            "cholesterol": 250,
            "fasting_bs": 1,
            "resting_ecg": "LVH",
            "max_hr": 130,
            "exercise_angina": "Y",
            "oldpeak": 2.0,
            "st_slope": "Down",
        },
    )

    assert response.status_code == 200

    updated = response.json()

    assert updated["age"] == 60
    assert updated["sex"] == "F"
    assert updated["st_slope"] == "Down"


def test_update_missing_patient():
    headers = get_auth_headers()

    response = client.put(
        "/patients/9999",
        headers=headers,
        json={
            "age": 60,
            "sex": "F",
            "chest_pain_type": "ASY",
            "resting_bp": 140,
            "cholesterol": 250,
            "fasting_bs": 1,
            "resting_ecg": "LVH",
            "max_hr": 130,
            "exercise_angina": "Y",
            "oldpeak": 2.0,
            "st_slope": "Down",
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Patient not found"


def test_delete_patient():
    headers = get_auth_headers("admin")

    patient = create_sample_patient(headers)

    response = client.delete(
        f"/patients/{patient['id']}",
        headers=headers,
    )

    assert response.status_code == 204


def test_delete_missing_patient():
    headers = get_auth_headers("admin")

    response = client.delete(
        "/patients/9999",
        headers=headers,
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Patient not found"


def test_delete_requires_admin():
    doctor_headers = get_auth_headers()

    patient = create_sample_patient(doctor_headers)

    response = client.delete(
        f"/patients/{patient['id']}",
        headers=doctor_headers,
    )

    assert response.status_code == 403
