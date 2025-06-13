import pandas as pd

# Load the processed.csv file
processed_df = pd.read_csv('processed_data.csv')

# Load the location_data.csv file
location_data_df = pd.read_csv('updated_cluster_assignment_with_names.csv')

# Merge the two DataFrames on the shrid2 column
merged_df = pd.merge(processed_df, location_data_df[['shrid2', 'latitude', 'longitude']], on='shrid2', how='left')

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('processed2.csv', index=False)

print("The new file 'processed2.csv' has been created with latitude and longitude columns added.")
