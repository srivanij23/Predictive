import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load('maintenance_model.pkl')

# Streamlit App
st.title('Predictive Maintenance System')

# Input fields for machine sensor data
temperature = st.number_input('Temperature (°C)', min_value=0, max_value=200, value=100)
vibration = st.number_input('Vibration (mm/s)', min_value=0.0, max_value=10.0, value=5.0)
pressure = st.number_input('Pressure (Bar)', min_value=0.0, max_value=100.0, value=50.0)
speed = st.number_input('Speed (RPM)', min_value=0, max_value=3000, value=1500)

# Button to predict
if st.button('Predict Maintenance Need'):
    # Prepare input data for prediction
    input_data = pd.DataFrame([[temperature, vibration, pressure, speed]], 
                              columns=['Temperature', 'Vibration', 'Pressure', 'Speed'])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    if prediction == 0:
        st.success('No Maintenance Required')
    else:
        st.warning('Maintenance Required')
