import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load the data
data = pd.read_csv('clustered_data.csv')

# Step 2: Data Preprocessing
# Select the 'slope' feature for clustering
slope_feature = data[['slope']]

# Normalize the data
scaler = StandardScaler()
normalized_slope = scaler.fit_transform(slope_feature)

# Function to perform DBSCAN and return the number of clusters found
def perform_dbscan(eps, min_samples):
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    labels = dbscan.fit_predict(normalized_slope)
    num_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    return labels, num_clusters

# Step 3: Experiment with different eps and min_samples values
eps_values = np.arange(0.1, 1.1, 0.1)
min_samples_values = range(1, 10)

best_eps = 0
best_min_samples = 0
best_num_clusters = 0
best_labels = []

for eps in eps_values:
    for min_samples in min_samples_values:
        labels, num_clusters = perform_dbscan(eps, min_samples)
        if num_clusters > best_num_clusters:
            best_eps = eps
            best_min_samples = min_samples
            best_num_clusters = num_clusters
            best_labels = labels

print(f"Best eps: {best_eps}, Best min_samples: {best_min_samples}, Number of clusters: {best_num_clusters}")

# Assign the best labels to the data
data['Cluster'] = best_labels

# Step 4: Analyze and Visualize the Clusters
plt.figure(figsize=(10, 6))
plt.scatter(data['slope'], data['Cluster'], c=data['Cluster'], cmap='viridis')
plt.xlabel('Slope')
plt.ylabel('Cluster')
plt.title('DBSCAN Clustering Results (using Slope)')
plt.show()

# Save the clustered data to a new CSV file
data.to_csv('clustered_data.csv', index=False)

# Step 5: Get shrid2 values for each cluster
clustered_shrid2 = data.groupby('Cluster')['shrid2'].apply(list).reset_index()
clustered_shrid2.to_csv('clustered_shrid2.csv', index=False)

# Print the shrid2 values for each cluster
for cluster, shrid2_list in clustered_shrid2.values:
    print(f"Cluster {cluster}:")
    print(shrid2_list)
