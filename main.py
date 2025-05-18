import streamlit as st
import pandas as pd

# Title of the dashboard
st.title("Solar Energy Dashboard")

# Dropdown to select country
country = st.selectbox("Select a country", ["Benin", "Sierra Leone", "Togo"])

# Load the correct dataset
df = pd.read_csv(f"data/{country.lower()}_clean.csv")

# Display the dataset preview
st.subheader("Dataset Overview")
st.write(df.head())

# Boxplot of Global Horizontal Irradiance (GHI)
st.subheader("Solar Irradiance Comparison")
st.boxplot(df["GHI"])

# Show summary statistics
st.subheader("Summary Statistics")
st.write(df.describe())

st.write("To run this app, use the command: `streamlit run app/main.py`")