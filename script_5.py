
# Step 9: Create actionable business recommendations
print("\n\n" + "="*80)
print("9. BUSINESS RECOMMENDATIONS & MARKETING STRATEGIES")
print("="*80)

recommendations = {
    0: """
    Cluster 0 - 'At-Risk Customers' (21.8% of customer base)
    --------------------------------------------------------
    ISSUE: Low spending score (27.5/100) and long time since last purchase (255 days)
    
    RECOMMENDATIONS:
    • Re-engagement Campaign: Send personalized win-back offers
    • Special Discount: Offer 15-20% discount on next purchase
    • Survey: Understand why they stopped engaging
    • Email Marketing: Newsletter with new products/features
    • Urgency: Limited-time offers to create FOMO
    
    EXPECTED IMPACT: Recover 30-40% of at-risk customers
    """,
    
    1: """
    Cluster 1 - 'Premium Loyal Customers' (25.8% of customer base)
    --------------------------------------------------------------
    STRENGTH: Highest income ($114,806), frequent buyers (35.9 times/year)
    
    RECOMMENDATIONS:
    • VIP Program: Create exclusive loyalty program with premium benefits
    • Early Access: Give first access to new products/sales
    • Personal Shopping: Assign dedicated account manager
    • Upselling: Recommend premium/complementary products
    • Referral Program: Incentivize them to bring new customers
    
    EXPECTED IMPACT: Increase customer lifetime value by 25-35%
    """,
    
    2: """
    Cluster 2 - 'Active High-Engagement Shoppers' (26.6% of customer base)
    ----------------------------------------------------------------------
    STRENGTH: Recent purchases (110 days), high spending score (61.8/100)
    
    RECOMMENDATIONS:
    • Cross-Selling: Recommend related products they haven't tried
    • Bundle Offers: Create attractive product bundles
    • Frequency Rewards: Points for every purchase to boost frequency
    • Social Proof: Showcase reviews and testimonials
    • Mobile App: Encourage app downloads for easier shopping
    
    EXPECTED IMPACT: Increase purchase frequency by 40-50%
    """,
    
    3: """
    Cluster 3 - 'Budget-Conscious Regular Customers' (25.8% of customer base)
    -------------------------------------------------------------------------
    PROFILE: Lower income ($51,383) but highly frequent (37.6 times/year)
    
    RECOMMENDATIONS:
    • Value Deals: Highlight best-value products and promotions
    • Bulk Discounts: Offer savings on larger quantities
    • Loyalty Points: Reward program that accumulates to discounts
    • Budget-Friendly Options: Showcase affordable alternatives
    • Payment Plans: Offer installment options for larger purchases
    
    EXPECTED IMPACT: Increase average transaction value by 20-30%
    """
}

for cluster_id, recommendation in recommendations.items():
    print(recommendation)

print("\n" + "="*80)
