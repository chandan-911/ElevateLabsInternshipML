# 🏠 Housing Linear Regression

## 🎯 Objective  
Implement **simple and multiple linear regression** on the Housing dataset to predict house prices based on features like area, bedrooms, bathrooms, stories, and more. Evaluate the model's performance using standard regression metrics.

---

## 📁 Files

| File Name                   | Description                                                      |
|----------------------------|------------------------------------------------------------------|
| `Housing.csv`              | Original housing dataset                                         |
| `Housing-Regression.csv`   | Preprocessed dataset ready for modeling                          |

---

## 🔧 Steps Performed

### 1. **Loaded and Preprocessed Dataset**
- Loaded `Housing.csv` using `pandas`.
- Verified no missing values.
- **Encoded binary features** (`mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`, `prefarea`) into 0/1.
- Applied **one-hot encoding** on `furnishingstatus`.
- **Removed outliers** in `price` using the IQR method.
- **Standardized** numerical features:
  - `area`, `bedrooms`, `bathrooms`, `stories`, `parking`.

### 2. **Split Data**
- Split into **80% training** and **20% testing** using `train_test_split` with `random_state=42`.

### 3. **Simple Linear Regression**
- Built model using `area` as the only feature.
- Evaluated using:
  - **MAE** (Mean Absolute Error)
  - **MSE** (Mean Squared Error)
  - **R²** (Coefficient of Determination)
- Saved regression plot: `simple_regression.png`.

### 4. **Multiple Linear Regression**
- Trained model on **all features**.
- Evaluated using the same metrics.
- Printed **model coefficients** for interpretation.

### 5. **Saved Outputs**
- Preprocessed dataset saved as `Housing-Regression.csv`.

---

## ✅ Key Outcomes

### 📈 Simple Linear Regression:
- **MAE:** ~1,200,000 – 1,500,000  
- **MSE:** ~2 – 3 × 10¹²  
- **R²:** ~0.3 – 0.4  
  > *Area has a moderate impact on price, but is not sufficient alone.*

### 🧠 Multiple Linear Regression:
- **MAE:** ~800,000 – 1,000,000 (improved)
- **MSE:** ~1 – 1.5 × 10¹² (lower)
- **R²:** ~0.6 – 0.7 (higher)
- **Influential Features:** `area`, `bathrooms`, and `airconditioning` have strong positive coefficients.
  > *Using all features significantly improves prediction accuracy.*

### 📊 Visualization:
- The simple regression plot shows a **positive linear trend** between `area` and `price`.

---

## ▶️ How to Run

1. **Open Google Colab**.
2. **Upload `Housing.csv`:**
   - Click 📁 in the sidebar.
   - Click ⬆️ and select `Housing.csv`.
3. **Paste code from `housing_linear_regression.py` into a code cell.**
4. **Run all cells** using `Shift + Enter`.
5. **Download outputs:**
   - `Housing-Regression.csv`

---

## 🧰 Requirements

- Python libraries (already available in Colab):
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`

---

## 📝 Notes

- Ensure `Housing.csv` is uploaded to `/content/Housing.csv` in Colab.
- The script is well-commented and prints key **metrics** and **coefficients** for easy analysis.
- Simple regression provides limited insight; **multiple regression is more reliable**.
- Coefficient values help identify **key drivers** behind housing prices.

---

📌 **Use this analysis to better understand housing market trends and price influencers!**
