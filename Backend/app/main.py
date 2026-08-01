from fastapi import FastAPI
from app.ml.model_loader import load_artifacts
from app.routers.predictions import router as prediction_router
app = FastAPI(
    title="Heart Disease Prediction API",
    version="1.0.0",
)

@app.on_event("startup")
def startup():
    load_artifacts()

app.include_router(prediction_router)

@app.get("/")
def root():
    return {"message": "API is running"}
