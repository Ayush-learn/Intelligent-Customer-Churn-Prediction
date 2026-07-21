import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Customer Retention Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Load CSS
# -----------------------------
css_path = Path(__file__).parent.parent / "assets" / "style.css"

if css_path.exists():
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# -----------------------------
# Load Data
# -----------------------------
LOG_FILE = Path(__file__).parent.parent / "prediction_logs.csv"

if not LOG_FILE.exists():
    st.warning("No prediction history available.")
    st.stop()

history = pd.read_csv(LOG_FILE)

if history.empty:
    st.info("Prediction history is empty.")
    st.stop()

history["Risk"] = (
    history["Risk"]
    .astype(str)
    .str.upper()
    .str.strip()
)

# -----------------------------
# Header
# -----------------------------

left, right = st.columns([4,1])

with left:

    st.markdown("""
    <h1 style="margin-bottom:0;">
    👋 Welcome Back, Ayush
    </h1>

    <p style="
    color:#94A3B8;
    font-size:18px;
    margin-top:0;
    ">
    Monitor customer churn predictions and business insights.
    </p>
    """, unsafe_allow_html=True)

with right:

    search = st.text_input(
        "",
        placeholder="🔍 Search Customer"
    )

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

# -----------------------------
# KPI Values
# -----------------------------

total_predictions = len(history)

high = history["Risk"].str.contains("HIGH").sum()
medium = history["Risk"].str.contains("MEDIUM").sum()
low = history["Risk"].str.contains("LOW").sum()

avg_probability = history["Probability"].mean()

# -----------------------------
# KPI Cards
# -----------------------------

cards = [
    ("📊","Total Predictions",total_predictions,"#2563EB"),
    ("🔴","High Risk",high,"#DC2626"),
    ("🟡","Medium Risk",medium,"#D97706"),
    ("🟢","Low Risk",low,"#16A34A")
]

cols = st.columns(4)

for col,(icon,title,value,color) in zip(cols,cards):

    with col:

        st.markdown(f"""
        <div style="
        background:linear-gradient(135deg,{color},#111827);
        padding:25px;
        border-radius:18px;
        color:white;
        box-shadow:0 10px 25px rgba(0,0,0,.35);
        ">

        <div style="font-size:38px;">
        {icon}
        </div>

        <div style="
        color:#CBD5E1;
        font-size:16px;
        margin-top:10px;
        ">
        {title}
        </div>

        <div style="
        font-size:36px;
        font-weight:bold;
        margin-top:5px;
        ">
        {value}
        </div>

        </div>
        """, unsafe_allow_html=True)

st.divider()

# -----------------------------
# Model Status
# -----------------------------

st.subheader("🤖 Model Status")

m1,m2,m3 = st.columns(3)

with m1:
    st.success("🟢 Model Loaded")

with m2:
    st.info("Algorithm: Logistic Regression")

with m3:
    st.metric(
        "Average Probability",
        f"{avg_probability:.2f}%"
    )

st.divider()

# -----------------------------
# Filters
# -----------------------------

st.subheader("🎛 Dashboard Filters")

f1,f2,f3,f4 = st.columns(4)

with f1:

    contract_filter = st.selectbox(
        "Contract",
        ["All"] + sorted(history["Contract"].dropna().unique().tolist())
    )

with f2:

    payment_filter = st.selectbox(
        "Payment",
        ["All"] + sorted(history["PaymentMethod"].dropna().unique().tolist())
    )

with f3:

    risk_filter = st.selectbox(
        "Risk",
        [
            "All",
            "HIGH RISK",
            "MEDIUM RISK",
            "LOW RISK"
        ]
    )

with f4:

    prediction_filter = st.selectbox(
        "Prediction",
        [
            "All",
            "Churn",
            "No Churn"
        ]
    )

filtered = history.copy()

if contract_filter != "All":
    filtered = filtered[
        filtered["Contract"] == contract_filter
    ]

if payment_filter != "All":
    filtered = filtered[
        filtered["PaymentMethod"] == payment_filter
    ]

if risk_filter != "All":
    filtered = filtered[
        filtered["Risk"] == risk_filter
    ]

if prediction_filter != "All":
    filtered = filtered[
        filtered["Prediction"] == prediction_filter
    ]

if search:
    filtered = filtered[
        filtered.astype(str)
        .apply(lambda x: x.str.contains(search, case=False, na=False))
        .any(axis=1)
    ]

st.divider()
# ==========================================================
# 📊 Analytics Section
# ==========================================================

st.markdown("## 📊 Analytics Overview")

col1, col2 = st.columns(2)

# -------------------------
# Donut Chart
# -------------------------

with col1:

    fig = px.pie(
        filtered,
        names="Risk",
        hole=0.65,
        color="Risk",
        color_discrete_map={
            "HIGH RISK": "#EF4444",
            "MEDIUM RISK": "#F59E0B",
            "LOW RISK": "#10B981"
        }
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig.update_layout(
        title="Risk Distribution",
        paper_bgcolor="#0F172A",
        plot_bgcolor="#0F172A",
        font_color="white",
        height=420
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Probability Histogram
# -------------------------

with col2:

    fig = px.histogram(
        filtered,
        x="Probability",
        nbins=20,
        color_discrete_sequence=["#3B82F6"]
    )

    fig.update_layout(
        title="Probability Distribution",
        paper_bgcolor="#0F172A",
        plot_bgcolor="#0F172A",
        font_color="white",
        height=420
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================================
# 📈 Trend & Prediction Charts
# ==========================================================

col3, col4 = st.columns(2)

# -------------------------
# Trend Chart
# -------------------------

with col3:

    if "Timestamp" in filtered.columns:

        trend = (
            filtered
            .groupby("Timestamp")
            .size()
            .reset_index(name="Predictions")
        )

        fig = px.line(
            trend,
            x="Timestamp",
            y="Predictions",
            markers=True
        )

        fig.update_layout(
            title="Prediction Trend",
            paper_bgcolor="#0F172A",
            plot_bgcolor="#0F172A",
            font_color="white",
            height=420
        )

        st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Prediction Distribution
# -------------------------

with col4:

    fig = px.bar(
        filtered["Prediction"]
        .value_counts()
        .reset_index(),
        x="Prediction",
        y="count",
        color="Prediction"
    )

    fig.update_layout(
        title="Prediction Distribution",
        paper_bgcolor="#0F172A",
        plot_bgcolor="#0F172A",
        font_color="white",
        showlegend=False,
        height=420
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================================
# 💡 AI Business Insights
# ==========================================================

st.markdown("## 💡 Business Insights")

left, right = st.columns(2)

high_percent = (high / total_predictions * 100) if total_predictions else 0

with left:

    st.info(f"""
### 📌 Key Findings

• **{high_percent:.1f}%** customers are High Risk.

• Average churn probability is **{avg_probability:.2f}%**

• Total predictions analyzed: **{total_predictions}**

• Low-risk customers form the healthiest customer segment.
""")

with right:

    st.success("""
### 🚀 Recommended Actions

✅ Contact High Risk customers first

✅ Offer retention discounts

✅ Improve customer support follow-ups

✅ Promote long-term contracts

✅ Encourage Auto Payment methods
""")

st.divider()

# ==========================================================
# 📋 Recent Predictions
# ==========================================================

st.markdown("## 📋 Recent Predictions")

show_df = filtered.tail(20)

st.dataframe(
    show_df,
    use_container_width=True,
    height=450
)

# ==========================================================
# 📥 Export Buttons
# ==========================================================

c1, c2 = st.columns(2)

with c1:

    st.download_button(
        "⬇ Download CSV",
        filtered.to_csv(index=False),
        file_name="prediction_history.csv",
        mime="text/csv"
    )

with c2:

    st.download_button(
        "⬇ Download Excel (CSV)",
        filtered.to_csv(index=False),
        file_name="prediction_history.xls",
        mime="application/vnd.ms-excel"
    )