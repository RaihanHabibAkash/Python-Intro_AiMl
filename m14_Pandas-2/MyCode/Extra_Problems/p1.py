import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [5, np.nan, np.nan, None, 10],
    'C': ['a', 'b', 'c', None, 'e']
})

print(df)

# Replace null values based on given conditions
df_filled = df.fillna({'A': 0, 'B': 99, 'C': 'Unknown'})
print(df_filled)

# Forward fill column B
df_ffilled = df.copy()
df_ffilled["B"] = df["B"].ffill()
print(df_ffilled)


# Fills missing values in numeric columns with the mean of the column and in string columns with 'Unknown'.
def get_val(df):
    num_col = df.select_dtypes(include='number').columns
    str_col = df.select_dtypes(exclude='number').columns
    
    
    df[num_col] = df[num_col].fillna(df[num_col].mean())
    df[str_col] = df[str_col].fillna("Unknown")
    
    return df
    
print(get_val(df.copy()))