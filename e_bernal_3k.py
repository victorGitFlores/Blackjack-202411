# e_bernal_3k.py

import pandas as pd

# Original data as seen in the image
data = {
    'Km': [0.5, 1, 1.5, 2, 2.5, 3],
    'Avg Pace': [6.30, 6.45, 6.50, 6.20, 6.35, 6.40],
    'Cumulative Avg Pace': [6.30, 6.38, 6.42, 6.36, 6.36, 6.37]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Modify the values to target a final average pace of 6:15
adjustment_factor = 6.15 / df['Cumulative Avg Pace'].iloc[-1]
df['Avg Pace'] = df['Avg Pace'] * adjustment_factor
df['Cumulative Avg Pace'] = df['Cumulative Avg Pace'] * adjustment_factor

# Display the adjusted DataFrame
print(df)