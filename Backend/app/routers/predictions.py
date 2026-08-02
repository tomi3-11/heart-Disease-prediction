from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User

from app.db.dependencies import get_db
from app.services.auth_service import get_current_user

from app.schemas.prediction import (
    PredictionRequest,
    PredictionResponse,
)

from app.services.prediction_service import (
    make_prediction,
    get_predictions,
    get_patient_predictions,
)

router = APIRouter(
    prefix="/predictions",
    tags=["Predictions"],
)


@router.post("/", response_model=PredictionResponse)
def create_prediction(
    request: PredictionRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    prediction = make_prediction(
        db,
        request.patient_id,
    )

    if prediction is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found",
        )

    return prediction


@router.get("/", response_model=list[PredictionResponse])
def read_predictions(
    db: Session = Depends(get_db),
):
    return get_predictions(db)


@router.get("/patient/{patient_id}", response_model=list[PredictionResponse])
def read_patient_predictions(
    patient_id: int,
    db: Session = Depends(get_db),
):
    return get_patient_predictions(db, patient_id)
