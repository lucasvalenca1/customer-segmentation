import plotly.graph_objects as go
import plotly.express as px

# Data from the provided JSON
clusters = ["0", "1", "2", "3"]
annual_income = [49.4, 76.5, 57.1, 27.2]
spending_score = [27.5, 53.2, 61.8, 47.4]
purchase_frequency = [34.0, 72.9, 25.8, 76.5]
avg_transaction = [39.9, 57.1, 68.1, 52.2]
days_since_last = [70.2, 61.2, 30.3, 41.6]

# Create the grouped bar chart
fig = go.Figure()

# Add bars for each characteristic using the brand colors
fig.add_trace(go.Bar(
    name='Annual Income',
    x=clusters,
    y=annual_income,
    marker_color='#1FB8CD'
))

fig.add_trace(go.Bar(
    name='Spending Score',
    x=clusters,
    y=spending_score,
    marker_color='#DB4545'
))

fig.add_trace(go.Bar(
    name='Purchase Freq',
    x=clusters,
    y=purchase_frequency,
    marker_color='#2E8B57'
))

fig.add_trace(go.Bar(
    name='Avg Transaction',
    x=clusters,
    y=avg_transaction,
    marker_color='#5D878F'
))

fig.add_trace(go.Bar(
    name='Days Since Last',
    x=clusters,
    y=days_since_last,
    marker_color='#D2BA4C'
))

# Update layout with title and labels (shortened to meet character limits)
fig.update_layout(
    title='Customer Segment Comparison',
    xaxis_title='Cluster',
    yaxis_title='Normalized Value',
    barmode='group',
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

# Update traces
fig.update_traces(cliponaxis=False)

# Save as both PNG and SVG
fig.write_image("customer_clusters.png")
fig.write_image("customer_clusters.svg", format="svg")

fig.show()