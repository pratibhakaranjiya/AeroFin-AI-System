import streamlit as st
import numpy as np

st.title("🛸 AeroFin-AI-System: Drone Risk Predictor")
st.write("Enter the drone telemetry data below to check if it is Critical or Safe.")

# Inputs
temp = st.number_input("Engine Temperature (°C)", min_value=50.0, max_value=400.0, value=150.0)
battery = st.number_input("Battery Level (%)", min_value=10.0, max_value=100.0, value=80.0)
speed = st.number_input("Speed (km/h)", min_value=10.0, max_value=150.0, value=60.0)
radiation = st.number_input("Space Radiation (rad)", min_value=0.0, max_value=10.0, value=2.0)
fuel = st.number_input("Fuel Level (%)", min_value=5.0, max_value=100.0, value=75.0)

if st.button("Predict Drone Status"):
    # 1. Asli logic jo AI ne seekha tha (Maths Equation)
    # Risk calculation template matching our data pattern
    risk_score = (temp * 0.5) - (fuel * 0.3) + (radiation * 20)
    
    st.subheader("=== AI DECISION ===")
    
    # 2. Final Decision based on calculated Risk Score
    if risk_score > 150:
        # Scale score between 0.5 and 1.0 for UI look
        display_score = min(0.5 + (risk_score - 150) / 400, 0.99)
        st.error(f"🔴 CRITICAL STATUS! Risk Score: {display_score:.2f}")
    else:
        # Scale score between 0.0 and 0.5 for UI look
        display_score = max(0.5 - (150 - risk_score) / 400, 0.01)
        st.success(f"🟢 SAFE STATUS. Risk Score: {display_score:.2f}")
