import streamlit as st
import random
import pandas as pd
import time
import requests

st.set_page_config(page_title="Smart Agriculture AI System", layout="wide")

st.title("🌱 Smart Agriculture AI Dashboard")

menu = st.sidebar.selectbox("Menu", ["Dashboard", "Weather", "AI Crop Advisor", "Add Field", "View Fields"])

# Session storage
if "fields" not in st.session_state:
    st.session_state.fields = []

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Moisture", "Temperature", "Humidity", "pH"])

# -------- Dashboard --------
if menu == "Dashboard":

    st.subheader("📊 Live Sensor Monitoring")

    col1, col2, col3, col4 = st.columns(4)

    moisture = random.randint(30, 80)
    temperature = random.randint(20, 40)
    humidity = random.randint(40, 90)
    ph = round(random.uniform(5.5, 7.5), 2)

    col1.metric("Moisture", moisture)
    col2.metric("Temperature", temperature)
    col3.metric("Humidity", humidity)
    col4.metric("pH", ph)

    new_data = pd.DataFrame({
        "Moisture": [moisture],
        "Temperature": [temperature],
        "Humidity": [humidity],
        "pH": [ph]
    })

    st.session_state.data = pd.concat([st.session_state.data, new_data]).tail(20)

    st.subheader("📈 Sensor Trends")
    st.line_chart(st.session_state.data)

    st.subheader("💧 Irrigation")
    if moisture < 50:
        st.error("Irrigation ON")
    else:
        st.success("Irrigation OFF")

    st.subheader("⚠️ Alerts")
    if temperature > 35:
        st.warning("High Temperature!")
    if humidity < 50:
        st.warning("Low Humidity!")

    time.sleep(2)
    st.rerun()

# -------- Weather --------
elif menu == "Weather":

    st.subheader("🌦️ Weather Information")

    if st.button("Get Weather"):

        temp = random.randint(20, 40)
        humidity = random.randint(40, 90)
        weather = random.choice(["Sunny ☀️", "Cloudy ☁️", "Rainy 🌧️"])

        st.success(f"Temperature: {temp}°C")
        st.info(f"Humidity: {humidity}%")
        st.write(f"Condition: {weather}")

# -------- AI Crop Advisor --------
elif menu == "AI Crop Advisor":

    st.subheader("🤖 AI Crop Recommendation")

    soil = st.selectbox("Soil Type", ["Loamy", "Sandy", "Clay"])
    water = st.selectbox("Water Availability", ["Low", "Medium", "High"])
    season = st.selectbox("Season", ["Summer", "Winter", "Rainy"])

    if st.button("Predict Crop"):

        if soil == "Loamy" and water == "Medium":
            crop = "Wheat 🌾"
        elif soil == "Sandy" and water == "Low":
            crop = "Millets 🌱"
        elif season == "Rainy":
            crop = "Rice 🌾"
        else:
            crop = "Maize 🌽"

        st.success(f"Recommended Crop: {crop}")

# -------- Add Field --------
elif menu == "Add Field":

    name = st.text_input("Field Name")
    crop = st.text_input("Crop Type")

    if st.button("Add Field"):
        if name and crop:
            st.session_state.fields.append({"name": name, "crop": crop})
            st.success("Field Added!")

# -------- View Fields --------
elif menu == "View Fields":

    if len(st.session_state.fields) == 0:
        st.info("No fields yet")
    else:
        for f in st.session_state.fields:
            st.write(f"🌱 {f['name']} | Crop: {f['crop']}")