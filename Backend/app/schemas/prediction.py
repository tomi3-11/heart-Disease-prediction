from pydantic import BaseModel


class PredictionRequest(BaseModel):
    patient_id: int


class PredictionResponse(BaseModel):
    id: int
    patient_id: int
    prediction: int
    probability: float

    model_config = {
        "from_attributes": True
    }
