import streamlit as st
import pandas as pd
import plotly.express as px
from dashboard.widgets import metric_card   # ✅ new import


def show_dashboard(history):

    if history.empty:
        st.info("No predictions available.")
        return

    # -------------------------
    # Clean Risk Column
    # -------------------------
    history["Risk"] = (
        history["Risk"]
        .astype(str)
        .str.upper()
        .str.strip()
    )

    # -------------------------
    # Dashboard Metrics
    # -------------------------

    total_predictions = len(history)

    high_risk = history["Risk"].str.contains("HIGH").sum()
    medium_risk = history["Risk"].str.contains("MEDIUM").sum()
    low_risk = history["Risk"].str.contains("LOW").sum()

    avg_probability = history["Probability"].mean()

    st.title("📊 Customer Retention Analytics Dashboard")

    # -------------------------
    # Custom Metric Cards
    # -------------------------
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card(
            "Predictions",
            total_predictions,
            "📊",
            "#2563EB"
        )

    with col2:
        metric_card(
            "High Risk",
            high_risk,
            "🔴",
            "#DC2626"
        )

    with col3:
        metric_card(
            "Medium Risk",
            medium_risk,
            "🟡",
            "#D97706"
        )

    with col4:
        metric_card(
            "Low Risk",
            low_risk,
            "🟢",
            "#16A34A"
        )

    st.divider()
    # ... rest of your dashboard code unchanged ...
