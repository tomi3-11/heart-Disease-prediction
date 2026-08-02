from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_PATH = BASE_DIR / "ml_artifacts" / "random_forest_model.joblib"
ENCODER_PATH = BASE_DIR / "ml_artifacts" / "label_encoders.joblib"
FEATURE_PATH = BASE_DIR / "ml_artifacts" / "feature_order.joblib"

MODEL_VERSION = "1.0.0"

DATABASE_URL = os.getenv("DATABASE_URL")
