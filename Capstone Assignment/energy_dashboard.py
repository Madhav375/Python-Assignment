#Name: Madhav Kalra
#Class: B.tech CSE (AI ML) 1st year 
#Section-A
#Roll No: 2501730284

import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path
print("Working directory:", os.getcwd())
os.makedirs("output", exist_ok=True)

# Task 1: Data Ingestion and Validation

data_folder = "data"     
path_obj = Path(data_folder)
all_files = list(Path(data_folder).glob("*.csv"))
combined_data = []
print("Reading CSV files from:", data_folder)

for file in all_files:
    try:
        df = pd.read_csv(file)
        df["source_file"] = file.name  
        combined_data.append(df)
        print("Loaded:", file.name)
    except Exception as e:
        print("Error loading:", file.name, "->", e)

# merge everything
if len(combined_data) == 0:
    print("No data found.")
    exit()

df = pd.concat(combined_data, ignore_index=True)

# clean timestamp column
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df = df.dropna(subset=["timestamp"])

print("\nData Loaded Successfully. Preview:\n")
print(df.head())

# Task 2: Core Aggregation Logic

def calculate_daily_totals(data):
    return data.resample("D", on="timestamp")["kwh"].sum()

def calculate_weekly_totals(data):
    return data.resample("W", on="timestamp")["kwh"].sum()

def building_wise_summary(data):
    return data.groupby("building")["kwh"].agg(["mean", "min", "max", "sum"])

daily_totals = calculate_daily_totals(df)
weekly_totals = calculate_weekly_totals(df)
build_summary = building_wise_summary(df)

print("\n--- Building Summary ---\n")
print(build_summary)

# Task 3: Object Oriented Modelling

class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp
        self.kwh = kwh

class Building:
    def __init__(self, name):
        self.name = name
        self.meter_readings = []

    def add_reading(self, reading):
        self.meter_readings.append(reading)

    def calculate_total_consumption(self):
        return sum(r.kwh for r in self.meter_readings)

    def generate_report(self):
        total = self.calculate_total_consumption()
        return f"{self.name}: Total monthly consumption = {total:.2f} kWh"

class BuildingManager:
    def __init__(self):
        self.buildings = {}

    def add_reading(self, building_name, timestamp, kwh):
        if building_name not in self.buildings:
            self.buildings[building_name] = Building(building_name)
        self.buildings[building_name].add_reading(MeterReading(timestamp, kwh))

    def generate_all_reports(self):
        reports = []
        for b in self.buildings.values():
            reports.append(b.generate_report())
        return reports

manager = BuildingManager()

for _, row in df.iterrows():
    manager.add_reading(row["building"], row["timestamp"], row["kwh"])
print("\n--- OOP Building Reports ---\n")
for report in manager.generate_all_reports():
    print(report)

# Task 4: Visualization using Matplotlib

plt.figure(figsize=(14, 10))

# Subplot 1 – Daily Trend Line
plt.subplot(3, 1, 1)
plt.plot(daily_totals.index, daily_totals.values)
plt.title("Daily Electricity Usage")
plt.xlabel("Date")
plt.ylabel("kWh")

# Subplot 2 – Weekly Comparison Bar Chart
plt.subplot(3, 1, 2)
plt.bar(weekly_totals.index.astype(str), weekly_totals.values)
plt.title("Weekly Electricity Usage")
plt.xlabel("Week")
plt.ylabel("kWh")

# Subplot 3 – Scatter Plot (all buildings)
plt.subplot(3, 1, 3)
plt.scatter(df["timestamp"], df["kwh"], alpha=0.5)
plt.title("Scatter Plot — All Readings")
plt.xlabel("Timestamp")
plt.ylabel("kWh")

plt.tight_layout()
plt.savefig("dashboard.png")
plt.close()

print("\nDashboard saved as dashboard.png")

# Task 5: Exporting clean data

df.to_csv("output/cleaned_energy_data.csv", index=False)
build_summary.to_csv("output/building_summary.csv")

with open("output/summary.txt", "w") as f:
    f.write("Campus Energy Summary Report\n")
    f.write("----------------------------\n")
    f.write(f"Total Campus Consumption: {df['kwh'].sum():.2f} kWh\n")
    f.write(f"Highest Consuming Building: {build_summary['sum'].idxmax()}\n")
    f.write("\nWeekly Totals:\n")
    f.write(str(weekly_totals))
    f.write("\n\nDaily Totals:\n")
    f.write(str(daily_totals))

print("Export complete: cleaned_energy_data.csv, building_summary.csv, summary.txt")
print("Project Finished.")
plt.savefig("output/dashboard.png")
