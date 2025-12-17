import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
st.set_page_config(
    page_title="System Anomaly Detection",
    layout="wide"
)
st.title("System & Log Anomaly Detection Dashboard")
st.sidebar.header("System Metrics Input")
cpu = st.sidebar.slider("CPU Usage (%)", 0.0, 100.0, 30.0)
memory = st.sidebar.slider("Memory Usage (%)", 0.0, 100.0, 40.0)
disk_io = st.sidebar.slider("Disk I/O (MB/s)", 0.0, 1000.0, 200.0)
network = st.sidebar.slider("Network Traffic (MB/s)", 0.0, 1000.0, 150.0)

np.random.seed(42)
data = pd.DataFrame({
    "cpu": np.random.normal(30, 10, 200),
    "memory": np.random.normal(60, 10, 200),
    "disk_io": np.random.normal(320, 80, 200),
    "network": np.random.normal(225, 70, 200)
})
model = IsolationForest(
    contamination=0.03,
    random_state=40
)
model.fit(data)
input_data = np.array([[cpu, memory, disk_io, network]])
prediction = model.predict(input_data)

st.subheader("Current System Status")

col1, col2, col3, col4 = st.columns(4)
col1.metric("CPU", cpu)
col2.metric("Memory", memory)
col3.metric("Disk I/O", disk_io)
col4.metric("Network", network)

if prediction[0] == -1:
    st.error("Anomaly Detected!System behavior is abnormal.")
else:
    st.success("System is operating normally.")

st.subheader("Historical Metrics Overview")
st.line_chart(data)
st.subheader("Example Log Messages")
logs = [
    "INFO: CPU usage normal",
    "WARNING: Disk I/O spike detected",
    "ERROR: Memory threshold exceeded",
    "INFO: Network traffic stable"
]

st.code("\n".join(logs), language="text")

