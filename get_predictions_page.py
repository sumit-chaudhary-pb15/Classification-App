import pickle
import streamlit as st
from constants import flower_mapping


def get_predictions_page(iris_data):
    # Create a drop-down to select a model for prediction
    classifiers = ['logistic_regression', 'random_forest_classifier']
    classifier = st.selectbox("Choose classifier for predictions", options=classifiers)

    # Create slider to take user input requirements
    st.write("Please insert values, to get Iris class prediction")
    sepal_length = st.slider('SepalLengthCm:', 2.0, 6.0)
    sepal_width = st.slider('SepalWidthCm:', 0.0, 5.0)
    petal_length = st.slider('PetalLengthCm', 0.0, 3.0)
    petal_width = st.slider('SkiPetalWidthCm:', 0.0, 2.0)

    # Predict type of flower basis model selected for prediction
    if classifier == 'logistic_regression':
        lr_pickle_in = open('logistic_regression.pkl', 'rb')
        lr_pkl = pickle.load(lr_pickle_in)
        if st.button("Predict"):
            result = lr_pkl.predict([[sepal_length, sepal_width, petal_length, petal_width]])
            st.success('The output is {}'.format(str(result[0])))
    elif classifier == 'random_forest_classifier':
        rfr_pickle_in = open('logistic_regression.pkl', 'rb')
        rfr_pkl = pickle.load(rfr_pickle_in)
        if st.button("Predict"):
            result = rfr_pkl.predict([[sepal_length, sepal_width, petal_length, petal_width]])
            st.success('The output is {}'.format(str(result[0])))

    st.markdown("*****")
    st.write("Mapping dictionary classes to IDs")
    st.write(flower_mapping)
