import joblib
import json
import pandas as pd
from app.core.config import ARTIFACT_PATH, FEATURE_SCHEMA_PATH


class ProductivityModel:
    def __init__(self):
        # Load ML model
        self.model = joblib.load(ARTIFACT_PATH)

        # Load feature schema
        with open(FEATURE_SCHEMA_PATH, "r") as f:
            schema = json.load(f)

        self.numeric_features = schema["numeric_features"]

    def predict(self, data: dict):
        df = pd.DataFrame([data])

        print("\n===== INPUT DATAFRAME =====")
        print(df)
        print(df.dtypes)
        print("==========================\n")

        # enforce order
        df = df[self.numeric_features]

        prediction = self.model.predict(df)[0]
        return float(prediction)


model_service = ProductivityModel()
