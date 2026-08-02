import pandas as pd

from app.ml.model_loader import (
    get_feature_order,
    get_label_encoders,
)


def preprocess(data: dict):
    df = pd.DataFrame([data])

    encoders = get_label_encoders()

    for column, encoder in encoders.items():
        df[column] = encoder.transform(df[column])

    df = df[get_feature_order()]

    return df
