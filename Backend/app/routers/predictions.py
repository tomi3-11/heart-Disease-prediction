from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.schemas.prediction import (
    PredictionRequest,
    PredictionResponse,
)

from app.services.prediction_service import make_prediction

router = APIRouter(
    prefix="/predictions",
    tags=["Predictions"],
)


@router.post("/", response_model=PredictionResponse)
def create_prediction(
    request: PredictionRequest,
    db: Session = Depends(get_db),
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
