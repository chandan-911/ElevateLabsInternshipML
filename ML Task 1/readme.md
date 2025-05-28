# Titanic Data Preprocessing

## 🎯 Objective  
Clean and preprocess the Titanic dataset to prepare it for machine learning by:
- Handling missing values  
- Encoding categorical variables  
- Standardizing numerical features  
- Detecting and removing outliers  

---

## 📁 Files

| File Name               | Description                                                  |
|------------------------|--------------------------------------------------------------|
| `Titanic-Dataset.csv`      | Original dataset                                             |
| `Titanic-Preprocessed.csv` | Final cleaned dataset                                        |

---

## 🔧 Steps Performed

### 1. **Loaded and Explored Dataset**
- Loaded `Titanic-Dataset.csv` using `pandas`.
- Displayed dataset info, missing values, and the first 5 rows.

### 2. **Handled Missing Values**
- `Age`: Filled missing values (177) with the **median** (28.0).
- `Cabin`: Dropped the column due to **77% missing values**.
- `Embarked`: Filled 2 missing values with the **mode** ('S').

### 3. **Encoded Categorical Variables**
- `Sex`: Label encoded (`male=0`, `female=1`).
- `Embarked`: One-hot encoded to create `Embarked_C`, `Embarked_Q`, and `Embarked_S`.
- Dropped `Name`, `Ticket`, and `PassengerId` (not useful for ML).

### 4. **Standardized Numerical Features**
- Standardized `Age`, `Fare`, `SibSp`, and `Parch` using `StandardScaler`.

### 5. **Detected and Removed Outliers**
- Used the **IQR method** to detect and remove outliers from `Age` and `Fare`.
- Visualized before and after using boxplots.

### 6. **Saved Preprocessed Dataset**
- Exported cleaned data to `Titanic-Preprocessed.csv`.

---

## ✅ Key Outcomes

- ✔️ No missing values remain.  
- ✔️ All categorical features are now numeric.  
- ✔️ Numerical features are standardized (mean = 0, std = 1).  
- ✔️ Outliers removed, reducing noise (e.g., extreme `Fare` values > 500).  
- ✔️ Visual confirmation via boxplots (`boxplots_before.png`, `boxplots_after.png`).

---

## ▶️ How to Run

1. **Open Google Colab.**
2. **Upload `Titanic-Dataset.csv`:**
   - Click the folder icon (left sidebar).
   - Click upload and select the CSV file.

3. **Copy and paste `titanic_preprocessing.py` contents into a code cell.**
4. **Run all cells sequentially** using `Shift + Enter`.
5. **Download Results:**
   - `Titanic-Preprocessed.csv`

---

## 🧰 Requirements

- Python libraries (pre-installed in Colab):
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`

---

## 📝 Notes

- Ensure the CSV is uploaded
