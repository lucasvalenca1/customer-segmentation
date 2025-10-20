
# Based on the elbow method and silhouette analysis, let's use 4 clusters for better interpretability
optimal_k = 4

print(f"\n6. Building K-Means Model with {optimal_k} clusters...")

# Build the final model
kmeans_final = KMeans(n_clusters=optimal_k, init='k-means++', random_state=42, n_init=10)
cluster_labels = kmeans_final.fit_predict(X_scaled)

# Add cluster labels to original dataframe
df['Cluster'] = cluster_labels

print(f"Model successfully built with {optimal_k} clusters!")
print(f"\nFinal Model Inertia: {kmeans_final.inertia_:.2f}")
print(f"Final Silhouette Score: {silhouette_score(X_scaled, cluster_labels):.4f}")

# Display cluster distribution
print("\n7. Cluster Distribution:")
cluster_counts = df['Cluster'].value_counts().sort_index()
print(cluster_counts)
print("\nCluster Percentages:")
print((cluster_counts / len(df) * 100).round(2))
