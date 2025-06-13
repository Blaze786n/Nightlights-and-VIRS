import pandas as pd

# Load the CSV file
file_path = 'slopes_with_location_names.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Define the column names for slopes (excluding the one for 2015-2016)
slope_columns = ['slope_2012_2013', 'slope_2013_2014', 'slope_2014_2015',
                 'slope_2016_2017', 'slope_2017_2018', 'slope_2018_2019',
                 'slope_2019_2020', 'slope_2020_2021']

# Function to count negative slopes
def count_negative_slopes(row):
    return sum(row[col] < 0 for col in slope_columns)

# Add a new column for the count of negative slopes
data['negative_slope_count'] = data.apply(count_negative_slopes, axis=1)

# Categorize rows based on the number of negative slopes
def categorize_row(count):
    if count == 1:
        return 'one_negative_slope'
    elif count == 2:
        return 'two_negative_slopes'
    elif count == 3:
        return 'three_negative_slopes'
    elif count >= 4:
        return 'four_or_more_negative_slopes'
    else:
        return 'no_negative_slopes'

data['category'] = data['negative_slope_count'].apply(categorize_row)

# Save the result to a new CSV file
output_file_path = 'categorized_data.csv'  # Replace with your desired output file path
data.to_csv(output_file_path, index=False)

print(f"Categorized data saved to {output_file_path}")
