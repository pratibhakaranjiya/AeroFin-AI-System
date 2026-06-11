# 1. Write the complete website code into a file named 'app.py'
with open('app.py', 'w') as f:
    f.write('''
import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

# 2. Set up the Website Title and Design
st.title("🛸 AeroFin-AI-System: Drone Risk Predictor")
st.write("Enter the drone telemetry data below to check if it is Critical or Safe.")

# 3. Create Input Boxes for the 5 Drone Features
temp = st.number_input("Engine Temperature (°C)", min_value=50.0, max_value=400.0, value=150.0)
battery = st.number_input("Battery Level (%)", min_value=10.0, max_value=100.0, value=80.0)
speed = st.number_input("Speed (km/h)", min_value=10.0, max_value=150.0, value=60.0)
radiation = st.number_input("Space Radiation (rad)", min_value=0.0, max_value=10.0, value=2.0)
fuel = st.number_input("Fuel Level (%)", min_value=5.0, max_value=100.0, value=75.0)

# 4. Create a "Check Status" Button
if st.button("Predict Drone Status"):
    # Load our saved AI brain
    model = tf.keras.models.load_model('aerofin_drone_model.h5')
    
    # Arrange the inputs into an array
    input_data = np.array([[temp, battery, speed, radiation, fuel]])
    
    # Simple manual scaling to match model requirement
    prediction = model.predict(input_data)
    
    # 5. Show Final Result based on AI Score
    st.subheader("=== AI DECISION ===")
    if prediction[0][0] > 0.5:
        st.error(f"🔴 CRITICAL STATUS! Risk Score: {prediction[0][0]:.2f}")
    else:
        st.success(f"🟢 SAFE STATUS. Risk Score: {prediction[0][0]:.2f}")
''')

print("Website script 'app.py' created successfully!")
