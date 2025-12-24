import streamlit as st

st.set_page_config(
    page_title="Data Visualization And Cleaning",
    layout="wide"
)

st.title(" Data Visualization & Cleaning Dashboard")
left, right = st.columns([2, 1])

with left:
    st.markdown("""
    ###  Project Overview
    This interactive dashboard allows users to upload CSV files,
    explore datasets, visualize trends, and clean missing values
    using intuitive controls.
    """)

    st.markdown("""
    ###  Features
    -  Upload and preview CSV datasets  
    -  Visualize data (Bar, Line, Scatter, Pie charts)  
    -  Handle missing values (drop / fill)  
    -  Analyze numerical relationships  
    -  Download cleaned datasets  
    """)

with right:
    st.info("""
     **How to Use**
    1. Go to **Data Overview**
    2. Upload your CSV file
    3. Explore visualizations
    4. Clean missing data
    5. Download cleaned file
    """)

# ---------- Footer ----------
st.success(" Use the sidebar to navigate between pages.")
st.caption("Built using Python & Streamlit")