# 🌳 Task 5: Decision Trees and Random Forests

This project implements **Task 5** of the **AI & ML Internship**, focusing on **tree-based classification models** using the **Heart Disease Dataset**. The solution includes training a **Decision Tree Classifier**, analyzing overfitting, implementing a **Random Forest Classifier**, interpreting **feature importances**, and evaluating model performance via **cross-validation**.

---

## 📊 Dataset

- **Heart Disease Dataset**  
  Contains 13 features such as age, sex, cholesterol, etc., and a binary target variable:  
  - `0`: No heart disease  
  - `1`: Heart disease

---

## 📂 Files

| File                             | Description                                                               |
|----------------------------------|---------------------------------------------------------------------------|
| `Task_5_Heart_Disease_Analysis.ipynb` | Google Colab notebook with the complete analysis                      |
| `heart.csv`                      | Input dataset                                                             |
| `decision_tree.png`              | Visualization of the decision tree                                       |
| `overfitting_analysis.png`       | Plot of training vs. test accuracy for varying tree depths               |
| `feature_importance.png`         | Random Forest feature importance plot                                    |
| `results.txt`                    | Model accuracy, classification report, and cross-validation scores       |

---

## 💾 Requirements

### For Local Environment
- Python 3.x  
- Required libraries:
  ```bash
  pip install pandas numpy scikit-learn matplotlib seaborn python-graphviz
