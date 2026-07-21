import joblib
import pandas as pd
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Model path
MODEL_PATH = BASE_DIR / "models" / "churn_model.pkl"

print(MODEL_PATH)
print(MODEL_PATH.exists())

# Load model
model = joblib.load(MODEL_PATH)


def predict_customer(customer_data: dict):
    """
    Predict churn probability for a single customer.
    """

    df = pd.DataFrame([customer_data])

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    return prediction, probability