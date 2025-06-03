# 🌸 K-Nearest Neighbors (KNN) Classification on Iris Dataset

## 🎯 Objective
This project, part of the **AI & ML Internship (Task 6)**, applies the **K-Nearest Neighbors (KNN)** algorithm to the Iris dataset to predict flower species based on sepal and petal measurements. The analysis includes:

- Data preprocessing & normalization  
- Training KNN models with different K values  
- Accuracy evaluation & confusion matrix generation  
- Visualization of decision boundaries to understand KNN behavior

---

## 📊 Dataset Overview
The **Iris dataset (`Iris.csv`)** consists of **150** flower samples with the following attributes:

| Feature            | Description                            |
|--------------------|----------------------------------------|
| `SepalLengthCm`    | Sepal length in cm                     |
| `SepalWidthCm`     | Sepal width in cm                      |
| `PetalLengthCm`    | Petal length in cm                     |
| `PetalWidthCm`     | Petal width in cm                      |
| `Species`          | Iris-setosa, Iris-versicolor, Iris-virginica |
| `Id`               | Unique identifier (dropped)            |

---

## 🛠️ Tools & Libraries
- 📚 **Pandas** – Data handling & preprocessing  
- 📦 **Scikit-learn** – Model training, scaling, and evaluation  
- 📈 **Matplotlib & Seaborn** – Visualization  
- ☁️ **Google Colab** – Execution environment  
- 🐍 **Python** – Programming language

---

## 🔍 Methodology

### ✅ 1. Data Cleaning
- Removed the `Id` column
- Confirmed no missing values
- Applied `StandardScaler` for feature normalization

### 🤖 2. Model Training
- Split data: **70% training / 30% testing**
- Trained KNN models with: **K = [1, 3, 5, 7, 9, 11, 15]**

### 📏 3. Evaluation
- Accuracy measured for each K value
- Confusion matrices created for error analysis

### 🧠 4. Visualizations
- 📉 **Accuracy Plot**: Accuracy vs. K  
- 🔢 **Confusion Matrices**: K=1 to K=15  
- 🌈 **Decision Boundaries**: For K=1, 5, 15 using `PetalLengthCm` & `PetalWidthCm`

---

## 📁 Project Files

| File                                | Description                                       |
|-------------------------------------|---------------------------------------------------|
| `iris_knn_classification.ipynb`     | Complete Jupyter Notebook                         |
| `Iris.csv`                          | Input dataset                                     |

---

## 📌 Key Observations
- 🔹 **Accuracy**: Peaks around **K=5 to K=11**, typically **>95%**
- 🔹 **Confusion**: Minor misclassification between *versicolor* and *virginica*
- 🔹 **Boundaries**:  
  - **K=1**: Overfits with jagged boundaries  
  - **K=15**: Smooth, generalized regions

---

## 💡 Feature-Level Inferences
- 🌟 `PetalLengthCm` & `PetalWidthCm` are the most informative features
- ⚖️ Normalization is critical to avoid scale dominance
- 📐 Best performance observed with **K between 5–9**

---

## ▶️ How to Run

1. Open 🔗 [Google Colab](https://colab.research.google.com/)
2. Upload the following:
   - `iris_knn_classification.ipynb`
   - `Iris.csv`
3. Run all cells to:
   - Preprocess data
   - Train & evaluate KNN models
   - Generate outputs: accuracy plot, confusion matrices, and decision boundaries
4. 📦 Download the `outputs` folder for submission

---

## ✅ Submission
This repository contains all necessary files and visualizations for **Task 6** of the AI & ML Internship. It demonstrates effective use of the KNN algorithm for multi-class classification with insightful visual analysis and interpretation.

---

> 🔗 *“Data will talk to you if you’re willing to listen.” – Jim Bergeson*
