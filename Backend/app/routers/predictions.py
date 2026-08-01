from fastapi import APIRouter

from app.schemas.prediction import (
    PredictionRequest,
    PredictionResponse,
)
from app.services.prediction_service import make_prediction

router = APIRouter(
    prefix="/predictions",
    tags=["Predictions"],
)


@router.post(
    "/",
    response_model=PredictionResponse,
)
def create_prediction(request: PredictionRequest):
    return make_prediction(request.model_dump())
