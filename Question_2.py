import pandas as pd
import glob
import re

# Combine all yearly CSV files into one dataframe

files = glob.glob("C:/Users/tonyx/Desktop/New folder/Software Now/Assignment 2/temperatures/stations_group_*.csv")

df = pd.concat(
    (
        pd.read_csv(f).assign(
            year=int(re.search(r"\d{4}", f).group())
        )
        for f in files
    ),
    ignore_index=True
)

print("Combined dataframe shape:", df.shape)

STATION_COL = "STATION_NAME"

MONTH_COLS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Force month columns to numeric (non-numeric → NaN)
df[MONTH_COLS] = df[MONTH_COLS].apply(
    pd.to_numeric, errors="coerce"
)

# ANALYSIS 1: Seasonal average temperature

monthly_avg = df[MONTH_COLS].mean()

seasonal_avg = {
    "Summer": monthly_avg[["December", "January", "February"]].mean(),
    "Autumn": monthly_avg[["March", "April", "May"]].mean(),
    "Winter": monthly_avg[["June", "July", "August"]].mean(),
    "Spring": monthly_avg[["September", "October", "November"]].mean(),
}

average_temp_output = "C:/Users/tonyx/Desktop/New folder/Software Now/Assignment 2/average_temp.txt"

with open(average_temp_output, "w", encoding="utf-8") as f:
    for season in ["Summer", "Autumn", "Winter", "Spring"]:
        value = seasonal_avg[season]
        if pd.isna(value):
            f.write(f"{season}: N/A\n")
        else:
            f.write(f"{season}: {value:.1f}°C\n")

print("Saved:", average_temp_output)

# ANALYSIS 2: Station with largest temperature range

long_df = df.melt(
    id_vars=[STATION_COL],
    value_vars=MONTH_COLS,
    var_name="Month",
    value_name="Temperature"
)

long_df = long_df.dropna(subset=["Temperature"])

station_range = (
    long_df
    .groupby(STATION_COL)["Temperature"]
    .agg(Min="min", Max="max")
)

station_range["Range"] = station_range["Max"] - station_range["Min"]

max_range = station_range["Range"].max()
top_range_stations = station_range[station_range["Range"] == max_range]

range_output = "C:/Users/tonyx/Desktop/New folder/Software Now/Assignment 2/largest_temp_range_station.txt"

with open(range_output, "w", encoding="utf-8") as f:
    for station, row in top_range_stations.iterrows():
        f.write(
            f"Station {station}: "
            f"Range {row['Range']:.1f}°C "
            f"(Max: {row['Max']:.1f}°C,  Min: {row['Min']:.1f}°C)\n"              
        )

print("Saved:", range_output)

# ANALYSIS 3: Temperature stability (standard deviation)

station_std = (
    long_df
    .groupby(STATION_COL)["Temperature"]
    .std()
)

min_std = station_std.min()
max_std = station_std.max()

most_stable = station_std[station_std == min_std]
most_variable = station_std[station_std == max_std]

stability_output = "C:/Users/tonyx/Desktop/New folder/Software Now/Assignment 2/temperature_stability_stations.txt"

with open(stability_output, "w", encoding="utf-8") as f:
    for station, std in most_stable.items():
        f.write(f"Most Stable: Station {station}: StdDev {std:.1f}°C\n")

    for station, std in most_variable.items():
        f.write(f"Most Variable: Station {station}: StdDev {std:.1f}°C\n")

print("Saved:", stability_output)

print("All analyses completed successfully.")
