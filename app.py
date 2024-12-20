import streamlit as st
import numpy as np
import requests

# Load the trained model (optional in this case, since we'll use FastAPI for prediction)
# model = joblib.load('Iris-model.pkl') 

# Set up FastAPI endpoint URL (make sure FastAPI is running)
API_URL = "http://52.200.221.168:8000/predict"  # Replace with the actual URL if it's running elsewhere

# Define the Streamlit interface
st.title("Iris Flower Species Prediction")
st.write("Enter the following details about the Iris flower:")

# Input fields for the features
# Input sliders
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0, 0.1)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 5.0, 3.0, 0.1)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 3.5, 0.1)
petal_width = st.slider("Petal Width (cm)", 0.1, 3.0, 1.0, 0.1)

# Button to trigger prediction
if st.button("Predict"):
    # Create the input data in the format expected by the API
    input_data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    # Send a POST request to the FastAPI endpoint
    try:
        response = requests.post(API_URL, json=input_data)
        response.raise_for_status()  # Raise an exception for 4xx/5xx responses
        
        # Parse the prediction result
        predicted_species = response.json()
        
        # Display the predicted species
        st.success(predicted_species)
    
    except requests.exceptions.RequestException as e:
        st.error(f"Error occurred: {e}")
