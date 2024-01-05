# Breast Cancer Diagnosis Predictor

## Overview

The **Breast Cancer Diagnosis Predictor** is a sophisticated machine learning tool developed to aid healthcare professionals in the crucial task of diagnosing breast cancer. Utilizing an advanced algorithm, the application analyzes a set of measurements to predict whether a given breast mass is benign or malignant. The feature-rich application includes a visually informative radar chart, offering a detailed representation of the input data. Additionally, the app provides the predicted diagnosis and the corresponding probability of the mass being benign or malignant.

The app is versatile, allowing users to input measurements manually or seamlessly connect to a cytology lab, streamlining the process of obtaining data directly from laboratory machines. It's important to note that while the application is an invaluable aid in the diagnostic process, the connection to the laboratory machine is an external component and not an inherent part of the app itself.

This application was developed as part of a machine learning exercise utilizing the publicly available [Breast Cancer Wisconsin (Diagnostic) Data Set](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data). However, it's essential to recognize that this dataset may not be considered reliable for professional diagnosis. The project primarily serves educational purposes within the domain of machine learning.

For a live experience, the application is accessible on the [Streamlit Community Cloud](https://alejandro-ao-streamlit-cancer-predict-appmain-uitjy1.streamlit.app/).

## Installation

To run the **Breast Cancer Diagnosis Predictor** locally, ensure you have Python 3.6 or a higher version installed. Then, install the required packages by executing the following command:

```bash
pip install -r requirements.txt

## Usage

### Running Locally

1. Ensure you have Python 3.6 or a higher version installed on your machine.

2. Install the required packages by running the following command in your terminal or command prompt:

    ```bash
    pip install -r requirements.txt
    ```

    This will install all the necessary dependencies, including Streamlit, OpenCV, and scikit-image.

3. Start the **Breast Cancer Diagnosis Predictor** locally by executing the following command:

    ```bash
    streamlit run app.py
    ```

    This will launch the application in your default web browser.

4. Upload Cell Images for Analysis:

    - Once the application is running, use the provided interface to upload cell images that you want to analyze.

5. Fine-Tune Settings:

    - Adjust various settings to customize the analysis according to your requirements.

6. View Results:

    - The application will provide a visual representation of the analysis using a radar chart.

7. Export Measurements:

    - If satisfied with the results, you can export the measurements to a CSV file for further in-depth analysis.

### Live Deployment

For a live experience, you can access the application on the [Streamlit Community Cloud](https://alejandro-ao-streamlit-cancer-predict-appmain-uitjy1.streamlit.app/).

**Note:** Ensure that your internet connection is stable for live deployment.

**Important:** The Breast Cancer Diagnosis Predictor is designed for educational purposes within the field of machine learning. The provided dataset may not be considered reliable for professional diagnosis. Always consult with a medical professional for accurate diagnostic assessments.

