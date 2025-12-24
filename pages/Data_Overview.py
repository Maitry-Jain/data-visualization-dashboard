import streamlit as st
import pandas as pd

st.title("Data Overview")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.session_state["df"] = df

    st.subheader("Dataset Preview")
    st.dataframe(df)

    st.subheader("Dataset Information")
    col1, col2 = st.columns(2)

    with col1:
        st.write("Rows:", df.shape[0])
        st.write("Columns:", df.shape[1])

    with col2:
        st.write("Column Names:")
        st.write(list(df.columns))
else:
    st.warning("Please upload a CSV file.")
