
import pandas as pd
import streamlit as st

st.title("ThreeSixty – Gym Analytics Dashboard")

st.sidebar.header("Filters")
date_min, date_max = st.sidebar.date_input("Date range", [])
channel = st.sidebar.multiselect("Channel", ["mobile_app", "web", "email", "kiosk"])

st.subheader("KPIs")
col1, col2, col3, col4 = st.columns(4)
col1.metric("DAU", "—")
col2.metric("Attendance Rate", "—")
col3.metric("No-show Rate", "—")
col4.metric("Avg Dwell (min)", "—")

st.subheader("Attendance Over Time")
st.line_chart(pd.DataFrame({"date": [], "attendance": []}).set_index("date"))

st.subheader("Coach Booking Rates")
st.bar_chart(pd.DataFrame({"coach": [], "rate": []}).set_index("coach"))

st.subheader("Usage Heatmap (Hour x Day)")
st.write("TODO: add heatmap from processed attendance.")

st.caption("Tip: Populate with processed CSVs or connect directly to PostgreSQL via SQLAlchemy.")
