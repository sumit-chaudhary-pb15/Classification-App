import pickle
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix
from constants import flower_mapping

class_names = flower_mapping.keys()


def visualize_results(model, x_test, y_test):
    # get accuracy and confusion matrix
    accuracy = model.score(x_test, y_test)
    y_pred = model.predict(x_test)
    st.write("Accuracy ", accuracy.round(2))
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.subheader("Confusion Matrix")
    plot_confusion_matrix(model, x_test, y_test, display_labels=class_names)
    st.pyplot()


def get_model_page(iris_data):
    st.header("Model development")

    # Assigning unique ID to different classes in target column
    iris_data['target'] = iris_data['target'].map({'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2})

    # Extracting feature and target space
    X = iris_data.iloc[:, :-1]
    y = iris_data.iloc[:, -1]

    # Slitting dataset into training and testing dataset
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    classifiers = ['logistic_regression', 'random_forest_classifier']
    # Create a drop-down to select a model to classification
    classifier = st.selectbox("Choose classifier", options=classifiers)

    # model development
    if classifier == 'logistic_regression':
        st.markdown("Model hyperparameters")
        # input parameters for the model
        C = st.number_input("C (Regularization parameter)", 0.01, 10.0, step=0.005, key='C_LR')
        max_iter = st.slider("Maximum number of iterations", 100, 500, key='max_iter')

        # train the logistic regression model with selected parameters
        if st.button("Train", key='classify'):
            st.subheader("Logistic Regression Results")
            model = LogisticRegression(C=C, max_iter=max_iter)
            model.fit(x_train, y_train)
            visualize_results(model, x_test, y_test)
            pickle_out = open('logistic_regression.pkl', "wb")
            pickle.dump(model, pickle_out)
            pickle_out.close()

    if classifier == 'random_forest_classifier':
        st.markdown("Model hyperparameters")
        n_estimators = st.number_input("The number of trees in the forest", 100, 5000, step=10,
                                       key='n_estimators')
        max_depth = st.number_input("The maximum depth of the tree", 1, 20, step=1, key='max_depth')
        bootstrap = st.radio("Bootstrap samples when building trees", ('True', 'False'), key='bootstrap')

        # train the random forest model with selected parameters
        if st.button("Train", key='classify'):
            st.subheader("")
            model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, bootstrap=bootstrap,
                                           n_jobs=-1)
            model.fit(x_train, y_train)
            model.fit(x_train, y_train)
            visualize_results(model, x_test, y_test)
            pickle_out = open('random_forest_classifier.pkl', "wb")
            pickle.dump(model, pickle_out)
            pickle_out.close()
