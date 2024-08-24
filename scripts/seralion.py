import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import seaborn as sns
from math import pi
df=pd.read_csv(r"C:/Users/Admin.DESKTOP-M4R2VLU/Desktop/week01/week0/data/sierraleone-bumbuna.csv")
 # Calculate the summary statistics

#Summary stastic

numeric_columns = df.select_dtypes(include=['number']).columns

print("Summary Statistics:")
for column in numeric_columns:
    print(f"\nColumn: {column}")
    print(f"Mean: {df[column].mean():.2f}")
    print(f"Median: {df[column].median():.2f}")
    print(f"Standard Deviation: {df[column].std():.2f}")
    print(f"Minimum: {df[column].min():.2f}")
    print(f"Maximum: {df[column].max():.2f}")
    print(f"Variance: {df[column].var():.2f}")
    print(f"Skewness: {df[column].skew():.2f}")
    print(f"Kurtosis: {df[column].kurtosis():.2f}")


# Check for missing values
print("Missing values:")
print(df.isnull().sum())

# Check for outliers
print("\nOutliers:")

# GHI, DNI, DHI
for col in ['GHI', 'DNI', 'DHI']:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print(f"Outliers in {col}: {len(outliers)}")

# ModA, ModB
for col in ['ModA', 'ModB']:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print(f"Outliers in {col}: {len(outliers)}")

# WS, WSgust
for col in ['WS', 'WSgust']:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print(f"Outliers in {col}: {len(outliers)}")

# Check for negative values in columns where only positive values should exist
print("\nNegative values:")
for col in ['GHI', 'DNI', 'DHI']:
    neg_values = df[df[col] < 0]
    print(f"Negative values in {col}: {len(neg_values)}")


  

# Convert the 'Timestamp' column to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Plot GHI, DNI, DHI, and Tamb over time
fig, axes = plt.subplots(4, 1, figsize=(12, 10), sharex=True)

# GHI
axes[0].plot(df['Timestamp'], df['GHI'])
axes[0].set_title('Global Horizontal Irradiance (GHI)')
axes[0].xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

# DNI
axes[1].plot(df['Timestamp'], df['DNI'])
axes[1].set_title('Direct Normal Irradiance (DNI)')
axes[1].xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

# DHI
axes[2].plot(df['Timestamp'], df['DHI'])
axes[2].set_title('Diffuse Horizontal Irradiance (DHI)')
axes[2].xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

# Tamb
axes[3].plot(df['Timestamp'], df['Tamb'])
axes[3].set_title('Ambient Temperature (Tamb)')
axes[3].xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

plt.suptitle('Time Series Plots')
plt.tight_layout()
plt.show()

# Evaluate the impact of cleaning on ModA and ModB
fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# ModA
axes[0].plot(df['Timestamp'], df['ModA'], label='Uncleaned')
axes[0].plot(df['Timestamp'], df.loc[df['Cleaning'] == 1, 'ModA'], label='Cleaned')
axes[0].set_title('Module A (ModA)')
axes[0].legend()
axes[0].xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

# ModB
axes[1].plot(df['Timestamp'], df['ModB'], label='Uncleaned')
axes[1].plot(df['Timestamp'], df.loc[df['Cleaning'] == 1, 'ModB'], label='Cleaned')
axes[1].set_title('Module B (ModB)')
axes[1].legend()
axes[1].xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

plt.suptitle('Impact of Cleaning on Sensor Readings')
plt.tight_layout()
plt.show()



# Create the polar plot
plt.figure(figsize=(10, 10))
ax = plt.subplot(111, projection='polar')

# Plot the wind speed and direction
ax.scatter(df['WD'] * pi/180, df['WS'], s=5, cmap='viridis')

# Set the radial gridlines
ax.set_rlim(0, df['WS'].max())
ax.set_rticks(range(0, int(df['WS'].max())+1, 2))
ax.set_rgrids(range(0, int(df['WS'].max())+1, 2), labels=[str(x) for x in range(0, int(df['WS'].max())+1, 2)])

# Set the angular gridlines and labels
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_thetagrids([0, 45, 90, 135, 180, 225, 270, 315], labels=['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])

# Add labels and title
ax.set_title('Wind Speed and Direction')
ax.set_xlabel('Wind Direction (degrees)')
ax.set_ylabel('Wind Speed (m/s)')

plt.show()