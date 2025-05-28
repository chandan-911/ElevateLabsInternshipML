# Titanic Exploratory Data Analysis (EDA)

## 🎯 Objective  
Perform exploratory data analysis on the Titanic dataset to understand its structure, distributions, relationships, and patterns using statistics and visualizations.

---

## 📁 Files

| File Name                  | Description                                                       |
|---------------------------|-------------------------------------------------------------------|
| `Titanic-Dataset.csv`     | Original Titanic dataset                                          |
| `Titanic-EDA.csv`         | Optional saved dataset after EDA                                   |

---

## 🔧 Steps Performed

### 1. **Loaded Dataset**
- Loaded `Titanic-Dataset.csv` using `pandas`.

### 2. **Generated Summary Statistics**
- Computed descriptive statistics (mean, median, std) for numerical features (`Age`, `Fare`, `SibSp`, `Parch`).
- Summarized categorical features (`Sex`, `Embarked`, `Pclass`) using value counts.

### 3. **Created Histograms and Boxplots**
- Visualized distribution of numerical features via **histograms**.
- Used **boxplots** to examine spread and detect outliers.

### 4. **Explored Feature Relationships**
- Generated **pairplot** to observe relationships between numerical features, colored by `Survived`.
- Created **correlation matrix heatmap** to check for numerical relationships.

### 5. **Analyzed Patterns and Trends**
- Plotted survival counts by:
  - `Sex`
  - `Pclass`
- Plotted:
  - `Age` distribution by survival status
  - `Fare` distribution by survival status

### 6. **Saved Visualizations and Findings**
- Printed key insights for documentation.

---

## ✅ Key Findings

- 📊 **Distributions:**  
  - `Age` and `Fare` are **right-skewed**.  
  - `SibSp` and `Parch` contain many **zeros**.

- 🚨 **Outliers:**  
  - `Fare` has extreme values (e.g., >500) — possible luxury tickets or data anomalies.

- 🔗 **Correlations:**  
  - Weak correlation overall between numerical features.  
  - Moderate positive correlation between `SibSp` and `Parch` (~0.41).

- ♀️ **Patterns:**  
  - **Females** and **1st class passengers** have **higher survival rates**.

- 📈 **Trends:**  
  - **Younger passengers** and those who paid **higher fares** had better survival chances.

- ❗ **Anomalies:**  
  - Some passengers with **zero fare** — could be crew or special passengers.

---

## ▶️ How to Run

1. **Open Google Colab.**
2. **Upload `Titanic-Dataset.csv`:**
   - Click the 📁 folder icon on the left.
   - Click the upload button and select the dataset.

3. **Copy and paste the contents of `titanic_eda.py` into a code cell.**
4. **Run all cells sequentially** using `Shift + Enter`.
5. **Download Results:**
   - Visual PNGs like `histograms.png`, `boxplots.png`, `pairplot.png`, etc.

---

## 🧰 Requirements

- Python libraries (pre-installed in Colab):
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `plotly`

---

## 📝 Notes

- Ensure the CSV is uploaded to `/content/Titanic-Dataset.csv` in Colab.
- The script contains **comments** and **print statements** for tracking progress.
- All visualizations are saved as **PNGs**, suitable for documentation or GitHub repos.
- Findings can inform **feature selection** and **model development** in machine learning.

---

🔍 Dive deep to predict who survived the Titanic!
