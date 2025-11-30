# Weather Data Analysis Dashboard

Interactive Streamlit dashboard to visualize and analyze weather/climate datasets.

## Features

- Upload your CSV dataset
- View dataset preview and summary statistics
- Plot daily trends for weather variables
- Seasonal decomposition (trend, seasonal, residual)
- Rainfall distribution histogram
- Correlation heatmap

## How to Run

1. Clone the repository:

```bash
git clone <your-repo-url>
Install dependencies:

bash
pip install -r requirements.txt
Run the Streamlit app:

bash
streamlit run app.py
Upload a weather CSV file with columns like:
date, temp_max, temp_min, temp_avg, precip_mm, humidity, wind_speed, pressure

yaml

---

# **4️⃣ `data/weather_data.csv`**  

- Place your weather dataset here.
- Example CSV columns:
date,temp_max,temp_min,temp_avg,precip_mm,humidity,wind_speed,pressure
2018-01-01,28.1,18.3,23.2,0.0,56,10.2,1012.8
2018-01-02,29.3,19.0,24.1,5.3,62,8.4,1011.9

