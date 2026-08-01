import pandas as pd

from app.ml.model_loader import (
    get_feature_order,
    get_label_encoders,
)

def preprocess(data: dict):
    """
    Convert raw input into the format expected by the model.
    """
    df = pd.DataFrame([data])

    encoders = get_label_encoders()

    for column, encoder in encoders.items():
        df[column] = encoder.transform(df[column])

    feature_order = get_feature_order()

    df = df[feature_order]

    return df
