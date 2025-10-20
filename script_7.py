
# Create a comprehensive Python script for GitHub

python_script = '''#!/usr/bin/env python3
"""
Customer Segmentation Using K-Means Clustering
===============================================

This project demonstrates customer segmentation using machine learning (K-Means clustering)
with Python and scikit-learn. The analysis identifies distinct customer groups to enable
targeted marketing strategies and improve business outcomes.

Author: [Your Name]
Date: October 2025
Tools: Python, scikit-learn, pandas, matplotlib, seaborn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import warnings
warnings.filterwarnings('ignore')

# Configuration
RANDOM_STATE = 42
N_CUSTOMERS = 500
OPTIMAL_CLUSTERS = 4

# Set visualization style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)


def generate_customer_data(n_samples=N_CUSTOMERS):
    """Generate synthetic customer data for demonstration purposes."""
    np.random.seed(RANDOM_STATE)
    
    data = {
        'CustomerID': range(1, n_samples + 1),
        'Age': np.random.randint(18, 70, n_samples),
        'Annual_Income': np.random.randint(20000, 150000, n_samples),
        'Spending_Score': np.random.randint(1, 100, n_samples),
        'Purchase_Frequency': np.random.randint(1, 50, n_samples),
        'Average_Transaction_Value': np.random.randint(20, 500, n_samples),
        'Days_Since_Last_Purchase': np.random.randint(1, 365, n_samples)
    }
    
    return pd.DataFrame(data)


def perform_eda(df):
    """Perform exploratory data analysis on the dataset."""
    print("="*80)
    print("EXPLORATORY DATA ANALYSIS")
    print("="*80)
    print("\\nDataset Shape:", df.shape)
    print("\\nFirst 10 rows:")
    print(df.head(10))
    print("\\nStatistical Summary:")
    print(df.describe())
    print("\\nMissing Values:")
    print(df.isnull().sum())


def scale_features(X):
    """Scale features using StandardScaler for K-Means clustering."""
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("\\n" + "="*80)
    print("FEATURE SCALING COMPLETE")
    print("="*80)
    print("Mean of scaled features:", X_scaled.mean(axis=0).round(2))
    print("Std of scaled features:", X_scaled.std(axis=0).round(2))
    return X_scaled, scaler


def elbow_method(X_scaled, k_range=range(2, 11)):
    """Apply elbow method to find optimal number of clusters."""
    inertias = []
    silhouette_scores = []
    
    print("\\n" + "="*80)
    print("ELBOW METHOD ANALYSIS")
    print("="*80)
    
    for k in k_range:
        kmeans = KMeans(n_clusters=k, init='k-means++', 
                       random_state=RANDOM_STATE, n_init=10)
        kmeans.fit(X_scaled)
        inertias.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))
    
    results_df = pd.DataFrame({
        'Number of Clusters': list(k_range),
        'Inertia (WCSS)': inertias,
        'Silhouette Score': silhouette_scores
    })
    
    print(results_df)
    return inertias, silhouette_scores


def build_kmeans_model(X_scaled, n_clusters=OPTIMAL_CLUSTERS):
    """Build and train K-Means clustering model."""
    print(f"\\n{'='*80}")
    print(f"BUILDING K-MEANS MODEL WITH {n_clusters} CLUSTERS")
    print("="*80)
    
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', 
                   random_state=RANDOM_STATE, n_init=10)
    cluster_labels = kmeans.fit_predict(X_scaled)
    
    print(f"Model Inertia: {kmeans.inertia_:.2f}")
    print(f"Silhouette Score: {silhouette_score(X_scaled, cluster_labels):.4f}")
    
    return kmeans, cluster_labels


def analyze_clusters(df, features):
    """Analyze and interpret customer segments."""
    print("\\n" + "="*80)
    print("CLUSTER ANALYSIS")
    print("="*80)
    
    cluster_summary = df.groupby('Cluster')[features].mean()
    print("\\nAverage characteristics per cluster:")
    print(cluster_summary.round(2))
    
    print("\\nCluster distribution:")
    print(df['Cluster'].value_counts().sort_index())
    
    return cluster_summary


def generate_recommendations():
    """Generate business recommendations for each segment."""
    recommendations = {
        0: "At-Risk Customers: Implement re-engagement campaigns with special offers",
        1: "Premium Loyal: Create VIP program with exclusive benefits",
        2: "Active Shoppers: Focus on cross-selling and increasing purchase frequency",
        3: "Budget-Conscious: Offer value deals and loyalty rewards"
    }
    
    print("\\n" + "="*80)
    print("BUSINESS RECOMMENDATIONS")
    print("="*80)
    for cluster_id, rec in recommendations.items():
        print(f"\\nCluster {cluster_id}: {rec}")


def save_results(df, cluster_summary):
    """Save analysis results to CSV files."""
    df.to_csv('customer_segmentation_results.csv', index=False)
    cluster_summary.to_csv('cluster_summary.csv')
    print("\\n" + "="*80)
    print("RESULTS SAVED")
    print("="*80)
    print("✓ customer_segmentation_results.csv")
    print("✓ cluster_summary.csv")


def main():
    """Main execution function."""
    print("="*80)
    print("CUSTOMER SEGMENTATION PROJECT")
    print("="*80)
    
    # Step 1: Generate/Load data
    df = generate_customer_data()
    
    # Step 2: Exploratory Data Analysis
    perform_eda(df)
    
    # Step 3: Feature selection and scaling
    features = ['Annual_Income', 'Spending_Score', 'Purchase_Frequency',
                'Average_Transaction_Value', 'Days_Since_Last_Purchase']
    X = df[features]
    X_scaled, scaler = scale_features(X)
    
    # Step 4: Elbow method
    inertias, silhouette_scores = elbow_method(X_scaled)
    
    # Step 5: Build K-Means model
    kmeans, cluster_labels = build_kmeans_model(X_scaled)
    df['Cluster'] = cluster_labels
    
    # Step 6: Analyze clusters
    cluster_summary = analyze_clusters(df, features)
    
    # Step 7: Generate recommendations
    generate_recommendations()
    
    # Step 8: Save results
    save_results(df, cluster_summary)
    
    print("\\n" + "="*80)
    print("PROJECT COMPLETE!")
    print("="*80)


if __name__ == "__main__":
    main()
'''

# Save the Python script
with open('customer_segmentation.py', 'w') as f:
    f.write(python_script)

print("✓ Python script created: customer_segmentation.py")
