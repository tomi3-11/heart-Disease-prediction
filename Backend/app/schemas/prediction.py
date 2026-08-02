from typing import Literal

from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    Age: int = Field(..., ge=1, le=120)
    Sex: Literal["M", "F"]
    ChestPainType: Literal["ASY", "ATA", "NAP", "TA"]
    RestingBP: int = Field(..., ge=0)
    Cholesterol: int = Field(..., ge=0)
    FastingBS: Literal[0, 1]
    RestingECG: Literal["LVH", "Normal", "ST"]
    MaxHR: int = Field(..., ge=60, le=250)
    ExerciseAngina: Literal["N", "Y"]
    Oldpeak: float = Field(..., ge=0.0)
    ST_Slope: Literal["Down", "Flat", "Up"]


class PredictionResponse(BaseModel):
    prediction: int
    probability: float
