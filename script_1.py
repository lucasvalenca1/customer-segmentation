
# Step 2: Check for missing values and data quality
print("\n2. Data Quality Check:")
print("Missing Values:")
print(df.isnull().sum())

# Step 3: Feature Selection for Clustering
# Select relevant features for segmentation
features = ['Annual_Income', 'Spending_Score', 'Purchase_Frequency', 
            'Average_Transaction_Value', 'Days_Since_Last_Purchase']

X = df[features]

print("\n3. Selected Features for Clustering:")
print(X.head())

# Step 4: Feature Scaling using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\n4. Feature Scaling Complete")
print("Scaled Features (first 5 rows):")
print(pd.DataFrame(X_scaled, columns=features).head())
print("\nMean of scaled features:", X_scaled.mean(axis=0).round(2))
print("Std of scaled features:", X_scaled.std(axis=0).round(2))
