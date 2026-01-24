import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Mumbai Climate Dashboard",
    layout="wide"
)

st.title("🌦️ Mumbai Climate Dashboard")
st.markdown("Historical climate analysis for **Mumbai city**")

# -----------------------------
# Load data
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/climate_dashboard_base.csv")

climate_df = load_data()

# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.header("Filters")
st.sidebar.caption("Scope: Mumbai city only")

years = sorted(climate_df["Year"].unique())
seasons = sorted(climate_df["Season"].unique())

year_filter = st.sidebar.multiselect(
    "Select Year(s)",
    options=years,
    default=years
)

season_filter = st.sidebar.multiselect(
    "Select Season(s)",
    options=seasons,
    default=seasons
)

filtered_df = climate_df[
    (climate_df["Year"].isin(year_filter)) &
    (climate_df["Season"].isin(season_filter))
]

# -----------------------------
# KPIs
# -----------------------------
st.subheader("📊 Key Climate Indicators (Mumbai)")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Avg Max Temperature (°C)",
    round(filtered_df["Temp Max"].mean(), 2)
)

col2.metric(
    "Avg Rainfall (mm)",
    round(filtered_df["Rain"].mean(), 2)
)

col3.metric(
    "Avg Temperature Range (°C)",
    round(filtered_df["Temp_Range"].mean(), 2)
)

# -----------------------------
# Yearly Temperature Trend
# -----------------------------
st.subheader("📈 Yearly Average Maximum Temperature — Mumbai")

yearly_temp = (
    filtered_df.groupby("Year")["Temp Max"]
    .mean()
    .reset_index()
)

fig, ax = plt.subplots(figsize=(5,3))
ax.plot(yearly_temp["Year"], yearly_temp["Temp Max"], marker="o")
ax.set_xlabel("Year")
ax.set_ylabel("Avg Max Temp (°C)")
ax.set_title("Mumbai Yearly Temperature Trend")
plt.xticks(rotation=45)
st.pyplot(fig, use_container_width=False)

# -----------------------------
# Seasonal Rainfall
# -----------------------------
st.subheader("🌧️ Seasonal Rainfall Pattern — Mumbai")

seasonal_rain = (
    filtered_df.groupby("Season")["Rain"]
    .mean()
    .reset_index()
)

fig, ax = plt.subplots(figsize=(5,3))
ax.bar(seasonal_rain["Season"], seasonal_rain["Rain"])
ax.set_xlabel("Season")
ax.set_ylabel("Avg Rainfall (mm)")
ax.set_title("Mumbai Seasonal Rainfall Distribution")
st.pyplot(fig, use_container_width=False)

# -----------------------------
# Temperature Variability
# -----------------------------
st.subheader("🌡️ Temperature Variability Over Years — Mumbai")

temp_var = (
    filtered_df.groupby("Year")["Temp_Range"]
    .mean()
    .reset_index()
)

fig, ax = plt.subplots(figsize=(5,3))
ax.plot(temp_var["Year"], temp_var["Temp_Range"], marker="o")
ax.set_xlabel("Year")
ax.set_ylabel("Avg Temp Range (°C)")
ax.set_title("Mumbai Temperature Variability")
plt.xticks(rotation=45)
st.pyplot(fig, use_container_width=False)

# -----------------------------
# Notes
# -----------------------------
st.markdown("""
---
### 📌 Dashboard Notes
- Dataset is limited to **Mumbai city**
- All charts dynamically respond to filters
- Data cleaning & feature engineering done in Python (EDA phase)
- Streamlit used only for visualization & interaction
""")
