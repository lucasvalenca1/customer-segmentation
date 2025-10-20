# Quick Start Guide

## Customer Segmentation Project - Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/customer-segmentation.git
cd customer-segmentation
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Using venv
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Project
```bash
python customer_segmentation.py
```

### Step 5: View Results
After running, check:
- `customer_segmentation_results.csv` - Full customer data with cluster assignments
- `cluster_summary.csv` - Statistical summary of each segment
- Terminal output for detailed analysis and recommendations

### Optional: Jupyter Notebook
```bash
jupyter notebook
# Open and run the analysis.ipynb notebook
```

## Key Files

- `customer_segmentation.py` - Main Python script
- `README.md` - Complete documentation
- `requirements.txt` - Python dependencies
- `customer_segmentation_results.csv` - Output data
- `cluster_summary.csv` - Segment statistics

## Expected Output

The script will:
1. Generate/load customer data (500 samples)
2. Perform exploratory data analysis
3. Scale features using StandardScaler
4. Run Elbow Method to find optimal K
5. Build K-Means model with K=4 clusters
6. Analyze and interpret segments
7. Generate business recommendations
8. Save results to CSV files

## Model Performance Metrics

- **Clusters**: 4 customer segments
- **Silhouette Score**: ~0.15
- **Cluster Distribution**: Balanced (21-27% each)

## Troubleshooting

**Issue**: ModuleNotFoundError  
**Solution**: Ensure virtual environment is activated and dependencies installed

**Issue**: File not found errors  
**Solution**: Run script from project root directory

**Issue**: Different results each run  
**Solution**: Random state is set to 42 for reproducibility

## Next Steps

1. Explore the generated CSV files
2. Modify features in the script for different segmentations
3. Integrate with your own customer data
4. Deploy insights to marketing team

For detailed information, see README.md
