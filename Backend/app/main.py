from fastapi import FastAPI
from app.ml.model_loader import (
    load_artifacts,
    get_model,
    get_label_encoders,
    get_feature_order,
)

app = FastAPI(
    title="Heart Disease Prediction API",
    version="1.0.0",
)

@app.on_event("startup")
def startup():
    load_artifacts()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/test-loader")
def test_loader():
    return {
        "model_loaded": get_model() is not None,
        "encoders_loaded": get_label_encoders() is not None,
        "feature_order": get_feature_order(),
    }
