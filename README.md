# Cardiovascular Disease Prediction Analysis

This repository contains several Jupyter Notebooks that apply different tree-based ensemble models to predict the presence of cardiovascular disease based on patient health metrics.

All notebooks use the `cardio_train.csv` dataset.

---

## Data Preprocessing (Common Steps)

All five notebooks appear to follow a similar data preprocessing and feature engineering pipeline before modeling:

1.  **Load Data:** The `cardio_train.csv` dataset is loaded.
2.  **Age Normalization:** The `age` column (in days) is converted to years.
3.  **Outlier Removal:** Outliers are removed based on statistical properties (e.g., values outside 2.5% and 97.5% quantiles) for `height`, `weight`, `ap_hi` (systolic blood pressure), and `ap_lo` (diastolic blood pressure). Incorrect blood pressure readings (e.g., diastolic > systolic) are also filtered out.
4.  **Feature Engineering:** New features are created:
    * `pulse_pressure` = `ap_hi` - `ap_lo`
    * `map` (Mean Arterial Pressure) = `ap_lo` + (`ap_hi` - `ap_lo`) / 3
    * `bmi` (Body Mass Index) = `weight` / (`height` / 100)^2
    * `sys_dsys_ratio` = `ap_hi` / `ap_lo`
5.  **Oversampling (SMOTE):** The minority classes for categorical features (`cholesterol`, `gluc`, `smoke`, `alco`, `active`) are oversampled using SMOTE to create a more balanced dataset.
6.  **Encoding:** Ordinal features (`cholesterol`, `gluc`) are converted into categorical dummies.
7.  **Scaling:** Numerical features are standardized using `StandardScaler`.

---

## Model Performance Summary

After preprocessing, the data is split into training (80%) and testing (20%) sets. The following results were achieved on the test set:

### 1. `RandomForest_Cardio.ipynb`

* **Model:** Random Forest Classifier (`n_estimators=50`)
* **Test Accuracy:** **96.93%**
* **Test AUC:** 0.99

### 2. `ExtraTreeClassifier_Cardio.ipynb`

* **Model:** Extra Trees Classifier (`n_estimators=50`)
* **Test Accuracy:** **95.70%**
* **Test AUC:** 0.99

### 3. `CatBoost_Cardio.ipynb`

* **Model:** CatBoost Classifier (`iterations=100`, `depth=8`)
* **Test Accuracy:** 85.47%
* **Test AUC:** 0.93

### 4. `XGBoost_Cardio.ipynb`

* **Model:** XGBoost Classifier (`n_estimators=50`, `max_depth=5`)
* **Test Accuracy:** 82.80%
* **Test AUC:** 0.91

### 5. `GradientBoosting_Cardio.ipynb`

* **Model:** Gradient Boosting Classifier (`n_estimators=50`, `max_depth=1`)
* **Test Accuracy:** 78.59%
* **Test AUC:** 0.86
###ScreenShots
<img width="2209" height="1027" alt="image" src="https://github.com/user-attachments/assets/30f0fc4c-a28f-4b6b-8603-6cb523337406" />
<img width="2224" height="931" alt="image" src="https://github.com/user-attachments/assets/3a4676b1-8de2-48bc-9901-afa9dda1b978" />
<img width="2228" height="1165" alt="image" src="https://github.com/user-attachments/assets/ff9cde07-29a0-46ae-95b3-8d379eec9b12" />
