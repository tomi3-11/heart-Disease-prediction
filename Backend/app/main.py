from fastapi import FastAPI
from app.ml.preprocessing import preprocess
from app.ml.predictor import predict
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


@app.get("/test-preprocessing")
def test_preprocessing():
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

    processed = preprocess(sample)

    return processed.to_dict(orient="records")[0]

@app.get("/debug/encoders")
def debug_encoders():
    encoders = get_label_encoders()

    result = {}

    for name, encoder in encoders.items():
        result[name] = encoder.classes_.tolist()

    return result


@app.get("/test-prediction")
def test_prediction():
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

    processed = preprocess(sample)

    return predict(processed)
