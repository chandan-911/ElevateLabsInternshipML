# 🎯 Task 8: Clustering with K-Means

## 📌 Objective
To perform unsupervised learning using **K-Means clustering** to segment customers based on attributes like age, gender, income, and spending score.

---

## 🛠 Tools & Libraries
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 📁 Dataset
**Mall Customers Dataset**  
- Features: Gender, Age, Annual Income (k$), Spending Score (1–100)  
- Task: Cluster similar customers without using labels

---

## 🔄 Workflow Summary

### ✅ Step 1: Data Preparation
- Loaded dataset and dropped `CustomerID`
- Converted categorical `Gender` column into numeric (Male=0, Female=1)
- Normalized data using `StandardScaler`

### ✅ Step 2: Elbow Method
- Calculated **inertia** (within-cluster sum of squares) for different K values
- Found optimal K using **Elbow point** on the plot

### ✅ Step 3: K-Means Clustering
- Applied `KMeans` with optimal K (e.g., K=5)
- Assigned each customer to a cluster
- Added cluster labels to dataset

### ✅ Step 4: PCA for 2D Visualization
- Reduced data to 2D using **Principal Component Analysis**
- Plotted clusters using `Seaborn` scatterplot with color-coding

### ✅ Step 5: Clustering Evaluation
- Used **Silhouette Score** to evaluate how well clusters are separated
- Higher score indicates better-defined clusters

---

## 📊 Results

| Metric             | Value     |
|--------------------|-----------|
| Optimal Clusters K | 5         |
| Silhouette Score   | ~0.45–0.55 (approx.) |
| Visualization      | Done with PCA |

---

## 📚 Key Concepts Learned

- **Unsupervised Learning**: No labels, grouping based on similarity
- **K-Means**: Clustering algorithm using centroids
- **Inertia**: Sum of squared distances from points to centroids
- **Elbow Method**: Plot of inertia vs. K to choose optimal clusters
- **Silhouette Score**: Score from -1 to 1 that shows cluster quality
- **PCA**: Technique to reduce high-dimensional data to 2D for visualization

---
## 💾 How to Run

1. Upload `Mall_Customers.csv` in Colab
2. Run the notebook step-by-step
3. Visualize clusters and note evaluation scores
4. Save results and optionally push to GitHub

---
