# 🚀 Intelligent Customer Churn Prediction

### AI-Powered Customer Retention Intelligence Platform

An end-to-end machine learning platform that predicts customer churn, classifies customer risk, and generates actionable retention recommendations.

The project is deployed using **AWS ECS Fargate**, exposed through an **Application Load Balancer**, and connected to a **Streamlit frontend** with automated CI/CD through **GitHub Actions**.

🔗 **Live Demo:** https://intelligent-customer-churn-prediction-nshbyqpwm54dtq5w7miwsk.streamlit.app/

---

# 📌 Project Overview

Customer churn is a major challenge for subscription-based businesses.

This project uses machine learning to:

- Predict whether a customer is likely to churn
- Calculate churn probability
- Classify customers into risk levels
- Generate personalized retention recommendations
- Provide an interactive dashboard for predictions and analytics
- Expose predictions through a production REST API
- Deploy the ML backend on AWS
- Monitor the backend using CloudWatch
- Automatically scale the API based on CPU utilization
- Automatically deploy new versions through GitHub Actions

The goal is to move beyond simply predicting churn and provide **business-oriented actions that can help retain high-risk customers.**

---

# ✨ Key Features

### 🤖 Machine Learning

- Customer churn prediction
- Churn probability estimation
- Risk classification
- Logistic Regression model
- Data preprocessing and feature engineering
- Model evaluation and performance metrics

### 📊 Analytics Dashboard

- Interactive Streamlit dashboard
- Customer-level predictions
- Prediction history
- Risk analysis
- Project information
- Business-oriented insights

### 💡 Retention Intelligence

The recommendation engine generates actions based on customer risk and service characteristics.

Examples include:

- Contact high-risk customers
- Offer loyalty discounts
- Assign retention executives
- Recommend longer-term contracts
- Promote technical support
- Promote online security services

### ☁️ Production Deployment

- FastAPI REST API
- Dockerized ML backend
- AWS ECS Fargate
- Amazon ECR
- Application Load Balancer
- ECS health checks
- CloudWatch logging
- CloudWatch CPU monitoring
- SNS email alerts
- ECS target-tracking auto scaling
- GitHub Actions CI/CD

---

# 🏗️ System Architecture

text
                         ┌─────────────────────┐
                         │   GitHub Repository  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   GitHub Actions     │
                         │       CI/CD          │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     Amazon ECR       │
                         │    Docker Image      │
                         └──────────┬──────────┘
                                    │
                                    ▼

┌──────────────┐          ┌─────────────────────┐
│     User     │ ───────► │  Streamlit Cloud    │
└──────────────┘          │    Frontend         │
                          └──────────┬──────────┘
                                     │
                                     │ HTTP
                                     ▼
                          ┌─────────────────────┐
                          │ Application Load    │
                          │ Balancer (ALB)      │
                          └──────────┬──────────┘
                                     │
                                     ▼
                          ┌─────────────────────┐
                          │    AWS ECS Fargate  │
                          │    FastAPI Backend  │
                          └──────────┬──────────┘
                                     │
                                     ▼
                          ┌─────────────────────┐
                          │    ML Churn Model   │
                          └──────────┬──────────┘
                                     │
                         ┌───────────┴───────────┐
                         ▼                       ▼
                  ┌──────────────┐       ┌────────────────┐
                  │ Risk Level   │       │ Recommendation │
                  │ Classification│       │    Engine      │
                  └──────────────┘       └────────────────┘


             ┌─────────────────────────────────────┐
             │          AWS Monitoring             │
             │                                     │
             │ ECS → CloudWatch → SNS → Email     │
             └─────────────────────────────────────┘

                    ECS Auto Scaling
                         │
                    1 ───► 2 Tasks
🛠️ Technology Stack
Programming & Data
Python
Pandas
NumPy
Scikit-learn
Machine Learning
Logistic Regression
Feature Engineering
Model Evaluation
Probability-based Risk Classification
Backend & API
FastAPI
Pydantic
Uvicorn
Frontend & Visualization
Streamlit
Plotly
Cloud & Deployment
AWS ECS Fargate
Amazon ECR
Application Load Balancer
Amazon CloudWatch
Amazon SNS
Docker
DevOps
Git
GitHub
GitHub Actions
CI/CD
📂 Project Structure
Intelligent-Customer-Churn-Prediction/
│
├── app/
│   ├── app.py
│   ├── assets/
│   └── pages/
│
├── api/
│   ├── main.py
│   └── schemas.py
│
├── assets/
│
├── dashboard/
│
├── data/
│
├── models/
│   └── churn_model.pkl
│
├── notebooks/
│
├── pages/
│   ├── Dashboard.py
│   ├── Prediction_History.py
│   └── Project_Info.py
│
├── reports/
│   └── metrics/
│
├── src/
│   ├── models/
│   │   ├── config.py
│   │   ├── evaluate.py
│   │   ├── metrics.py
│   │   ├── pipeline.py
│   │   ├── predict.py
│   │   ├── risk.py
│   │   └── train.py
│   │
│   └── services/
│       ├── logging_service.py
│       ├── recommendation_service.py
│       └── utils/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── Dockerfile
├── requirements.txt
├── README.md
└── LICENSE
🔄 Machine Learning Workflow
Raw Customer Data
        │
        ▼
Data Cleaning
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Model Training
        │
        ▼
Logistic Regression
        │
        ▼
Churn Probability
        │
        ▼
Risk Classification
        │
        ▼
Retention Recommendations
🧠 Prediction Pipeline

The FastAPI backend accepts customer information through a REST endpoint.

Customer Data
      │
      ▼
FastAPI Request
      │
      ▼
Pydantic Validation
      │
      ▼
ML Model
      │
      ▼
Churn Prediction
      │
      ▼
Churn Probability
      │
      ▼
Risk Classification
      │
      ▼
Retention Recommendations
      │
      ▼
JSON Response

Example response:

{
  "prediction": 1,
  "churn_probability": 0.81,
  "risk": "HIGH RISK",
  "recommendations": [
    "Contact the customer within 48 hours.",
    "Offer a loyalty discount.",
    "Assign a retention executive."
  ]
}
☁️ AWS Deployment

The ML backend is containerized using Docker and deployed on AWS.

Deployment Flow
Developer
    │
    ▼
Git Push
    │
    ▼
GitHub Actions
    │
    ▼
Docker Build
    │
    ▼
Amazon ECR
    │
    ▼
AWS ECS Fargate
    │
    ▼
Application Load Balancer
    │
    ▼
FastAPI API
AWS Services Used
Service	Purpose
Amazon ECR	Stores Docker container images
Amazon ECS Fargate	Runs the FastAPI backend
Application Load Balancer	Exposes and routes API traffic
CloudWatch	Logs and monitors the application
SNS	Sends monitoring alerts
ECS Auto Scaling	Scales tasks based on CPU utilization
🔁 CI/CD Pipeline

GitHub Actions automatically deploys the backend whenever changes are pushed to the main branch.

Git Push
   │
   ▼
GitHub Actions
   │
   ├── Checkout Repository
   │
   ├── Configure AWS Credentials
   │
   ├── Login to Amazon ECR
   │
   ├── Build Docker Image
   │
   ├── Push Image to ECR
   │
   └── Deploy to ECS

This removes the need to manually build and deploy the backend after every code update.

📈 Monitoring & Auto Scaling

The deployed API is monitored using Amazon CloudWatch.

Current monitoring includes:

ECS application logs
API request logs
ECS CPU utilization monitoring
CloudWatch CPU alarm
SNS email notifications

The ECS service also uses target-tracking auto scaling.

Normal Load
    │
    ▼
1 ECS Task

High CPU Utilization
    │
    ▼
Auto Scaling
    │
    ▼
2 ECS Tasks
📊 Dashboard Modules
🏠 Main Dashboard

Provides an overview of the churn prediction platform.

🔮 Customer Prediction

Allows users to enter customer information and receive:

Churn prediction
Churn probability
Risk level
Retention recommendations
📜 Prediction History

Stores and displays previous prediction results.

ℹ️ Project Information

Provides information about the project, methodology, and technology stack.

💼 Business Impact

The system can help businesses:

Identify customers at high risk of churn
Prioritize retention efforts
Reduce unnecessary retention spending
Personalize customer offers
Improve customer engagement
Support data-driven retention strategies

Instead of treating every customer equally, businesses can focus their resources on customers who are most likely to leave.

🚀 Running Locally
1. Clone the repository
git clone https://github.com/Ayush-learn/Intelligent-Customer-Churn-Prediction.git
cd Intelligent-Customer-Churn-Prediction
2. Create a virtual environment
python -m venv venv
Windows
venv\Scripts\activate
Linux / macOS
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Run the FastAPI backend
uvicorn api.main:app --reload

API documentation:

http://127.0.0.1:8000/docs
5. Run the Streamlit application
streamlit run app/app.py
🔮 Future Enhancements
Random Forest & XGBoost model comparison
Explainable AI using SHAP
Cloud database integration
User authentication and authorization
Model drift monitoring
Advanced application monitoring
HTTPS with custom domain
Automated model retraining pipeline
👨‍💻 Author
Ayush Kumar

Machine Learning & Data Science Enthusiast

🔗 GitHub: https://github.com/Ayush-learn

🔗 LinkedIn: [Add your LinkedIn profile]

⭐ Project Highlights
Machine Learning
       +
FastAPI REST API
       +
Docker
       +
AWS ECS Fargate
       +
Amazon ECR
       +
Application Load Balancer
       +
CloudWatch Monitoring
       +
SNS Alerts
       +
Auto Scaling
       +
GitHub Actions CI/CD

An end-to-end ML system built from model development to production deployment.
