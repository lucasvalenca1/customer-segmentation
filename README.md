# 🛍️ Customer Segmentation Using K-Means Clustering

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## 📋 Project Overview

This project demonstrates **customer segmentation** using machine learning to identify distinct customer groups and enable data-driven marketing strategies. Built with Python and scikit-learn, it showcases the complete workflow from data preprocessing to actionable business insights.

### 🎯 Key Objectives
- Segment customers based on behavioral and demographic data
- Apply K-Means clustering algorithm with optimal cluster selection
- Generate actionable business recommendations for each segment
- Demonstrate proficiency in predictive analytics and data visualization

---

## 🚀 Features

✅ **Complete ML Pipeline**: Data preprocessing, feature scaling, model training, and evaluation  
✅ **Elbow Method**: Systematic approach to determine optimal number of clusters  
✅ **Silhouette Analysis**: Model quality assessment and validation  
✅ **Business Insights**: Detailed segment profiles with marketing recommendations  
✅ **Visualization**: Charts showing cluster characteristics and distributions  
✅ **Production-Ready**: Modular, well-documented code following best practices

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **scikit-learn**: K-Means clustering, StandardScaler, metrics
- **pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib & Seaborn**: Data visualization
- **Jupyter Notebook**: Interactive development

---

## 📊 Project Workflow

### 1️⃣ Data Preparation
- Load customer transaction and demographic data
- Handle missing values and outliers
- Feature engineering and selection

### 2️⃣ Feature Scaling
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```
**Why?** K-Means is distance-based and sensitive to feature scales.

### 3️⃣ Optimal Cluster Selection
- **Elbow Method**: Plot inertia (WCSS) vs. number of clusters
- **Silhouette Score**: Measure cluster quality and separation
- Selected **K=4** for optimal balance

### 4️⃣ Model Training
```python
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42)
clusters = kmeans.fit_predict(X_scaled)
```

### 5️⃣ Cluster Analysis & Interpretation
Identified 4 distinct customer segments with unique characteristics.

---

## 📈 Results

### Customer Segments Identified

| Segment | Name | % of Base | Key Characteristics | Strategy |
|---------|------|-----------|---------------------|----------|
| **Cluster 0** | At-Risk Customers | 21.8% | Low engagement, 255 days since purchase | Re-engagement campaigns |
| **Cluster 1** | Premium Loyal | 25.8% | High income ($114K), frequent buyers | VIP rewards program |
| **Cluster 2** | Active Shoppers | 26.6% | Recent activity, high spending score | Cross-selling opportunities |
| **Cluster 3** | Budget-Conscious | 25.8% | Price-sensitive, frequent purchasers | Value deals and discounts |

### Model Performance
- **Inertia (WCSS)**: 1,670.65
- **Silhouette Score**: 0.1507
- **Cluster Balance**: Well-distributed segments (21-27% each)

---

## 📁 Project Structure

```
customer-segmentation/
│
├── customer_segmentation.py          # Main Python script
├── customer_segmentation_results.csv # Clustered customer data
├── cluster_summary.csv                # Segment statistics
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
│
├── notebooks/
│   └── analysis.ipynb                 # Jupyter notebook with detailed analysis
│
└── visualizations/
    ├── elbow_plot.png                 # Optimal K selection
    ├── silhouette_scores.png          # Model quality metrics
    ├── cluster_comparison.png         # Segment characteristics
    └── distribution_pie.png           # Customer distribution
```

---

## 🎯 Business Recommendations

### 🔴 Cluster 0: At-Risk Customers (21.8%)
**Problem**: Low engagement, haven't purchased in 255+ days  
**Actions**:
- Send personalized win-back email campaigns
- Offer 15-20% discount on next purchase
- Conduct exit surveys to understand churn reasons
- Create urgency with limited-time offers

### 🟢 Cluster 1: Premium Loyal Customers (25.8%)
**Strength**: High income, frequent purchases  
**Actions**:
- Launch VIP loyalty program with exclusive benefits
- Provide early access to new products
- Assign dedicated account managers
- Implement referral incentive program

### 🔵 Cluster 2: Active High-Engagement Shoppers (26.6%)
**Strength**: Recent activity, high spending score  
**Actions**:
- Recommend complementary products (cross-selling)
- Create attractive product bundles
- Increase purchase frequency with rewards
- Encourage mobile app adoption

### 🟡 Cluster 3: Budget-Conscious Regular Customers (25.8%)
**Profile**: Lower income but highly frequent  
**Actions**:
- Highlight best-value products
- Offer bulk purchase discounts
- Implement points-based loyalty program
- Provide flexible payment options

---

## 🚀 Getting Started

### Prerequisites
```bash
python >= 3.8
pip >= 21.0
```

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/customer-segmentation.git
cd customer-segmentation

# Install dependencies
pip install -r requirements.txt
```

### Run the Project
```bash
# Run the main script
python customer_segmentation.py

# Or use Jupyter Notebook
jupyter notebook notebooks/analysis.ipynb
```

---

## 📦 Dependencies

```
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
jupyter>=1.0.0
```

---

## 🔍 Key Learnings

1. **Feature Scaling is Critical**: K-Means requires standardized features for optimal performance
2. **Multiple Evaluation Metrics**: Combined Elbow Method and Silhouette Score for robust cluster selection
3. **Business Context Matters**: Technical accuracy must align with actionable business insights
4. **Interpretability**: 4 clusters provide better interpretability than 10+ micro-segments

---

## 🎓 Skills Demonstrated

✅ **Machine Learning**: Unsupervised learning, K-Means clustering  
✅ **Data Preprocessing**: Feature scaling, StandardScaler  
✅ **Model Evaluation**: Inertia, Silhouette Score, Elbow Method  
✅ **Data Analysis**: pandas, NumPy statistical operations  
✅ **Visualization**: Matplotlib, Seaborn for insights communication  
✅ **Business Acumen**: Translating technical results into strategic recommendations  
✅ **Python Best Practices**: Modular code, documentation, version control

---

## 📊 Visualizations

### Elbow Method
![Elbow Plot](visualizations/elbow_plot.png)
*Optimal number of clusters identified at K=4 where inertia decrease slows*

### Cluster Characteristics
![Cluster Comparison](visualizations/cluster_comparison.png)
*Comparative analysis of segment behavioral patterns*

### Customer Distribution
![Distribution](visualizations/distribution_pie.png)
*Balanced distribution across four customer segments*

---

## 🔮 Future Enhancements

- [ ] Implement RFM (Recency, Frequency, Monetary) analysis
- [ ] Add predictive churn modeling using classification algorithms
- [ ] Create interactive dashboard with Streamlit/Plotly
- [ ] Deploy model as REST API using Flask/FastAPI
- [ ] A/B testing framework for marketing campaign effectiveness
- [ ] Time-series analysis of segment evolution

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](https://github.com/yourusername/customer-segmentation/issues).

---

## 👤 Author

**Your Name**  
- GitHub: [@yourusername](https://github.com/yourusername)  
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)  
- Email: your.email@example.com

---

## 📝 License

This project is [MIT](https://opensource.org/licenses/MIT) licensed.

---

## 🙏 Acknowledgments

- Dataset inspired by UCI Machine Learning Repository
- scikit-learn documentation and community
- Worship.Works for the inspiration to apply data science in impactful ways

---

## 📚 References

- [scikit-learn K-Means Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
- [Elbow Method for Optimal K](https://www.geeksforgeeks.org/elbow-method-for-optimal-value-of-k-in-kmeans/)
- [Customer Segmentation Best Practices](https://www.datacamp.com/tutorial/k-means-clustering-python)
- [StandardScaler Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)

---

**⭐ If you find this project helpful, please consider giving it a star!**
