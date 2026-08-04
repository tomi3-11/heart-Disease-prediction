from app.ml.model_loader import get_model


def predict(features):
    """
    Make prediction using the trained model.
    """

    model = get_model()

    prediction = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]

    return {
        "prediction": int(prediction),
        "probability": float(probabilities[prediction]),
    }
