import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
LOG_FILE = BASE_DIR / "app" / "prediction_logs.csv"


def save_prediction(customer, prediction, probability, risk):
    """
    Save each prediction to prediction_logs.csv
    """

    row = customer.copy()

    # Prediction
    row["Prediction"] = "Churn" if prediction == 1 else "No Churn"

    # Probability (%)
    row["Probability"] = round(probability * 100, 2)

    # Store clean risk text (no emojis)
    clean_risk = (
        risk.replace("🟢 ", "")
            .replace("🟡 ", "")
            .replace("🔴 ", "")
            .strip()
    )

    row["Risk"] = clean_risk

    df = pd.DataFrame([row])

    if LOG_FILE.exists():
        df.to_csv(
            LOG_FILE,
            mode="a",
            header=False,
            index=False
        )
    else:
        df.to_csv(
            LOG_FILE,
            index=False
        )