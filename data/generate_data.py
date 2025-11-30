import pandas as pd
import numpy as np

# --- Parameters ---
start_date = "2020-01-01"
end_date = "2022-12-31"
dates = pd.date_range(start=start_date, end=end_date, freq="D")
n = len(dates)

# --- Generate synthetic weather values ---
np.random.seed(42)  # for reproducibility

# Temperatures (Celsius)
temp_avg = 15 + 10 * np.sin(2 * np.pi * dates.dayofyear / 365) + np.random.normal(0, 2, n)
temp_max = temp_avg + np.random.normal(5, 1.5, n)
temp_min = temp_avg - np.random.normal(5, 1.5, n)

# Precipitation (mm)
precip_mm = np.random.gamma(1.5, 2, n)
precip_mm[np.random.rand(n) < 0.7] = 0  # 70% days have no rain

# Other metrics
humidity = np.clip(50 + 30 * np.sin(2 * np.pi * dates.dayofyear / 365) + np.random.normal(0,5,n), 20, 100)
wind_speed = np.clip(np.random.normal(10, 3, n), 0, 25)
pressure = np.clip(np.random.normal(1013, 5, n), 980, 1050)

# --- Create DataFrame ---
df = pd.DataFrame({
    "date": dates,
    "temp_max": np.round(temp_max, 1),
    "temp_min": np.round(temp_min, 1),
    "temp_avg": np.round(temp_avg, 1),
    "precip_mm": np.round(precip_mm, 1),
    "humidity": np.round(humidity, 0),
    "wind_speed": np.round(wind_speed, 1),
    "pressure": np.round(pressure, 1)
})

# --- Save to CSV ---
df.to_csv("weather_data.csv", index=False)
print("weather_data.csv generated successfully!")
