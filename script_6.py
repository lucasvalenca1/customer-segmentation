
# Step 10: Save results and create output files for GitHub

# Save the clustered data
output_file = 'customer_segmentation_results.csv'
df.to_csv(output_file, index=False)
print(f"\n10. Results saved to '{output_file}'")

# Save cluster summary
cluster_summary_file = 'cluster_summary.csv'
cluster_summary.to_csv(cluster_summary_file)
print(f"Cluster summary saved to '{cluster_summary_file}'")

# Create a summary report
summary_stats = {
    'Metric': ['Total Customers', 'Number of Clusters', 'Inertia', 'Silhouette Score'],
    'Value': [len(df), optimal_k, f"{kmeans_final.inertia_:.2f}", f"{silhouette_score(X_scaled, cluster_labels):.4f}"]
}
summary_df = pd.DataFrame(summary_stats)
print("\n" + "="*80)
print("PROJECT SUMMARY")
print("="*80)
print(summary_df.to_string(index=False))

print("\n" + "="*80)
print("FILES CREATED FOR GITHUB:")
print("="*80)
print(f"✓ {output_file} - Complete customer data with cluster assignments")
print(f"✓ {cluster_summary_file} - Statistical summary of each cluster")
print("\n" + "="*80)
print("PROJECT COMPLETE! Ready for GitHub upload.")
print("="*80)
