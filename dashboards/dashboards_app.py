import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Gym Dashboard")

data = pd.read_csv("data/members.csv")

st.subheader("Total Members")
st.metric(label="Count", value=data['member_id'].nunique())

st.subheader("Gender Distribution")
fig, ax = plt.subplots()
data['gender'].value_counts().plot(kind='bar', ax=ax)
st.pyplot(fig)
