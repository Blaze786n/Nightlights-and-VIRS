import pandas as pd
import numpy as np
from scipy.stats import linregress

# Read data from CSV file
df = pd.read_csv('532-545(districts).csv')

# Pivot the data to have years as columns
pivot_df = df.pivot_table(index='shrid2', columns='year', values='viirs_annual_mean').reset_index()

# Get the list of years we're interested in
years = list(range(2012, 2022))

# Ensure the year columns are numeric
for year in years:
    pivot_df[year] = pd.to_numeric(pivot_df[year], errors='coerce')

# List to store results
results = []

# Calculate slope for each row
for _, row in pivot_df.iterrows():
    # Extract the VIIRS annual mean values for the relevant years
    means = row[years].values.astype(np.float64)
    
    # Check if there are at least two non-NaN values
    if np.count_nonzero(~np.isnan(means)) > 1:
        # Perform linear regression
        slope, intercept, r_value, p_value, std_err = linregress(years, means)
        results.append({
            'shrid2': row['shrid2'],
            'slope': slope,
            'intercept': intercept,
            'r_value': r_value,
            'p_value': p_value,
            'std_err': std_err
        })
    else:
        results.append({
            'shrid2': row['shrid2'],
            'slope': np.nan,
            'intercept': np.nan,
            'r_value': np.nan,
            'p_value': np.nan,
            'std_err': np.nan
        })  # Not enough data to calculate slope

# Convert results to DataFrame
results_df = pd.DataFrame(results)

# Save the results to a CSV file
results_df.to_csv('slopes_per_row.csv', index=False)

print("Detailed results have been saved to slopes_per_row.csv")
