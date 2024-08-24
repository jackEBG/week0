import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from math import pi
df=pd.read_csv(r"C:/Users/Admin.DESKTOP-M4R2VLU/Desktop/week01/week0/data/benin-malanville.csv")
 # Calculate the summary statistics
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


# Correlation heatmap
plt.figure(figsize=(10, 8))
corr_matrix = df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='YlOrRd')
plt.title('Correlation Heatmap')
plt.show()

# Pair plot
plt.figure(figsize=(12, 10))
sns.pairplot(df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']], diag_kind='kde')
plt.suptitle('Pair Plot')
plt.show()

# Scatter matrix
plt.figure(figsize=(12, 10))
scatter_matrix = pd.plotting.scatter_matrix(df[['GHI', 'DNI', 'DHI', 'WS', 'WSgust', 'WD']], diagonal='kde')
plt.suptitle('Scatter Matrix')
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


fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.plot(df.index, df['Tamb'], color='red', label='Ambient Temperature')
ax2 = ax1.twinx()
ax2.plot(df.index, df['RH'], color='blue', label='Relative Humidity')

ax1.set_xlabel('Time')
ax1.set_ylabel('Ambient Temperature (°C)', color='red')
ax2.set_ylabel('Relative Humidity (%)', color='blue')
ax1.set_title('Ambient Temperature and Relative Humidity')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()



# Create a figure with 2x3 subplots
fig, axes = plt.subplots(2, 3, figsize=(16, 10))

# Plot histograms
axes[0, 0].hist(df['GHI'], bins=30)
axes[0, 0].set_title('Global Horizontal Irradiance (GHI)')
axes[0, 0].set_xlabel('GHI (W/m^2)')
axes[0, 0].set_ylabel('Frequency')

axes[0, 1].hist(df['DNI'], bins=30)
axes[0, 1].set_title('Direct Normal Irradiance (DNI)')
axes[0, 1].set_xlabel('DNI (W/m^2)')
axes[0, 1].set_ylabel('Frequency')

axes[0, 2].hist(df['DHI'], bins=30)
axes[0, 2].set_title('Diffuse Horizontal Irradiance (DHI)')
axes[0, 2].set_xlabel('DHI (W/m^2)')
axes[0, 2].set_ylabel('Frequency')

axes[1, 0].hist(df['WS'], bins=30)
axes[1, 0].set_title('Wind Speed (WS)')
axes[1, 0].set_xlabel('WS (m/s)')
axes[1, 0].set_ylabel('Frequency')

axes[1, 1].hist(df['Tamb'], bins=30)
axes[1, 1].set_title('Ambient Temperature (Tamb)')
axes[1, 1].set_xlabel('Tamb (°C)')
axes[1, 1].set_ylabel('Frequency')

axes[1, 2].hist(df['RH'], bins=30)
axes[1, 2].set_title('Relative Humidity (RH)')
axes[1, 2].set_xlabel('RH (%)')
axes[1, 2].set_ylabel('Frequency')

plt.tight_layout()
plt.show()

# Assume your data is in a pandas DataFrame 'df'
# Calculate the mean and standard deviation for each variable
means = df.mean()
stds = df.std()

# Calculate the Z-scores
z_scores = (df - means) / stds

# Identify data points with a Z-score greater than 3 or less than -3 (99.7% confidence interval)
outliers = z_scores[(z_scores > 3) | (z_scores < -3)]

# Print the outliers
print(outliers)

# Choose the variable to represent bubble size
bubble_size_var = 'RH'  # or 'BP' for Barometric Pressure

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the bubble chart
bubble_size = df[bubble_size_var]
ax.scatter(df['GHI'], df['Tamb'], s=bubble_size * 10, c=df['WS'], alpha=0.6)

# Add labels and title
ax.set_xlabel('GHI (W/m^2)')
ax.set_ylabel('Tamb (°C)')
ax.set_title(f'GHI vs Tamb vs WS, bubble size represents {bubble_size_var}')

# Add a colorbar for wind speed
cbar = ax.figure.colorbar(ax.collections[0], ax=ax)
cbar.set_label('Wind Speed (m/s)')

# Adjust the layout
plt.tight_layout()
plt.show()