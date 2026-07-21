import streamlit as st
from pathlib import Path

css_file = Path("assets/style.css")

with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.set_page_config(page_title="Project Info")

st.title("ℹ Project Information")

st.header("Customer Retention Intelligence Dashboard")

st.markdown("""
### 🚀 Tech Stack

- Python
- Streamlit
- Scikit-Learn
- Pandas
- Plotly
- Joblib

---

### 🤖 Machine Learning Model

- Logistic Regression
- Hyperparameter Tuned
- Pipeline Based
- Standard Scaler
- One Hot Encoding

---

### 📊 Dataset

IBM Telco Customer Churn Dataset

- 7043 Customers
- 20 Features
- Binary Classification

---

### 🎯 Features

✅ Customer Churn Prediction

✅ Churn Probability

✅ Risk Analysis

✅ Business Recommendations

✅ Prediction History

✅ Dashboard Analytics

---

### 📈 Model Performance

Accuracy : **82%**

Precision : **79%**

Recall : **72%**

F1 Score : **75%**

ROC AUC : **0.85**

---

### 👨‍💻 Developed By

Ayush Kumar

B.Tech Information Science

Data Scientist Portfolio Project
""")