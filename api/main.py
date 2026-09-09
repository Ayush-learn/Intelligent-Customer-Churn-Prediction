from fastapi import FastAPI

from api.schemas import CustomerData

from src.models.predict import predict_customer
from src.models.risk import get_risk_level
from src.services.recommendation_service import get_recommendations


app = FastAPI(
    title="Customer Churn Prediction API",
    description="ML API for customer churn prediction and retention recommendations",
    version="1.0.0"
)


@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "service": "customer-churn-api"
    }


@app.post("/predict")
def predict(customer: CustomerData):

    customer_data = customer.model_dump()

    prediction, probability = predict_customer(customer_data)

    risk = get_risk_level(probability)

    recommendations = get_recommendations(
        probability,
        customer_data
    )

    return {
        "prediction": int(prediction),
        "churn_probability": float(probability),
        "risk": risk,
        "recommendations": recommendations
    }