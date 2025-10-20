
# Step 5: Elbow Method to find optimal number of clusters
print("\n5. Finding Optimal Number of Clusters using Elbow Method...")

inertias = []
silhouette_scores = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))

# Display results
results_df = pd.DataFrame({
    'Number of Clusters': list(K_range),
    'Inertia (WCSS)': inertias,
    'Silhouette Score': silhouette_scores
})

print(results_df)
print("\nBest Silhouette Score:", max(silhouette_scores))
print("Optimal K based on Silhouette:", list(K_range)[silhouette_scores.index(max(silhouette_scores))])
