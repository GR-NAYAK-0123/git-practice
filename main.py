import pandas as pd
import matplotlib.pyplot as plt

# Read parquet file
df = pd.read_parquet("customers.parquet")

# Select numeric column
column_name = "hour_utc"

# Histogram
plt.figure(figsize=(8, 5))
plt.hist(df[column_name], bins=10)
plt.title(f"Histogram of {column_name}")
plt.xlabel(column_name)
plt.ylabel("Frequency")
plt.show()

# Box Plot
plt.figure(figsize=(6, 5))
plt.boxplot(df[column_name])
plt.title(f"Box Plot of {column_name}")
plt.ylabel(column_name)
plt.show()