import streamlit as st
import pickle5 as pickle
import pandas as pd
import plotly.graph_objects as go
import numpy as np

def load_clean_data():
    data = pd.read_csv("data/data.csv")
    data = data.drop(['Unnamed: 32', 'id'], axis=1)
    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})
    return data

def configure_sidebar():
    st.sidebar.header("Nuclei Measurements")

    data = load_clean_data()

    slider_labels = [
        ("Radius (mean)", "radius_mean"),
        # ... (list of other features)
        ("Fractal dimension (worst)", "fractal_dimension_worst"),
    ]

    input_dict = {}

    for label, key in slider_labels:
        input_dict[key] = st.sidebar.slider(
            label,
            min_value=float(0),
            max_value=float(data[key].max()),
            value=float(data[key].mean())
        )

    return input_dict

def scale_input_values(input_dict):
    data = load_clean_data()
    X = data.drop(['diagnosis'], axis=1)
    scaled_dict = {}

    for key, value in input_dict.items():
        max_val = X[key].max()
        min_val = X[key].min()
        scaled_value = (value - min_val) / (max_val - min_val)
        scaled_dict[key] = scaled_value

    return scaled_dict

def generate_radar_chart(scaled_input_data):
    categories = ['Radius', 'Texture', 'Perimeter', 'Area',
                  'Smoothness', 'Compactness',
                  'Concavity', 'Concave Points',
                  'Symmetry', 'Fractal Dimension']

    fig = go.Figure()

    for chart_type in ['mean', 'se', 'worst']:
        radar_data = [scaled_input_data[f'{feature}_{chart_type}'] for feature in categories]
        fig.add_trace(go.Scatterpolar(
            r=radar_data,
            theta=categories,
            fill='toself',
            name=f'{chart_type.capitalize()} Value'
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]
            )),
        showlegend=True
    )

    return fig

def display_predictions(scaled_input_data):
    model = pickle.load(open("model/model.pkl", "rb"))
    scaler = pickle.load(open("model/scaler.pkl", "rb"))

    input_array = np.array(list(scaled_input_data.values())).reshape(1, -1)
    input_array_scaled = scaler.transform(input_array)

    prediction = model.predict(input_array_scaled)

    st.subheader("Cell Cluster Prediction")
    st.write("The cell cluster is:")

    if prediction[0] == 0:
        st.write("<span class='diagnosis benign'>Benign</span>", unsafe_allow_html=True)
    else:
        st.write("<span class='diagnosis malicious'>Malicious</span>", unsafe_allow_html=True)

    st.write("Probability of being benign: ", model.predict_proba(input_array_scaled)[0][0])
    st.write("Probability of being malicious: ", model.predict_proba(input_array_scaled)[0][1])

    st.write("This app can assist medical professionals in making a diagnosis, but should not be used as a substitute for a professional diagnosis.")

def main():
    st.set_page_config(
        page_title="Cancer Predictor",
        page_icon=":female-doctor:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    with open("assets/style.css") as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

    input_data = configure_sidebar()

    with st.container():
        st.title("Cancer Predictor")
        st.write("Please connect this app to your cytology lab to help diagnose cancer from your tissue sample. This app predicts using a machine learning model whether a cell cluster is benign or malignant based on the measurements it receives from your cytosis lab. You can also update the measurements by hand using the sliders in the sidebar.")

    col1, col2 = st.columns([4, 1])

    with col1:
        radar_chart = generate_radar_chart(input_data)
        st.plotly_chart(radar_chart)
    with col2:
        display_predictions(input_data)

if __name__ == '__main__':
    main()
