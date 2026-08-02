from fastapi import FastAPI
from app.ml.model_loader import load_artifacts
from app.routers.predictions import router as prediction_router
from app.db.base import Base
from app.db.session import engine
import app.models


app = FastAPI(
    title="Heart Disease Prediction API",
    version="1.0.0",
)

@app.on_event("startup")
def startup():
    load_artifacts()
    Base.metadata.create_all(bind=engine)

app.include_router(prediction_router)

@app.get("/")
def root():
    return {"message": "API is running"}
