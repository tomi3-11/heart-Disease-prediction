from pydantic import BaseModel
from datetime import datetime


class PredictionRequest(BaseModel):
    patient_id: int


class PredictionResponse(BaseModel):
    id: int
    patient_id: int
    prediction: int
    probability: float
    input_snapshot: dict
    created_at: datetime
    shap_values: list[float]

    model_config = {
        "from_attributes": True
    }
