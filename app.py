# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

st.set_page_config(page_title="Weather Dashboard", layout="wide")
st.title("🌤 Weather Data Analysis Dashboard")
st.write("Interactive dashboard for exploring climate/weather data.")

# --- Sidebar ---
st.sidebar.header("Upload Your Dataset")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# --- Load Data ---
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset loaded successfully!")
else:
    st.info("Upload a CSV file to get started.")
    st.stop()

# --- Basic Info ---
st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Summary Statistics")
st.write(df.describe())

# --- Preprocessing ---
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"])

# --- Weather Trends ---
st.subheader("📈 Daily Weather Trends")
weather_metric = st.selectbox(
    "Select a weather variable to visualize",
    options=[col for col in df.columns if df[col].dtype != 'object' and col != "date"]
)

fig_weather = px.line(df, x="date", y=weather_metric, title=f"{weather_metric} Over Time")
st.plotly_chart(fig_weather, use_container_width=True)

# --- Seasonal Decomposition ---
st.subheader("🔍 Seasonal Decomposition")
metric = st.selectbox("Choose metric for seasonal analysis", df.select_dtypes("number").columns, index=0)
df_sa = df.dropna(subset=[metric])

try:
    result = seasonal_decompose(df_sa[metric], model="additive", period=365)
    st.write("Trend Component")
    st.line_chart(result.trend)
    st.write("Seasonal Component")
    st.line_chart(result.seasonal)
    st.write("Residual Component")
    st.line_chart(result.resid)
except:
    st.warning("Seasonal decomposition requires at least one year of daily data.")

# --- Rainfall / Precipitation Distribution ---
if "precip_mm" in df.columns:
    st.subheader("🌧 Rainfall Distribution")
    fig_rain = px.histogram(df, x="precip_mm", nbins=40, title="Rainfall Distribution")
    st.plotly_chart(fig_rain, use_container_width=True)

# --- Correlation Heatmap ---
st.subheader("📊 Correlation Heatmap")
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
