import pandas as pd
import numpy as np

# Create a sample DataFrame
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value1': [10, 20, 30, 40, 50, 60],
    'Value2': [100, 200, 300, 400, 500, 600]
})

# Basic groupby and aggregation
print("Mean of Value1 for each Category:")
print(df.groupby('Category')['Value1'].mean())

print("Max of Value2 for each Category:")
print(df.groupby('Category')['Value2'].max())

print("Sum of Value1 for each Category:")
print(df.groupby('Category')['Value1'].sum())

