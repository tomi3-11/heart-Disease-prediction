from typing import Literal

from pydantic import BaseModel, Field


class PatientCreate(BaseModel):
    age: int = Field(..., ge=1, le=120)
    sex: Literal["M", "F"]
    chest_pain_type: Literal["ASY", "ATA", "NAP", "TA"]
    resting_bp: int = Field(..., ge=0)
    cholesterol: int = Field(..., ge=0)
    fasting_bs: Literal[0, 1]
    resting_ecg: Literal["LVH", "Normal", "ST"]
    max_hr: int = Field(..., ge=60, le=250)
    exercise_angina: Literal["N", "Y"]
    oldpeak: float = Field(..., ge=0)
    st_slope: Literal["Down", "Flat", "Up"]


class PatientResponse(PatientCreate):
    id: int

    model_config = {"from_attributes": True}
