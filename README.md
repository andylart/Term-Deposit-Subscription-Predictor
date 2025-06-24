<<<<<<< HEAD
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
=======
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

## 📊 EDA Highlights
Subscription Rate: A relatively small proportion of clients subscribed to the term deposit, indicating a class imbalance in the dataset.

Age Factor: Clients aged between 30 and 40 years were more likely to subscribe, while subscription rates declined for older clients.

Contact Duration: Call duration had a significant positive relationship with subscription; longer calls tended to lead to positive outcomes.

Previous Campaign Outcomes: Clients with a previous successful marketing outcome were more likely to subscribe again.

Pdays (Days since last contact): Clients contacted more recently (lower pdays values) showed a higher likelihood of subscribing.

Euribor 3-Month Rate (euribor3m): Higher euribor3m values were associated with lower subscription rates — indicating that during periods of higher interest rates in the broader economy, clients were less willing to commit to fixed-term deposits.

Employment Variation Rate (emp_var_rate): Lower emp_var_rate values correlated with higher subscription rates.

Consumer Confidence Index (cons_conf_idx): Higher consumer confidence led to increased likelihood of term deposit subscriptions.

Month of Contact (month): Campaigns executed in May, August, and October achieved higher subscription rates.

Contact Type (contact): Cellular communication channels showed higher success rates than telephone calls.

---

## 📌 Actionable Recommendations:
Prioritize clients aged 30–40 years in upcoming campaigns as they showed higher responsiveness.

Invest in longer, high-quality client calls, as call duration was a strong predictor of positive outcomes.

Focus on clients with previous positive campaign outcomes for higher success rates in follow-up campaigns.

Schedule calls during months with historically higher subscription rates (e.g. May, August, October).

Limit or reevaluate the use of telephone contact channels, which showed lower subscription rates compared to cellular.

Develop a lead scoring model incorporating these key variables to assist the marketing team in efficiently targeting high-potential clients.

Monitor macroeconomic indicators like employment variation rate (emp_var_rate) and consumer confidence (cons_conf_idx) — launching campaigns during periods of stable employment rates and higher consumer confidence may improve subscription rates.

Adjust campaign intensity during periods of high euribor3m rates — as higher interest rates correlate with lower subscription rates, marketing efforts may need to be adapted during such times.

---


## Deployment

This project is deployed as a Streamlit web application for real-time predictions.

🔗 [Click here to access the live app](https://term-deposit-subscription-predictor-ch9dca2w6fzpz268muchtx.streamlit.app/)

## 📌 Author
Andrew Lartey
>>>>>>> 5230a2a47a33ea9a6a7307feebc1abe670fc6532
