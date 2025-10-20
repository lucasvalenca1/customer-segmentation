import plotly.graph_objects as go
import plotly.io as pio

# Data for the elbow plot
k_values = [2, 3, 4, 5, 6, 7, 8, 9, 10]
inertia_values = [2106.53, 1858.86, 1670.65, 1515.47, 1384.86, 1276.00, 1193.74, 1124.56, 1055.02]

# Create the main line chart
fig = go.Figure()

# Add the main elbow curve
fig.add_trace(go.Scatter(
    x=k_values,
    y=inertia_values,
    mode='lines+markers',
    marker=dict(size=8, symbol='circle'),
    line=dict(width=3),
    name='Inertia',
    hovertemplate='Clusters: %{x}<br>Inertia: %{y:.2f}<extra></extra>'
))

# Add special marker for K=4 (the elbow point)
fig.add_trace(go.Scatter(
    x=[4],
    y=[1670.65],
    mode='markers',
    marker=dict(size=15, symbol='circle', color='#DB4545', line=dict(width=3, color='white')),
    name='Optimal (K=4)',
    hovertemplate='Optimal Point<br>Clusters: 4<br>Inertia: 1670.65<extra></extra>'
))

# Update layout
fig.update_layout(
    title='Elbow Method - Optimal Clusters',
    xaxis_title='Clusters',
    yaxis_title='Inertia',
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

# Update axes
fig.update_xaxes(range=[1.5, 10.5], dtick=1)
fig.update_yaxes(range=[1000, 2200])

# Enable clipping off axis for better marker visibility
fig.update_traces(cliponaxis=False)

# Save the chart as both PNG and SVG
fig.write_image('elbow_plot.png')
fig.write_image('elbow_plot.svg', format='svg')

fig.show()