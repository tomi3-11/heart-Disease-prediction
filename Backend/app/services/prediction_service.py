from app.ml.preprocessing import preprocess
from app.ml.predictor import predict


def make_prediction(data: dict):
    """
    Preprocess input and return a prediction.
    """
    features = preprocess(data)
    return predict(features)
