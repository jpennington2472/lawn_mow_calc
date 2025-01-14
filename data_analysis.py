import pandas as pd

# Load the dataset
data = pd.read_csv("lawn_mowing_data.csv")

# Perform analysis
print("Summary of collected data:")
print(data.describe())
