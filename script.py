
# Customer Segmentation Using K-Means Clustering
# A complete project for GitHub portfolio

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# Step 1: Create synthetic customer data (you can replace this with real data)
np.random.seed(42)

# Generate realistic customer behavior data
n_customers = 500

data = {
    'CustomerID': range(1, n_customers + 1),
    'Age': np.random.randint(18, 70, n_customers),
    'Annual_Income': np.random.randint(20000, 150000, n_customers),
    'Spending_Score': np.random.randint(1, 100, n_customers),
    'Purchase_Frequency': np.random.randint(1, 50, n_customers),
    'Average_Transaction_Value': np.random.randint(20, 500, n_customers),
    'Days_Since_Last_Purchase': np.random.randint(1, 365, n_customers)
}

df = pd.DataFrame(data)

print("="*60)
print("CUSTOMER SEGMENTATION PROJECT")
print("="*60)
print("\n1. Dataset Overview:")
print(df.head(10))
print("\nDataset Shape:", df.shape)
print("\nDataset Info:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())
