import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

st.title("🛸 AeroFin-AI-System: Drone Risk Predictor")
st.write("Enter the drone telemetry data below to check if it is Critical or Safe.")

temp = st.number_input("Engine Temperature (°C)", min_value=50.0, max_value=400.0, value=150.0)
battery = st.number_input("Battery Level (%)", min_value=10.0, max_value=100.0, value=80.0)
speed = st.number_input("Speed (km/h)", min_value=10.0, max_value=150.0, value=60.0)
radiation = st.number_input("Space Radiation (rad)", min_value=0.0, max_value=10.0, value=2.0)
fuel = st.number_input("Fuel Level (%)", min_value=5.0, max_value=100.0, value=75.0)

if st.button("Predict Drone Status"):
    try:
        # Recreate the exact same brain architecture (structure)
        model = Sequential([
            Dense(32, activation='relu', input_shape=(5,)),
            Dropout(0.2),
            Dense(16, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        
        # Load the safe weights file into this structure
        model.load_weights('model_weights.weights.h5')
        
        raw_inputs = np.array([[temp, battery, speed, radiation, fuel]])
        scaled_inputs = (raw_inputs - np.array([225.0, 55.0, 80.0, 5.0, 52.5])) / np.array([101.0, 26.0, 40.0, 2.9, 27.4])
        
        prediction = model.predict(scaled_inputs)
        
        st.subheader("=== AI DECISION ===")
        if prediction[0][0] > 0.5:
            st.error(f"🔴 CRITICAL STATUS! Risk Score: {prediction[0][0]:.2f}")
        else:
            st.success(f"🟢 SAFE STATUS. Risk Score: {prediction[0][0]:.2f}")
            
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
