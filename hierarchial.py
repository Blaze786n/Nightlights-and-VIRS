import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import plotly.express as px

# Load the data
file_path = 'merged_data.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the data
print(data.head())

# Check for longitude and latitude columns
if 'longitude' not in data.columns or 'latitude' not in data.columns:
    raise ValueError("Missing required columns: 'longitude' and 'latitude'")

# Calculate the slopes
# Adding a small epsilon to avoid division by zero
data['slope_lat'] = np.gradient(data['latitude'])
data['slope_lon'] = np.gradient(data['longitude'] + 1e-9)
data['slope'] = np.arctan2(data['slope_lat'], data['slope_lon'])

# Extract the relevant features
features = data[['longitude', 'latitude', 'slope_lat', 'slope_lon', 'slope']]

# Standardize the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Apply hierarchical clustering with Ward linkage
Z = linkage(features_scaled, method='ward')

# Determine the clusters using a distance threshold or by specifying the number of clusters
# For demonstration, let's use the distance threshold
distance_threshold = 10  # Adjust this threshold based on your data
clusters = fcluster(Z, t=distance_threshold, criterion='distance')

# Add the cluster labels to the original data
data['cluster'] = clusters

# Define a custom color sequence
color_sequence = px.colors.qualitative.Set1 + px.colors.qualitative.Set2 + px.colors.qualitative.Set3

# Plot the clusters using Plotly
fig = px.scatter(
    data,
    x='longitude',
    y='latitude',
    color='cluster',
    title=f'Hierarchical Clustering (Ward Linkage) based on Longitude, Latitude, and Slopes (Threshold={distance_threshold})',
    labels={'cluster': 'Cluster Label'},
    color_discrete_sequence=color_sequence
)

fig.show()

# Save the resulting clustered data to a new CSV file
output_file_path = 'clustered_data1.csv'
data.to_csv(output_file_path, index=False)
print(f"Clustered data saved to {output_file_path}")