import joblib

from app.core.config import (
    ENCODER_PATH,
    FEATURE_PATH,
    MODEL_PATH,
)

_model = None
_label_encoders = None
_feature_order = None


def load_artifacts():
    """Load all ML artifacts into memory."""

    global _model
    global _label_encoders
    global _feature_order

    _model = joblib.load(MODEL_PATH)
    _label_encoders = joblib.load(ENCODER_PATH)
    _feature_order = joblib.load(FEATURE_PATH)


def get_model():
    return _model


def get_label_encoders():
    return _label_encoders


def get_feature_order():
    return _feature_order
