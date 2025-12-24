import streamlit as st
import matplotlib.pyplot as plt

st.title(" Data Analysis")

if "df" not in st.session_state:
    st.warning("Upload data first.")
    st.stop()

df = st.session_state["df"]

st.subheader("Statistical Summary")
st.dataframe(df.describe())


