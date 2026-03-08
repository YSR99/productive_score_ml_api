import os
from pydantic_settings import BaseSettings


# ----------------------------
# Existing ML Path Config
# ----------------------------
# PROJECT ROOT → PRODUCTIVE_ML_API
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

ARTIFACT_PATH = os.path.join(PROJECT_ROOT, "artifacts/v1/model.pkl")
FEATURE_SCHEMA_PATH = os.path.join(PROJECT_ROOT, "artifacts/v1/feature_order.json")


# ----------------------------
# Application Settings (JWT, etc.)
# ----------------------------
class Settings(BaseSettings):
    SECRET_KEY: str = "your-secret"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"   # load env vars if available


settings = Settings()
