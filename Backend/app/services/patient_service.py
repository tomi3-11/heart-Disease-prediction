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


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.patient import PatientCreate, PatientResponse
from app.services.patient_service import (
    create_patient,
    get_patient,
    get_patients,
)

router = APIRouter(
    prefix="/patients",
    tags=["Patients"],
)


@router.post("/", response_model=PatientResponse)
def create(patient: PatientCreate, db: Session = Depends(get_db)):
    return create_patient(db, patient)


@router.get("/", response_model=list[PatientResponse])
def read_all(db: Session = Depends(get_db)):
    return get_patients(db)


@router.get("/{patient_id}", response_model=PatientResponse)
def read_one(patient_id: int, db: Session = Depends(get_db)):
    patient = get_patient(db, patient_id)

    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient



