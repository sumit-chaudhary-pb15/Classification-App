# necessary imports
import pandas as pd
import streamlit as st

# importing pages
from get_home_page import get_home_page
from get_raw_data_page import get_raw_data_page
from get_eda_page import get_eda_page
from get_model_page import get_model_page
from get_predictions_page import get_predictions_page


st.title("Flower species prediction AI/ML application")

pages = ["home", "view_raw_dataset", "exploratory_data_analysis", "model_development", "model_predictions"]
page = st.sidebar.selectbox("NAVIGATION", pages)

# Loading raw dataset
iris_data = pd.read_csv("iris_dataset.csv")

# Page Specific functionalities
if page == "home":
    get_home_page()
elif page == "view_raw_dataset":
    get_raw_data_page(iris_data)
elif page == "exploratory_data_analysis":
    get_eda_page(iris_data)
elif page == "model_development":
    get_model_page(iris_data)
elif page == "model_predictions":
    get_predictions_page(iris_data)
else:
    print(f"this {page} is not defined")


