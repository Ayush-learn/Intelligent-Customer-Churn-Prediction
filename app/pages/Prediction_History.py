import streamlit as st
import pandas as pd
from pathlib import Path
from pathlib import Path

css_file = Path("assets/style.css")

with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.set_page_config(page_title="Prediction History")

st.title("📜 Prediction History")

LOG_FILE=Path("prediction_logs.csv")

if LOG_FILE.exists():

    df=pd.read_csv(LOG_FILE)

    search=st.text_input("🔍 Search")

    if search:
        df=df[df.astype(str).apply(lambda x:x.str.contains(search,case=False)).any(axis=1)]

    st.dataframe(df,use_container_width=True)

    csv=df.to_csv(index=False)

    st.download_button(
        "⬇ Download CSV",
        csv,
        "prediction_history.csv",
        "text/csv"
    )

else:

    st.info("No predictions yet.")