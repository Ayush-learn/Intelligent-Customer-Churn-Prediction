import streamlit as st


def show_recommendations(recommendations):

    st.subheader("💡 Business Recommendations")

    for item in recommendations:
        st.success(item)