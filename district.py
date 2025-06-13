import pandas as pd

# Read the CSV file
df = pd.read_csv('viirs_annual_pc11dist.csv')

# Filter rows where pc11_state_id is 28
filtered_df = df[df['pc11_state_id'] == 28]

# Save the filtered dataframe to a new CSV file
filtered_df.to_csv('filtered_data2.csv', index=False)

print("Filtered data has been saved to 'filtered_data2.csv'")
