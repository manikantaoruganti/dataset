import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="BBCAS - Continuous Authentication")

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Behavior-Based Continuous Authentication")

st.write("### Enter Live Behavioral Data")

tap_pressure = st.slider("Tap Pressure", 0.0, 1.0, 0.5)
swipe_speed = st.slider("Swipe Speed", 0.0, 1.0, 0.6)
hold_time = st.slider("Hold Time", 0.0, 1.0, 0.3)
typing_speed = st.slider("Typing Speed", 10, 100, 50)
device_tilt = st.slider("Device Tilt (°)", 0, 15, 5)
location_distance = st.slider("Location Distance (km)", 0, 10, 3)

test_data = pd.DataFrame([[
    tap_pressure, swipe_speed, hold_time,
    typing_speed, device_tilt, location_distance
]], columns=['tap_pressure','swipe_speed','hold_time','typing_speed','device_tilt','location_distance'])

if st.button("Check Anomaly"):
    prediction = model.predict(test_data)
    if prediction[0] == -1:
        st.error("Anomaly Detected ⚠")
    else:
        st.success("Normal Behavior ✅")
      
