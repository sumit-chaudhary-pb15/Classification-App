import streamlit as st


def get_home_page():
    st.header("Home")
    st.subheader("Project Description")
    st.markdown("""
        Iris dataset is a multi-class classification problem in machine learning.
        The iris dataset description:
        - Number of rows: 150
        - Number of columns: 5
        - Feature columns
            - sepal length in cm
            - sepal width in cm
            - petal length in cm
            - petal width in cm
        - One target column with three columns
            - Iris-Setosa
            - Iris-Versicolour
            - Iris-Virginica
    """)