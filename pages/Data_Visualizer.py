import streamlit as st
import matplotlib.pyplot as plt

st.title(" Visualizations")

if "df" not in st.session_state:
    st.warning("Upload data first from Data Overview page.")
    st.stop()

df = st.session_state["df"]

chart_type = st.sidebar.selectbox(
    "Select Chart Type",
    ["Bar Chart", "Line Chart", "Scatter Plot", "Pie Chart"]
)

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
all_cols = df.columns

if chart_type in ["Bar Chart", "Line Chart", "Scatter Plot"]:
    x_col = st.sidebar.selectbox("X-axis", all_cols)
    y_col = st.sidebar.selectbox("Y-axis", numeric_cols)

    st.subheader(f"{chart_type}: {y_col} vs {x_col}")

    if chart_type == "Bar Chart":
        st.bar_chart(df[[x_col, y_col]].set_index(x_col),x_label=x_col,y_label=y_col)

    elif chart_type == "Line Chart":
        st.line_chart(df[[x_col, y_col]].set_index(x_col),x_label=x_col,y_label=y_col)

    elif chart_type == "Scatter Plot":
        st.scatter_chart(df, x=x_col, y=y_col,x_label=x_col,y_label=y_col)

elif chart_type == "Pie Chart":
    cat_cols = df.select_dtypes(include=["object", "category"]).columns

    if len(cat_cols) == 0:
        st.warning("No categorical columns found.")
    else:
        col = st.sidebar.selectbox("Select Column", cat_cols)
        values = df[col].value_counts()

        fig, ax = plt.subplots()
        ax.pie(values, labels=values.index, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")
        st.pyplot(fig)
