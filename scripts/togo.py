import pandas as pd
df=pd.read_csv(r"C:/Users/Admin.DESKTOP-M4R2VLU/Desktop/week01/week0/data/togo-dapaong_qc.csv")
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