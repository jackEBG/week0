import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
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