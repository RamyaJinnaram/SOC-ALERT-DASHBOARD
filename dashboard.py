import streamlit as st
from detector import detect_threats

st.title("🛡️ SOC Alert Dashboard")

st.write("Monitoring system logs for suspicious activity...")

alerts = detect_threats("logs.txt")

st.subheader("🚨 Alerts")

if alerts:
for alert in alerts:
st.error(alert)
else:s
st.success("No suspicious activity detected")
