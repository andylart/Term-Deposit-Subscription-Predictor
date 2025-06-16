# 📊 Term Deposit Subscription Prediction

## 📌 Objective
Predict whether a bank client will subscribe to a term deposit based on demographic, campaign, and economic indicators using machine learning techniques.

---

## 📌 Approach

- **Exploratory Data Analysis (EDA):**  
  Identified feature distributions, class imbalance, outliers, and feature correlations.

- **Logistic Regression (Baseline Model):**  
  - Built with all available features.
  - Conducted feature importance analysis via model coefficients.
  - Removed low-impact features to simplify the model.
  - Performance remained suboptimal, especially with class imbalance.

**Logistic Regression Results:**
- **Accuracy:** 0.89  
- **Precision:** 0.58  
- **Recall:** 0.16  
- **AUC:** 0.78  

---

- **Random Forest Classifier:**  
  - Applied with the full feature set.
  - Outperformed Logistic Regression but still struggled with imbalance.

- **SMOTE (Synthetic Minority Over-sampling Technique):**  
  - Applied to balance the dataset.
  - Retrained the Random Forest model.

**Post-SMOTE Random Forest Results:**
- **Accuracy:** 0.91  
- **Precision:** 0.91  
- **Recall:** 0.91  

---

## 📌 Key Insights

- Class imbalance heavily impacted model performance.
- Random Forest with SMOTE significantly improved accuracy and recall.
- Key features included:
  - Employment variation rate
  - Previous campaign outcome
  - Economic indicators
  - Job roles
- Resampling techniques like SMOTE proved essential for imbalanced datasets.

---

## 📦 Final Deliverables

- `model.pkl` — Trained Random Forest model
- `app.py` — Streamlit web app for predictions
- `requirements.txt` — Project dependencies
- `README.md` — Project summary and documentation

---

## 📌 Deployment

Deployed as a Streamlit web application for real-time predictions.  
**To run locally:**

## 📌 Author
Andrew Lartey