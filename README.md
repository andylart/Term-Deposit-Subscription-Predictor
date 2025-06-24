 📊 Term Deposit Subscription Predictor

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20App-brightgreen)](https://term-deposit-subscription-predictor-4wqffsiudqdcx5wzsd8rho.streamlit.app/)

## 📌 Objective  
Predict whether a bank client will subscribe to a term deposit based on demographic, campaign, and economic indicators using machine learning techniques.

---

## 📌 Approach  

**Exploratory Data Analysis (EDA):**
- Identified feature distributions, class imbalance, outliers, and feature correlations.

**Logistic Regression (Baseline Model):**
- Built with all available features.
- Conducted feature importance analysis via model coefficients.
- Removed low-impact features to simplify the model.
- Performance remained suboptimal, especially with class imbalance.

**Logistic Regression Results:**
- Accuracy: 0.89
- Precision: 0.58
- Recall: 0.16
- AUC: 0.78

**Random Forest Classifier:**
- Applied with the full feature set.
- Outperformed Logistic Regression but still struggled with imbalance.

**SMOTE (Synthetic Minority Over-sampling Technique):**
- Applied to balance the dataset.
- Retrained the Random Forest model.

**Post-SMOTE Random Forest Results:**
- Accuracy: 0.91
- Precision: 0.91
- Recall: 0.91

---

## 📊 EDA Highlights
- **Subscription Rate:** Relatively low, indicating class imbalance.
- **Age Factor:** Clients aged 30-40 showed higher subscription rates.
- **Contact Duration:** Longer calls led to better outcomes.
- **Previous Campaign Outcomes:** Positive outcomes increased likelihood of new subscriptions.
- **Euribor 3-Month Rate:** Higher rates correlated with lower subscriptions.
- **Employment Variation Rate:** Lower values improved subscription rates.
- **Consumer Confidence:** Higher confidence increased subscriptions.
- **Contact Type:** Cellular contacts performed better than telephone.
- **Month of Contact:** May, August, and October achieved higher subscription rates.

---

## 📌 Actionable Recommendations
- Prioritize clients aged 30–40.
- Invest in longer, quality calls.
- Focus on clients with positive prior campaign outcomes.
- Optimize campaigns for May, August, and October.
- Favor cellular channels over telephone.
- Track macroeconomic indicators like employment variation and consumer confidence.
- Adapt marketing strategies during high euribor periods.

---

## 📦 Final Deliverables
- `model.pkl` — Trained Random Forest model
- `app.py` — Streamlit web app for predictions
- `requirements.txt` — Project dependencies
- `runtime.txt` — Deployment runtime environment
- `README.md` — Project summary and documentation

---

## 📌 Deployment  
Deployed as a Streamlit web application for real-time predictions.

**🔗 [Click here to access the live app](https://term-deposit-subscription-predictor-4wqffsiudqdcx5wzsd8rho.streamlit.app/)**

---

## 📦 Deployment Update — June 24, 2025
✅ Model retrained using **scikit-learn 1.4.2**  
✅ Resolved prior deployment errors caused by version mismatches  
✅ Cleaned and standardized `requirements.txt` dependencies  
✅ Git merge conflicts fully resolved  
✅ Successful deployment on **Streamlit Cloud**

---

## 📌 Author  
Andrew Lartey  
