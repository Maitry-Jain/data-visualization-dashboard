import streamlit as st

st.title(" Data Cleaning")

# ---------- Check Data ----------
if "df" not in st.session_state:
    st.warning("Upload data first.")
    st.stop()

df = st.session_state["df"]

# ---------- Missing Values Summary ----------
st.subheader(" Missing Values (Before Cleaning)")
st.dataframe(df.isna().sum())

# ---------- Cleaning Method ----------
method = st.selectbox(
    "Choose Cleaning Method",
    ["None", "Drop Rows", "Fill Numeric with Mean", "Fill Numeric with Median"]
)

cleaned_df = df.copy()  

if method == "Drop Rows":
    cleaned_df = cleaned_df.dropna()

elif method == "Fill Numeric with Mean":
    for col in cleaned_df.select_dtypes(include=["int64", "float64"]).columns:
        cleaned_df[col] = cleaned_df[col].fillna(cleaned_df[col].mean())

elif method == "Fill Numeric with Median":
    for col in cleaned_df.select_dtypes(include=["int64", "float64"]).columns:
        cleaned_df[col] = cleaned_df[col].fillna(cleaned_df[col].median())

# ---------- Show Cleaned Dataset ----------
st.subheader("Cleaned Dataset")
st.dataframe(cleaned_df)

# ---------- Update Session State ----------
st.session_state["df"] = cleaned_df
st.success("Data cleaned successfully!")
st.subheader(" Download Cleaned Data")

csv = cleaned_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Cleaned CSV",
    data=csv,
    file_name="cleaned_data.csv",
    mime="text/csv"
)