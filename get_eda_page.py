import streamlit as st
import plotly.express as px


def get_scatter_plot(iris_data, feature_space):
    x_column = st.selectbox("Select x-axis column:", options=feature_space, index=0)
    y_column = st.selectbox("Select y-axis column:", options=feature_space, index=1)
    fig = px.scatter(iris_data, x=x_column, y=y_column, color='target')
    st.plotly_chart(fig, use_container_width=True)


def get_3d_plot(iris_data, feature_space):
    x_column = st.selectbox("Select x-axis column:", options=feature_space, index=0)
    y_column = st.selectbox("Select y-axis column:", options=feature_space, index=1)
    z_column = st.selectbox("Select z-axis column:", options=feature_space, index=1)
    fig = px.scatter_3d(iris_data, x=x_column, y=y_column, z=z_column, color='target')
    st.plotly_chart(fig, use_container_width=True)


def get_eda_page(iris_data):
    st.header("Exploratory data analysis")
    stats_expander = st.expander("Statistical analysis", expanded=False)
    with stats_expander:
        st.metric("Rows:", len(iris_data))
        st.markdown("*********")
        st.metric("Columns:", len(iris_data.columns))
        st.markdown("*********")
        st.markdown("Feature columns name are:")
        st.write(iris_data.columns.tolist()[0:4])     
        st.markdown("*********")
        st.markdown("Target column name is:")
        st.write(iris_data.columns.tolist()[-1])
        st.write(iris_data[iris_data.columns.tolist()[-1]].value_counts())
        st.markdown("*********")
        st.markdown("Statistical parameters")
        st.write(iris_data.describe())
        st.markdown("*********")
        
    visual_expander = st.expander("Data visualizations", expanded=False)
    with visual_expander:
        feature_space = iris_data.columns.tolist()[0:4]
        plots = ["SCATTER", "3D"]
        plot_name = st.selectbox("Select type of visualization", options=plots)
        if plot_name == "SCATTER":
            get_scatter_plot(iris_data, feature_space)
        elif plot_name == "3D":
            get_3d_plot(iris_data, feature_space)
        else:
            print(f"type of {plot_name} visualization is not supported")

        