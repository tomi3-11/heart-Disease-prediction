import shap

from app.ml.model_loader import get_model

explainer = None


def load_explainer():
    global explainer
    explainer = shap.TreeExplainer(get_model())


def explain(features):
    shap_values = explainer.shap_values(features)

    if isinstance(shap_values, list):
        shap_values = shap_values[1]

    return shap_values[0].tolist()
