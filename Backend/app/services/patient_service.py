from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.patient import Patient
from app.schemas.patient import PatientCreate


def create_patient(db: Session, patient: PatientCreate):
    db_patient = Patient(**patient.model_dump())

    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)

    return db_patient

def get_patients(db: Session):
    statement = select(Patient)
    return db.scalars(statement).all()


def get_patient(db: Session, patient_id: int):
    statement = select(Patient).where(Patient.id == patient_id)
    return db.scalar(statement)


def update_patient(db: Session, patient_id: int, patient_data: PatientCreate):
    patient = get_patient(db, patient_id)

    if patient is None:
        return None

    for key, value in patient_data.model_dump().items():
        setattr(patient, key, value)

    db.commit()
    db.refresh(patient)

    return patient


def delete_patient(db: Session, patient_id: int):
    patient = get_patient(db, patient_id)

    if patient is None:
        return False

    db.delete(patient)
    db.commit()

    return True
