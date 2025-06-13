import pandas as pd

# Read the data from the file
df = pd.read_csv("532-545(districts).csv")

# Group the data by 'year' and calculate the slope for each consecutive year
slope_values = df.groupby('year')['viirs_annual_mean'].diff()

# Add the calculated slope values as a new column
df['slope'] = slope_values

# Write the updated DataFrame to a new file
df.to_csv("slopes_of_consecutive_years.csv", index=False)
