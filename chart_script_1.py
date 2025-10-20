import plotly.graph_objects as go
import plotly.express as px

# Data
k_values = [2, 3, 4, 5, 6, 7, 8, 9, 10]
silhouette_scores = [0.1540, 0.1460, 0.1507, 0.1554, 0.1660, 0.1737, 0.1739, 0.1763, 0.1841]

# Create colors list - highlight K=4 with different color
colors = ['#DB4545' if k == 4 else '#1FB8CD' for k in k_values]

# Create bar chart
fig = go.Figure()

# Add bars
fig.add_trace(go.Bar(
    x=k_values,
    y=silhouette_scores,
    marker_color=colors,
    showlegend=False
))

# Add horizontal reference line at y=0.15
fig.add_hline(y=0.15, line_dash="dash", line_color="gray", 
              annotation_text="Threshold", annotation_position="bottom right")

# Update layout
fig.update_layout(
    title="Silhouette Score by Number of Clusters",
    xaxis_title="Num of Clusters",
    yaxis_title="Silhouette Scr"
)

# Update traces
fig.update_traces(cliponaxis=False)

# Update x-axis to show integer ticks
fig.update_xaxes(tickmode='linear', tick0=2, dtick=1)

# Save as PNG and SVG
fig.write_image("silhouette_chart.png")
fig.write_image("silhouette_chart.svg", format="svg")

fig.show()