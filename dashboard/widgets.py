import streamlit as st


def metric_cards(probability, risk):

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "📈 Churn Probability",
            f"{probability * 100:.2f}%"
        )

    with col2:
        st.metric(
            "⚠ Risk Level",
            risk
        )

    st.progress(float(probability))


def metric_card(title,value,icon,color):

    st.markdown(f"""
    <div style="
        background:linear-gradient(135deg,{color},#111827);
        padding:25px;
        border-radius:18px;
        color:white;
        box-shadow:0 10px 25px rgba(0,0,0,.35);
        border:1px solid rgba(255,255,255,.05);
    ">

        <div style="font-size:35px;">
            {icon}
        </div>

        <div style="
            font-size:17px;
            color:#CBD5E1;
            margin-top:10px;
        ">
            {title}
        </div>

        <div style="
            font-size:38px;
            font-weight:700;
            margin-top:5px;
        ">
            {value}
        </div>

    </div>
    """,unsafe_allow_html=True)
    
