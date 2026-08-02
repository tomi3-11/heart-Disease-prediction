from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import ConfigDict
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_PATH = BASE_DIR / "ml_artifacts" / "random_forest_model.joblib"
ENCODER_PATH = BASE_DIR / "ml_artifacts" / "label_encoders.joblib"
FEATURE_PATH = BASE_DIR / "ml_artifacts" / "feature_order.joblib"

MODEL_VERSION = "1.0.0"

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    model_config = ConfigDict(env_file=".env", extra="ignore")


settings = Settings()

DATABASE_URL = settings.database_url
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

#DATABASE_URL = os.getenv("DATABASE_URL")
