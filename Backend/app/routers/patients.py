from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.patient import PatientCreate, PatientResponse
from app.services.patient_service import (
    create_patient,
    get_patient,
    get_patients,
    update_patient,
    delete_patient,
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

@router.put("/{patient_id}", response_model=PatientResponse)
def update(
    patient_id: int,
    patient: PatientCreate,
    db: Session = Depends(get_db),
):
    updated_patient = update_patient(db, patient_id, patient)

    if updated_patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found",
        )

    return updated_patient


@router.delete("/{patient_id}", status_code=204)
def delete(
    patient_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_patient(db, patient_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Patient not found",
        )
