import pandas as pd
import plotly.express as px

# Load the updated CSV file
updated_cluster_assignment_path = r'"F:\Nightlights\updated_cluster_assignment_with_names.csv"'
updated_cluster_assignment = pd.read_csv(updated_cluster_assignment_path)

# Create a scatter plot
fig = px.scatter(
    updated_cluster_assignment,
    x='longitude',
    y='latitude',
    color='shrid',
    hover_data=['town_name', 'village_name', 'district_name'],
    title='Latitude and Longitude Plot Colored by shrid'
)

# Update layout for better presentation
fig.update_layout(
    xaxis_title='Longitude',
    yaxis_title='Latitude',
    legend_title_text='shrid',
    legend=dict(
        title='shrid',
        traceorder='normal'
    )
)

# Show the plot
fig.show()
