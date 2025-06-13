import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 1: Load the data
data = pd.read_csv('532-545(districts).csv')

# Step 2: Data Preprocessing
# Select the 'viirs_annual_mean' column for clustering
intensity_data = data[['viirs_annual_mean']]

# Normalize the data
scaler = StandardScaler()
normalized_intensity = scaler.fit_transform(intensity_data)

# Step 3: Determine the optimal number of clusters using the elbow method
inertia = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(normalized_intensity)
    inertia.append(kmeans.inertia_)

# Plot the elbow curve
plt.figure(figsize=(10, 6))
plt.plot(K, inertia, 'bx-')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal k')
plt.show()

# Step 4: Apply K-means clustering
optimal_k = 3  # Choose the optimal number of clusters based on the elbow method
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
data['Cluster'] = kmeans.fit_predict(normalized_intensity)

# Step 5: Analyze the clusters
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
cluster_labels = kmeans.labels_

# Step 6: Visualize the results
plt.figure(figsize=(10, 6))
plt.scatter(data['viirs_annual_mean'], [0] * len(data), c=data['Cluster'], cmap='viridis')
plt.xlabel('viirs_annual_mean')
plt.title('K-means Clustering Based on Intensity')
plt.show()

# Display cluster centers
print("Cluster Centers:")
print(pd.DataFrame(cluster_centers, columns=['viirs_annual_mean']))
