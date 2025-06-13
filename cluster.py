import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the data
data = pd.read_csv('532-545(districts).csv')

# Step 2: Data Preprocessing
# Select relevant features for clustering
features = ['viirs_annual_min', 'viirs_annual_max', 'viirs_annual_mean', 'viirs_annual_sum', 'viirs_annual_num_cells']

# Normalize the data
scaler = StandardScaler()
normalized_data = scaler.fit_transform(data[features])

# Step 3: Determine the optimal number of clusters using the elbow method
inertia = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(normalized_data)
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
data['Cluster'] = kmeans.fit_predict(normalized_data)

# Step 5: Analyze the clusters
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
cluster_labels = kmeans.labels_

# Step 6: Visualize the results
sns.pairplot(data, hue='Cluster', vars=features, palette='Set1')
plt.show()

# Display cluster centers
print("Cluster Centers:")
print(pd.DataFrame(cluster_centers, columns=features))
