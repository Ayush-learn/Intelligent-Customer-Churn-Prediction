# 🚀 Intelligent Customer Churn Prediction

### AI-Powered Customer Retention Intelligence Platform

An end-to-end machine learning platform that predicts customer churn, classifies customer risk, and generates actionable retention recommendations.

The project combines a machine learning model with a FastAPI backend, Docker, AWS ECS Fargate, monitoring, auto scaling, and GitHub Actions CI/CD.

🔗 **Live Demo:** https://intelligent-customer-churn-prediction-nshbyqpwm54dtq5w7miwsk.streamlit.app/

---

## 📌 Project Overview

Customer churn is a major challenge for subscription-based businesses.

This project uses machine learning to:

- Predict whether a customer is likely to churn
- Calculate churn probability
- Classify customers into risk levels
- Generate actionable retention recommendations
- Provide an interactive Streamlit dashboard
- Expose predictions through a REST API
- Deploy the backend on AWS
- Monitor the application using CloudWatch
- Automatically scale the backend based on CPU utilization
- Automatically deploy updates using GitHub Actions

The goal is to move beyond simply predicting churn and provide **business-oriented actions that can help retain high-risk customers.**

---

## ✨ Key Features

### 🤖 Machine Learning

- Customer churn prediction
- Churn probability estimation
- Risk classification
- Logistic Regression model
- Data preprocessing
- Feature engineering
- Model evaluation

### 📊 Interactive Dashboard

- Streamlit-based interface
- Customer churn prediction
- Risk assessment
- Prediction history
- Business insights
- Interactive visualizations using Plotly

### 💡 Retention Intelligence

The recommendation engine generates retention strategies based on customer risk and service characteristics.

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

## 🏗️ System Architecture

mermaid
flowchart TD

   A[GitHub Repository] --> B[GitHub Actions CI/CD]
  B --> C[Amazon ECR]
  C --> D[AWS ECS Fargate]
  
   U[User] --> S[Streamlit Cloud]
  S -->|HTTP Request| L[Application Load Balancer]
  L --> D
  
  D --> F[FastAPI Backend]
  F --> M[ML Churn Model]
  
   M --> P[Churn Probability]
  P --> R[Risk Classification]
   R --> Rec[Retention Recommendation Engine]
  
  D --> CW[Amazon CloudWatch]
  CW --> SNS[Amazon SNS]
  SNS --> E[Email Alerts]
  
  D --> AS[ECS Auto Scaling]
  AS --> D
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
🔄 Machine Learning Workflow
🧠 Prediction Pipeline

The FastAPI backend accepts customer information through a REST endpoint and returns a complete prediction response.

Example API Response
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

The ML backend is containerized using Docker and deployed on AWS ECS Fargate.

Deployment Flow
AWS Services Used
Service	Purpose
Amazon ECR	Stores Docker container images
Amazon ECS Fargate	Runs the FastAPI backend
Application Load Balancer	Routes API traffic
Amazon CloudWatch	Application logging and monitoring
Amazon SNS	Sends monitoring alerts
ECS Auto Scaling	Scales backend tasks based on CPU utilization
🔁 CI/CD Pipeline

GitHub Actions automatically deploys the backend whenever changes are pushed to the main branch.

This removes the need to manually build and deploy the backend after every code update.

📈 Monitoring & Auto Scaling

The backend is monitored using Amazon CloudWatch.

Current monitoring includes:

ECS application logs
API request logs
CPU utilization monitoring
CloudWatch CPU alarm
SNS email notifications

The ECS service uses target-tracking auto scaling.

📊 Dashboard Modules
🏠 Main Dashboard

Provides an overview of the customer churn prediction platform.

🔮 Customer Prediction

Users can enter customer information and receive:

Churn prediction
Churn probability
Risk level
Retention recommendations
📜 Prediction History

Displays previous customer prediction results.

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
