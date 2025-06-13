import pandas as pd
import plotly.express as px

# Load the data from the CSV file
df = pd.read_csv("updated_cluster_assignment_with_names.csv")

# Filter out the data for Telangana (if necessary)
telangana_data = df[df['state_name'] == 'telangana']

# Plot the clusters on the map
fig = px.scatter_mapbox(
    telangana_data, 
    lat='latitude', 
    lon='longitude', 
    color='DBSCAN_Cluster',  # Color points based on cluster
    hover_data=['place_name'],  # Additional data to show on hover
    zoom=5,
)

# Update layout to customize map appearance
fig.update_layout(
    mapbox_style="carto-positron",  # Map style
    mapbox_zoom=5,  # Initial zoom level
    mapbox_center={"lat": 17.123184, "lon": 79.208824},  # Center of the map
    margin={"r":0,"t":0,"l":0,"b":0}  # Margins around the plot
)

# Show the plot
fig.show()
