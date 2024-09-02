# SDV Sample Project

This project is a sample implementation of a Synthetic Data Vault (SDV) application with a user-friendly interface built using Streamlit. The application allows users to generate synthetic data using various models and perform time series forecasting on uploaded datasets.

## Features

- **Data Upload**: Upload your dataset in CSV format to begin generating synthetic data.
- **Model Selection**: Choose between different synthetic data generation models:
  - **GaussianCopula**
  - **FastML**
  - **CTGAN**
- **Synthetic Data Generation**: Generate synthetic data based on the model selected. The generated data mimics the structure and properties of the input data.
- **Time Series Forecasting**:
  - Enable the checkbox to open the time series forecasting interface.
  - Input the necessary information such as context columns, sequence key, and other relevant parameters.
  - Perform forecasting on the uploaded dataset.
