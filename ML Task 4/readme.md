# 🧠 Task 4: Classification with Logistic Regression

This repository contains the solution for **Task 4 of the AI & ML Internship**, implementing a **binary classifier** using **logistic regression** on the **Breast Cancer Wisconsin Dataset**.

---

## 📁 Contents

| File Name                            | Description                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------|
| `data.csv`                          | Breast Cancer Wisconsin dataset                                             |               |

---

## 📝 Task Description

- Developed a **logistic regression model** to classify breast cancer as **Malignant (M)** or **Benign (B)**.
- Preprocessed the dataset:
  - Standardized numerical features.
  - Split the dataset into training and testing sets (typically 80/20).
- Evaluated the model using:
  - **Confusion Matrix**
  - **Precision, Recall, Accuracy**
  - **ROC Curve** and **AUC Score**
- Plotted the **sigmoid function** to illustrate decision boundary logic.
- Tuned the **classification threshold** to explore trade-offs between precision and recall.

---

## ▶️ How to Run

1. **Install dependencies** (if not already installed):
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn
