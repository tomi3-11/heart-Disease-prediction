from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.patient import Patient
from app.models.prediction import Prediction

from app.ml.preprocessing import preprocess
from app.ml.predictor import predict


def make_prediction(db: Session, patient_id: int):
    patient = db.get(Patient, patient_id)

    if patient is None:
        return None

    patient_data = {
        "Age": patient.age,
        "Sex": patient.sex,
        "ChestPainType": patient.chest_pain_type,
        "RestingBP": patient.resting_bp,
        "Cholesterol": patient.cholesterol,
        "FastingBS": patient.fasting_bs,
        "RestingECG": patient.resting_ecg,
        "MaxHR": patient.max_hr,
        "ExerciseAngina": patient.exercise_angina,
        "Oldpeak": patient.oldpeak,
        "ST_Slope": patient.st_slope,
    }

    features = preprocess(patient_data)

    result = predict(features)

    db_prediction = Prediction(
        patient_id=patient.id,
        prediction=result["prediction"],
        probability=result["probability"],
        input_snapshot=patient_data,
    )

    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)

    return db_prediction


def get_predictions(db: Session):
    statement = select(Prediction).order_by(Prediction.created_at.desc())
    return db.scalars(statement).all()


def get_patient_predictions(db: Session, patient_id: int):
    statement = (
        select(Prediction)
        .where(Prediction.patient_id == patient_id)
        .order_by(Prediction.created_at.desc())
    )

    return db.scalars(statement).all()
