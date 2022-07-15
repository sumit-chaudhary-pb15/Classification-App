import streamlit as st


def get_raw_data_page(iris_data):
    st.header("View Raw Dataset")
    st.subheader("Link to download the dataset")
    st.markdown("""https://gist.github.com/Thanatoz-1/9e7fdfb8189f0cdf5d73a494e4a6392a""")
    st.subheader("Raw data table")
    # Slider with minimum value of 0 and maximum value of 150
    data_points = st.slider("Number of rows to see in table:", 0, len(iris_data), 5)
    st.write(iris_data.head(data_points))