# 🎯 Task 7: Support Vector Machines (SVM) & Non-SVM Comparison

## 📌 Objective
To compare Support Vector Machine (SVM) models with non-SVM models for binary classification using the Breast Cancer dataset.

---

## 🛠 Tools & Libraries
- Python, NumPy, Pandas
- Scikit-learn
- Matplotlib, Seaborn

---

## 📁 Dataset
**Breast Cancer Dataset**  
- Target: `diagnosis` — Malignant (1) or Benign (0)
- Features: 30 numeric values (e.g., radius_mean, texture_mean, etc.)

---

## 🔄 Workflow Summary

### ✅ Data Preprocessing
- Removed irrelevant columns (`id`, `Unnamed: 32`)
- Converted diagnosis (M, B) to binary
- Normalized features using `StandardScaler`

---

## 🔍 Models Used

### 🔹 SVM Models
- SVM with Linear Kernel
- SVM with RBF Kernel
- PCA visualization of linear decision boundary

### 🔹 Non-SVM Models
- Logistic Regression
- K-Nearest Neighbors (KNN)

---

## 📊 Model Accuracy Comparison

| Model               | Accuracy |
|---------------------|----------|
| SVM (Linear)        | ~96%     |
| SVM (RBF)           | ~98%     |
| Logistic Regression | ~96%     |
| K-Nearest Neighbors | ~95%     |

---

## 🧪 Evaluation Metrics
- Accuracy Score
- Confusion Matrix
- Precision, Recall, F1-Score
- PCA for decision boundary visualization

---

## 💾 How to Run

1. Upload `breast-cancer.csv` in Colab
2. Run cells in sequence
3. Observe results and visualizations
4. Optionally push code + `README.md` to GitHub

---

