import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
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

        # Line charts with Altair
        temp_chart = alt.Chart(st.session_state.data).mark_line().encode(
            x='Timestamp:T',
            y='Temperature (°C):Q'
        ).properties(title="Temperature Over Time")

        humidity_chart = alt.Chart(st.session_state.data).mark_line().encode(
            x='Timestamp:T',
            y='Humidity (%):Q'
        ).properties(title="Humidity Over Time")

        pressure_chart = alt.Chart(st.session_state.data).mark_line().encode(
            x='Timestamp:T',
            y='Pressure (hPa):Q'
        ).properties(title="Pressure Over Time")

        st.altair_chart(temp_chart, use_container_width=True)
        st.altair_chart(humidity_chart, use_container_width=True)
        st.altair_chart(pressure_chart, use_container_width=True)

    time.sleep(2)  # Updates every 2 seconds
