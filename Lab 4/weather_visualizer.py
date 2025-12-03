#Name: Madhav Kalra
#Roll No: 2501730284

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_name = "weather_data.csv"

try:
    data = pd.read_csv(file_name)
    print("File loaded successfully!")
except:
    print("Error loading the file. Make sure CSV exists.")
    exit()

print("\n--- Data Head ---")
print(data.head())

print("\n--- Info ---")
print(data.info())

print("\n--- Describe ---")
print(data.describe())

if "date" in data.columns:
    data["date"] = pd.to_datetime(data["date"], errors="coerce")

# Removing rows where date could NOT be converted
data = data.dropna(subset=["date"])

# Fill missing numeric values with mean (simple method)
numeric_cols = data.select_dtypes(include=["float64", "int64"]).columns
for col in numeric_cols:
    data[col] = data[col].fillna(data[col].mean())

# Keeping only important columns if available
use_cols = ["date", "temperature", "rainfall", "humidity"]
present_cols = [c for c in use_cols if c in data.columns]
data = data[present_cols]

print("\nCleaned Data:")
print(data.head())


temps = data["temperature"].values

print("\n--- Temperature Stats ---")
print("Mean:", np.mean(temps))
print("Min:", np.min(temps))
print("Max:", np.max(temps))
print("Std Dev:", np.std(temps))

# Monthly grouping (helpful later)
data["month"] = data["date"].dt.month

# Daily temperature line chart
plt.figure(figsize=(10,5))
plt.plot(data["date"], data["temperature"])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.tight_layout()
plt.savefig("daily_temperature.png")
plt.close()

# Monthly rainfall bar chart
if "rainfall" in data.columns:
    monthly_rain = data.groupby("month")["rainfall"].sum()
    plt.figure(figsize=(8,5))
    plt.bar(monthly_rain.index, monthly_rain.values)
    plt.title("Monthly Rainfall")
    plt.xlabel("Month")
    plt.ylabel("Rainfall Total")
    plt.savefig("monthly_rainfall.png")
    plt.close()

# Scatter plot: humidity vs temp
if "humidity" in data.columns:
    plt.figure(figsize=(7,5))
    plt.scatter(data["temperature"], data["humidity"])
    plt.title("Humidity vs Temperature")
    plt.xlabel("Temperature")
    plt.ylabel("Humidity")
    plt.savefig("temp_vs_humidity.png")
    plt.close()

# Combined figure (subplot)
fig, ax = plt.subplots(2,1,figsize=(10,8))
ax[0].plot(data["date"], data["temperature"])
ax[0].set_title("Temperature Trend")
if "humidity" in data.columns:
    ax[1].scatter(data["date"], data["humidity"])
    ax[1].set_title("Humidity Scatter")

plt.tight_layout()
plt.savefig("combined_plot.png")
plt.close()

monthly_stats = data.groupby("month").agg({
    "temperature": ["mean", "min", "max"],
    "rainfall": "sum" if "rainfall" in data.columns else "mean",
    "humidity": "mean" if "humidity" in data.columns else "mean"
})

print("\n--- Monthly Summary ---")
print(monthly_stats)

data.to_csv("cleaned_weather_data.csv", index=False)
print("\nCleaned data exported as cleaned_weather_data.csv")

with open("summary_report.txt", "w") as f:
    f.write("Weather Data Summary Report\n")
    f.write("--------------------------\n")
    f.write(str(monthly_stats))
    f.write("\n\nKey Observations:\n")
    f.write("- Temperature varies across months.\n")
    f.write("- Rainfall data shows seasonal patterns.\n")
    f.write("- Humidity relation can be checked in scatter plot.\n")

print("Summary report saved as summary_report.txt")
print("All plots saved as PNG files.\n")
print("Project completed!")