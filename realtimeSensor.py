import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time

st.title("📡 Real-Time IoT Sensor Dashboard")

# Simulated IoT sensor data
def get_sensor_data():
    return {
        "Timestamp": pd.Timestamp.now(),
        "Temperature (°C)": np.random.uniform(20, 35),
        "Humidity (%)": np.random.uniform(30, 70),
        "Pressure (hPa)": np.random.uniform(900, 1100),
    }

# Initialize session state for data storage
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Timestamp", "Temperature (°C)", "Humidity (%)", "Pressure (hPa)"])

# Live data update
placeholder = st.empty()

while True:
    new_data = get_sensor_data()
    st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([new_data])], ignore_index=True)

    with placeholder.container():
        st.subheader("📊 Sensor Data")
        st.dataframe(st.session_state.data.tail(10))  # Show last 10 readings

        # Line charts
        fig_temp = px.line(st.session_state.data, x="Timestamp", y="Temperature (°C)", title="Temperature Over Time")
        fig_humidity = px.line(st.session_state.data, x="Timestamp", y="Humidity (%)", title="Humidity Over Time")
        fig_pressure = px.line(st.session_state.data, x="Timestamp", y="Pressure (hPa)", title="Pressure Over Time")

        st.plotly_chart(fig_temp, use_container_width=True)
        st.plotly_chart(fig_humidity, use_container_width=True)
        st.plotly_chart(fig_pressure, use_container_width=True)

    time.sleep(2)  # Updates every 2 seconds
