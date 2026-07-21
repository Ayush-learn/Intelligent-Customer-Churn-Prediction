import streamlit as st
import sys
from pathlib import Path

# ==========================================================
# Project Path
# ==========================================================

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

# ==========================================================
# Page Config
# ==========================================================

st.set_page_config(
    page_title="Customer Retention Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

# ==========================================================
# Load CSS
# ==========================================================

css_file = Path(__file__).parent / "assets" / "style.css"

if css_file.exists():
    with open(css_file) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ==========================================================
# Imports
# ==========================================================

from dashboard.widgets import metric_cards
from dashboard.recommendations import show_recommendations

from src.models.predict import predict_customer
from src.models.risk import get_risk_level

from src.services.recommendation_service import (
    get_recommendations
)

from src.services.logging_service import (
    save_prediction
)

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.markdown("# 📊")

    st.markdown("## Customer Retention")

    st.caption("Machine Learning Dashboard")

    st.divider()

    st.success("🟢 Model Loaded")

    st.write("**Algorithm**")

    st.caption("Logistic Regression")

    st.write("**Version**")

    st.caption("1.0")

    st.divider()

    st.write("### 👨‍💻 Developer")

    st.write("Ayush Kumar")

    st.caption("Machine Learning Engineer")

# ==========================================================
# Hero Banner
# ==========================================================

st.markdown("""
<div style="
background:linear-gradient(135deg,#2563EB,#1E3A8A);
padding:28px;
border-radius:20px;
color:white;
margin-bottom:25px;
box-shadow:0 15px 35px rgba(0,0,0,.35);
">

<h1 style="
margin:0;
font-size:40px;
">
📊 Customer Retention Intelligence Platform
</h1>

<p style="
margin-top:12px;
font-size:18px;
color:#E2E8F0;
">

Predict customer churn using Machine Learning,
analyze customer risk,
and generate intelligent business recommendations.

</p>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# Search Bar
# ==========================================================

top1, top2 = st.columns([4,1])

with top1:

    search = st.text_input(
        "",
        placeholder="🔍 Search Customer"
    )

with top2:

    period = st.selectbox(
        "",
        [
            "Last 7 Days",
            "Last 30 Days",
            "Last 90 Days",
            "All Time"
        ]
    )

st.divider()

# ==========================================================
# Customer Form
# ==========================================================

left, right = st.columns(2)

# ==========================================================
# Customer Details
# ==========================================================

with left:

    st.markdown("""
    <div style="
    background:#111827;
    padding:15px;
    border-radius:14px;
    border-left:5px solid #2563EB;
    margin-bottom:15px;
    ">

    <h3 style="
    color:white;
    margin:0;
    ">
    👤 Customer Details
    </h3>

    </div>
    """, unsafe_allow_html=True)

    gender = st.selectbox(
        "Gender",
        ["Male","Female"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        [0,1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes","No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes","No"]
    )

    tenure = st.slider(
        "Tenure",
        0,
        72,
        12
    )

    phone = st.selectbox(
        "Phone Service",
        ["Yes","No"]
    )

    multiple = st.selectbox(
        "Multiple Lines",
        [
            "Yes",
            "No",
            "No phone service"
        ]
    )

# ==========================================================
# Internet Services
# ==========================================================

with right:

    st.markdown("""
    <div style="
    background:#111827;
    padding:15px;
    border-radius:14px;
    border-left:5px solid #06B6D4;
    margin-bottom:15px;
    ">

    <h3 style="
    color:white;
    margin:0;
    ">
    🌐 Internet Services
    </h3>

    </div>
    """, unsafe_allow_html=True)

    internet = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )

    security = st.selectbox(
        "Online Security",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    backup = st.selectbox(
        "Online Backup",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    protection = st.selectbox(
        "Device Protection",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    support = st.selectbox(
        "Tech Support",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    tv = st.selectbox(
        "Streaming TV",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    movies = st.selectbox(
        "Streaming Movies",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

st.divider()
# ==========================================================
# Billing Details
# ==========================================================

st.markdown("""
<div style="
background:#111827;
padding:15px;
border-radius:14px;
border-left:5px solid #10B981;
margin-top:10px;
margin-bottom:20px;
">

<h3 style="
margin:0;
color:white;
">
💳 Billing Details
</h3>

</div>
""", unsafe_allow_html=True)

bill1, bill2 = st.columns(2)

with bill1:

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    paperless = st.selectbox(
        "Paperless Billing",
        [
            "Yes",
            "No"
        ]
    )

    payment = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

with bill2:

    monthly = st.number_input(
        "Monthly Charges",
        min_value=18.0,
        max_value=120.0,
        value=70.0,
        step=0.5
    )

    total = st.number_input(
        "Total Charges",
        min_value=0.0,
        max_value=9000.0,
        value=2000.0,
        step=10.0
    )

# ==========================================================
# Customer Summary
# ==========================================================

st.divider()

st.markdown("""
<div style="
background:#111827;
padding:18px;
border-radius:14px;
border-left:5px solid #F59E0B;
margin-bottom:20px;
">

<h3 style="margin:0;color:white;">
📋 Customer Summary
</h3>

</div>
""", unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.metric("Tenure", f"{tenure} Months")

with s2:
    st.metric("Monthly Bill", f"${monthly:.2f}")

with s3:
    st.metric("Contract", contract)

with s4:
    st.metric("Internet", internet)

# ==========================================================
# Analyze Button
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

left, center, right = st.columns([2,3,2])

with center:

    predict = st.button(
        "🚀 Analyze Customer",
        use_container_width=True,
        type="primary"
    )

# ==========================================================
# Prediction
# ==========================================================

if predict:

    customer = {

        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "MultipleLines": multiple,
        "InternetService": internet,
        "OnlineSecurity": security,
        "OnlineBackup": backup,
        "DeviceProtection": protection,
        "TechSupport": support,
        "StreamingTV": tv,
        "StreamingMovies": movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total

    }

    prediction, probability = predict_customer(customer)

    risk = get_risk_level(probability)

    recommendations = get_recommendations(
        probability,
        customer
    )

    save_prediction(
        customer,
        prediction,
        probability,
        risk
    )

    st.divider()
    
# ==========================================================
# Prediction Result
# ==========================================================

    st.markdown("""
    <div style="
    background:#111827;
    padding:18px;
    border-radius:14px;
    border-left:5px solid #3B82F6;
    margin-bottom:20px;
    ">
        <h2 style="margin:0;color:white;">
        🎯 Prediction Result
        </h2>
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([2, 1])

    # ------------------------------------------------------
    # Result Card
    # ------------------------------------------------------

    with left:

        if prediction == 1:

            result_color = "#EF4444"
            result_icon = "🔴"
            result_title = "HIGH CHURN RISK"

            summary = """
            This customer has a high probability of leaving.
            Immediate retention actions are recommended.
            """

        else:

            result_color = "#10B981"
            result_icon = "🟢"
            result_title = "LOW CHURN RISK"

            summary = """
            This customer is likely to remain with the company.
            Continue delivering a positive experience.
            """

        st.markdown(f"""
        <div style="
        background:#111827;
        padding:30px;
        border-radius:18px;
        border-left:8px solid {result_color};
        box-shadow:0 15px 30px rgba(0,0,0,.35);
        ">

        <h1 style="
        color:{result_color};
        margin:0;
        ">
        {result_icon} {result_title}
        </h1>

        <p style="
        color:#CBD5E1;
        font-size:18px;
        margin-top:18px;
        ">
        {summary}
        </p>

        </div>
        """, unsafe_allow_html=True)

    # ------------------------------------------------------
    # Probability
    # ------------------------------------------------------

    with right:

        st.metric(
            "Churn Probability",
            f"{probability:.2f}%"
        )

        st.metric(
            "Risk Level",
            risk
        )

        confidence = max(probability, 100 - probability)

        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

    st.divider()

# ==========================================================
# Recommendations
# ==========================================================

    st.markdown("""
    <div style="
    background:#111827;
    padding:18px;
    border-radius:14px;
    border-left:5px solid #F59E0B;
    margin-bottom:20px;
    ">
        <h2 style="margin:0;color:white;">
        💡 Business Recommendations
        </h2>
    </div>
    """, unsafe_allow_html=True)

    show_recommendations(recommendations)

# ==========================================================
# AI Summary
# ==========================================================

    st.divider()

    st.markdown("""
    <div style="
    background:#111827;
    padding:20px;
    border-radius:14px;
    border-left:5px solid #8B5CF6;
    ">
        <h2 style="margin:0;color:white;">
        🤖 AI Business Summary
        </h2>
    </div>
    """, unsafe_allow_html=True)

    if prediction == 1:

        st.warning(f"""
### Customer Risk Analysis

This customer shows a **{probability:.2f}%** probability of churn.

Primary risk factors may include:

- Month-to-Month Contract
- Payment Method
- Low Tenure
- High Monthly Charges

**Recommended Action**

Prioritize this customer for proactive retention campaigns,
discount offers, and customer success follow-up.
""")

    else:

        st.success(f"""
### Customer Risk Analysis

This customer shows only **{probability:.2f}%** probability of churn.

Customer loyalty appears healthy.

**Recommended Action**

Maintain current engagement strategy and
continue providing excellent service.
""")

# ==========================================================
# Footer
# ==========================================================

st.markdown("---")

st.markdown("""
<div style="
text-align:center;
color:#94A3B8;
padding:15px;
">

Customer Retention Intelligence Platform

Version 1.0

Developed by <b>Ayush Kumar</b>

</div>
""", unsafe_allow_html=True)