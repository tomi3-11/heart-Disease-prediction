from tests.conftest import client, get_auth_headers


def create_sample_patient(headers):
    response = client.post(
        "/patients/",
        json={
            "age": 50,
            "sex": "M",
            "chest_pain_type": "ATA",
            "resting_bp": 120,
            "cholesterol": 240,
            "fasting_bs": 0,
            "resting_ecg": "Normal",
            "max_hr": 170,
            "exercise_angina": "N",
            "oldpeak": 0.0,
            "st_slope": "Up",
        },
        headers=headers,
    )

    assert response.status_code == 200
    return response.json()


def test_create_prediction():
    headers = get_auth_headers()

    patient = create_sample_patient(headers)

    response = client.post(
        "/predictions/",
        json={
            "patient_id": patient["id"],
        },
        headers=headers,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["patient_id"] == patient["id"]
    assert data["prediction"] in [0, 1]
    assert 0 <= data["probability"] <= 1
    assert "created_at" in data
    assert "input_snapshot" in data
    assert "shap_values" in data


def test_prediction_missing_patient():
    headers = get_auth_headers()

    response = client.post(
        "/predictions/",
        json={
            "patient_id": 9999,
        },
        headers=headers,
    )

    assert response.status_code == 404


def test_prediction_requires_auth():
    response = client.post(
        "/predictions/",
        json={
            "patient_id": 1,
        },
    )

    assert response.status_code == 401


def test_prediction_history():
    headers = get_auth_headers()

    patient = create_sample_patient(headers)

    prediction_response = client.post(
        "/predictions/",
        json={
            "patient_id": patient["id"],
        },
        headers=headers,
    )

    assert prediction_response.status_code == 200

    response = client.get(
        "/predictions/",
        headers=headers,
    )

    assert response.status_code == 200

    history = response.json()

    assert isinstance(history, list)
    assert len(history) == 1

    prediction = history[0]

    assert prediction["patient_id"] == patient["id"]
    assert prediction["prediction"] in [0, 1]
    assert 0 <= prediction["probability"] <= 1
    assert "created_at" in prediction
    assert "input_snapshot" in prediction
    assert "shap_values" in prediction


def test_prediction_history_empty():
    headers = get_auth_headers()

    response = client.get(
        "/predictions/",
        headers=headers,
    )

    assert response.status_code == 200
    assert response.json() == []
