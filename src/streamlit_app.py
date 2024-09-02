import streamlit as st
import requests
import pandas as pd

# Set up FastAPI endpoints
UPLOAD_URL = "http://localhost:6000/upload_data/"
GENERATE_URL = "http://localhost:6000/generate_synthetic_data/"

def upload_data(file):
    with st.spinner("Uploading data..."):
        files = {'file': file.getvalue()}
        response = requests.post(UPLOAD_URL, files=files)
        if response.status_code == 200:
            st.success("Data uploaded successfully!")
        else:
            st.error("Failed to upload data.")
            st.write(response.text)

def generate_data(num_rows, model_type):
    with st.spinner("Generating synthetic data..."):
        data = {"num_rows": num_rows, "model_type": model_type}
        response = requests.post(GENERATE_URL, json=data)
        if response.status_code == 200:
            result = response.json()
            st.success("Synthetic data generated successfully!")
            st.write(f"**Evaluation Score:** {result['evaluation_score']:.2f}")
            st.dataframe(pd.DataFrame(result['generated_data']))
        else:
            st.error("Failed to generate synthetic data.")
            st.write(response.text)


st.title("Synthetic Data Generator")

# Model type selection
model_type = st.selectbox(
    "Select Model Type",
    ("Gaussian", "CTGAN", "FAST_ML")
)

# Number of rows input
num_rows = st.number_input("Number of Rows", min_value=1, value=1000)

# File upload
uploaded_file = st.file_uploader("Upload CSV Data", type=["csv"])

# Buttons
if st.button("Upload Data"):
    if uploaded_file is not None:
        upload_data(uploaded_file)
    else:
        st.warning("Please upload a CSV file.")

if st.button("Generate Synthetic Data"):
    if uploaded_file is not None:
        upload_data(uploaded_file)  
        generate_data(num_rows, model_type)  
    else:
        st.warning("Please upload a CSV file first.")