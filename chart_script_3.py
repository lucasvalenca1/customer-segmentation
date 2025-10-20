import plotly.express as px
import pandas as pd

# Create the data from the provided JSON
data = {
    "segment": ["Cluster 0: At-Risk", "Cluster 1: Premium Loyal", "Cluster 2: Active High-Engagement", "Cluster 3: Budget-Conscious"], 
    "count": [109, 129, 133, 129], 
    "percentage": [21.8, 25.8, 26.6, 25.8]
}

df = pd.DataFrame(data)

# Create shorter labels for better display inside slices
df['short_label'] = ['At-Risk', 'Premium Loyal', 'Active High-Eng', 'Budget-Conscious']

# Create the pie chart
fig = px.pie(df, 
             values='count', 
             names='segment',
             title='Customer Distribution Across Segments')

# Update traces to show both label and percentage inside the slices
fig.update_traces(
    textposition='inside', 
    textinfo='label+percent',
    textfont_size=12,
    texttemplate='%{label}<br>%{percent}'
)

# Apply uniform text settings for pie chart
fig.update_layout(uniformtext_minsize=10, uniformtext_mode='hide')

# Use brand colors for the segments
colors = ['#1FB8CD', '#DB4545', '#2E8B57', '#5D878F']
fig.update_traces(marker=dict(colors=colors))

# Save as both PNG and SVG
fig.write_image("customer_distribution_pie.png")
fig.write_image("customer_distribution_pie.svg", format="svg")

fig.show()