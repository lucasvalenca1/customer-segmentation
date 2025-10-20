
# Step 8: Analyze and Interpret Each Cluster
print("\n8. Cluster Analysis & Customer Segment Profiles:")
print("="*80)

cluster_summary = df.groupby('Cluster')[features].mean()
print("\nAverage Characteristics of Each Cluster:")
print(cluster_summary.round(2))

# Create detailed segment profiles
print("\n" + "="*80)
print("DETAILED CUSTOMER SEGMENT PROFILES")
print("="*80)

for cluster in range(optimal_k):
    cluster_data = df[df['Cluster'] == cluster][features].mean()
    print(f"\n{'='*80}")
    print(f"CLUSTER {cluster} - Customer Segment Profile ({cluster_counts[cluster]} customers, {(cluster_counts[cluster]/len(df)*100):.1f}%)")
    print(f"{'='*80}")
    print(f"  Annual Income:              ${cluster_data['Annual_Income']:,.2f}")
    print(f"  Spending Score:             {cluster_data['Spending_Score']:.1f}/100")
    print(f"  Purchase Frequency:         {cluster_data['Purchase_Frequency']:.1f} times")
    print(f"  Avg Transaction Value:      ${cluster_data['Average_Transaction_Value']:.2f}")
    print(f"  Days Since Last Purchase:   {cluster_data['Days_Since_Last_Purchase']:.1f} days")
    
    # Segment characterization
    if cluster == 0:
        print(f"\n  SEGMENT NAME: 'High-Value Frequent Buyers'")
        print(f"  CHARACTERISTICS: Premium customers with high spending and frequent purchases")
    elif cluster == 1:
        print(f"\n  SEGMENT NAME: 'Budget Conscious Shoppers'")
        print(f"  CHARACTERISTICS: Lower income with moderate spending patterns")
    elif cluster == 2:
        print(f"\n  SEGMENT NAME: 'Inactive/Churned Customers'")
        print(f"  CHARACTERISTICS: Haven't purchased recently, at risk of churn")
    elif cluster == 3:
        print(f"\n  SEGMENT NAME: 'Occasional High-Spenders'")
        print(f"  CHARACTERISTICS: Infrequent but valuable when they purchase")
