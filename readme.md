# ElevateLabsInternshipML

This repository contains the solutions for the Machine Learning Internship tasks assigned by Elevate Labs. Each task focuses on a specific aspect of machine learning, from data preprocessing to unsupervised learning, using Python and relevant libraries like Pandas, Scikit-learn, Matplotlib, and Seaborn. Below is an overview of the tasks and their objectives.

## Task Overview

### Task 1: Data Cleaning & Preprocessing
- **Objective**: Clean and prepare raw data for machine learning.
- **Dataset**: Titanic Dataset
- **Key Steps**:
  - Imported and explored dataset for nulls and data types.
  - Handled missing values using mean/median imputation.
  - Encoded categorical features (e.g., one-hot encoding).
  - Normalized/standardized numerical features.
  - Visualized and removed outliers using boxplots.
- **Tools**: Python, Pandas, NumPy, Matplotlib, Seaborn
- **Files**: `task1_data_cleaning.py`, `titanic.csv`

### Task 2: Exploratory Data Analysis (EDA)
- **Objective**: Understand data through statistics and visualizations.
- **Dataset**: Titanic Dataset
- **Key Steps**:
  - Generated summary statistics (mean, median, std, etc.).
  - Created histograms and boxplots for numerical features.
  - Used pairplots and correlation matrices to explore feature relationships.
  - Identified patterns, trends, and anomalies.
  - Made feature-level inferences from visuals.
- **Tools**: Pandas, Matplotlib, Seaborn, Plotly
- **Files**: `task2_eda.py`, `titanic.csv`

### Task 3: Linear Regression
- **Objective**: Implement simple and multiple linear regression.
- **Dataset**: House Price Prediction Dataset
- **Key Steps**:
  - Preprocessed dataset and split into train-test sets.
  - Fitted a Linear Regression model using Scikit-learn.
  - Evaluated model using MAE, MSE, and R² metrics.
  - Plotted regression line and interpreted coefficients.
- **Tools**: Scikit-learn, Pandas, Matplotlib
- **Files**: `task3_linear_regression.py`, `house_prices.csv`

### Task 4: Classification with Logistic Regression
- **Objective**: Build a binary classifier using logistic regression.
- **Dataset**: Breast Cancer Wisconsin Dataset
- **Key Steps**:
  - Preprocessed dataset and standardized features.
  - Fitted a Logistic Regression model.
  - Evaluated with confusion matrix, precision, recall, and ROC-AUC.
  - Tuned classification threshold and explained sigmoid function.
- **Tools**: Scikit-learn, Pandas, Matplotlib
- **Files**: `task4_logistic_regression.py`, `breast_cancer.csv`

### Task 5: Decision Trees and Random Forests
- **Objective**: Implement tree-based models for classification and regression.
- **Dataset**: Heart Disease Dataset
- **Key Steps**:
  - Trained and visualized a Decision Tree Classifier.
  - Analyzed overfitting and controlled tree depth.
  - Trained a Random Forest and compared accuracy.
  - Interpreted feature importances.
  - Evaluated using cross-validation.
- **Tools**: Scikit-learn, Graphviz
- **Files**: `task5_decision_trees.py`, `heart_disease.csv`

### Task 6: K-Nearest Neighbors (KNN) Classification
- **Objective**: Implement KNN for classification problems.
- **Dataset**: Iris Dataset
- **Key Steps**:
  - Normalized features and trained KNeighborsClassifier.
  - Experimented with different K values.
  - Evaluated using accuracy and confusion matrix.
  - Visualized decision boundaries.
- **Tools**: Scikit-learn, Pandas, Matplotlib
- **Files**: `task6_knn.py`, `iris.csv`

### Task 7: Support Vector Machines (SVM)
- **Objective**: Use SVMs for linear and non-linear classification.
- **Dataset**: Breast Cancer Dataset
- **Key Steps**:
  - Trained SVM with linear and RBF kernels.
  - Visualized decision boundaries using 2D data.
  - Tuned hyperparameters (C and gamma).
  - Evaluated performance using cross-validation.
- **Tools**: Scikit-learn, NumPy, Matplotlib
- **Files**: `task7_svm.py`, `breast_cancer.csv`

### Task 8: Clustering with K-Means
- **Objective**: Perform unsupervised learning with K-Means clustering.
- **Dataset**: Mall Customer Segmentation Dataset
- **Key Steps**:
  - Loaded dataset and applied PCA for 2D visualization (optional).
  - Fitted K-Means and assigned cluster labels.
  - Used Elbow Method to find optimal K.
  - Visualized clusters with color-coding.
  - Evaluated clustering using Silhouette Score.
- **Tools**: Scikit-learn, Pandas, Matplotlib
- **Files**: `task8_kmeans.py`, `mall_customers.csv`

## Repository Structure
- `task1_data_cleaning.py`: Script for Task 1 (Data Cleaning & Preprocessing)
- `task2_eda.py`: Script for Task 2 (Exploratory Data Analysis)
- `task3_linear_regression.py`: Script for Task 3 (Linear Regression)
- `task4_logistic_regression.py`: Script for Task 4 (Logistic Regression)
- `task5_decision_trees.py`: Script for Task 5 (Decision Trees and Random Forests)
- `task6_knn.py`: Script for Task 6 (KNN Classification)
- `task7_svm.py`: Script for Task 7 (Support Vector Machines)
- `task8_kmeans.py`: Script for Task 8 (K-Means Clustering)
- `datasets/`: Directory containing datasets used (e.g., `titanic.csv`, `house_prices.csv`, etc.)
- `screenshots/`: Directory for any visualizations or outputs (if applicable)
- `README.md`: This file

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/chandan-911/ElevateLabsInternshipML.git
   ```
2. Install required dependencies:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn plotly graphviz
   ```
3. Navigate to the repository folder and run any task script:
   ```bash
   python task1_data_cleaning.py
   ```
4. Ensure the relevant dataset is in the `datasets/` folder before running each script.

## Notes
- Each task was completed following the provided guidelines, using free tools and self-researched resources.
- All scripts include comments explaining the code and steps.
- Screenshots of visualizations (if any) are included in the `screenshots/` folder.
- The datasets used are referenced in the task descriptions and stored in the `datasets/` folder.

## Submission
The GitHub repository link for submission is:  
[https://github.com/chandan-911/ElevateLabsInternshipML](https://github.com/chandan-911/ElevateLabsInternshipML)