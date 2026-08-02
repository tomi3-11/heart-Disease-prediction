from fastapi import FastAPI
from app.ml.model_loader import load_artifacts
from app.ml.explainer import load_explainer
from app.routers.predictions import router as prediction_router
from app.routers.patients import router as patient_router
from app.routers.auth import router as auth_router
from app.db.base import Base
from app.db.session import engine
import app.models

from app.ml.preprocessing import preprocess
from app.ml.explainer import explain


app = FastAPI(
    title="Heart Disease Prediction API",
    version="1.0.0",
)

@app.on_event("startup")
def startup():
    load_artifacts()
    load_explainer()
  

app.include_router(prediction_router)
app.include_router(patient_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "API is running"}


@app.get("/test-shap")
def test_shap():
    sample = {
        "Age": 40,
        "Sex": "M",
        "ChestPainType": "ATA",
        "RestingBP": 120,
        "Cholesterol": 250,
        "FastingBS": 0,
        "RestingECG": "Normal",
        "MaxHR": 170,
        "ExerciseAngina": "N",
        "Oldpeak": 0.0,
        "ST_Slope": "Up",
    }

    features = preprocess(sample)

    return {
        "shap_values": explain(features)
    }
