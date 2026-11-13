import pandas as pd

# Read CSV file
data = pd.read_csv("data.csv")

# Display complete data
print(data)

# Display each column
for col in data.columns:
    print(data[col])
