#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import numpy as np
import pickle

# Load the trained model
import joblib
model = joblib.load('model.pkl')

st.title("Bank Client Subscription Prediction App")
st.write("Predict whether a client will subscribe to a term deposit.")

# Define input fields for the 25 features
nr_employed = st.number_input("Number of employed in the economy (nr_employed)", value=5000.0)
pdays = st.number_input("Number of days since client was last contacted (pdays)", value=999)
euribor3m = st.number_input("Euribor 3 month rate", value=4.0)
emp_var_rate = st.number_input("Employment variation rate", value=0.0)
poutcome_nonexistent = st.number_input("poutcome_nonexistent (1=yes, 0=no)", min_value=0, max_value=1, value=1)
contact_telephone = st.number_input("contact_telephone (1=yes, 0=no)", min_value=0, max_value=1, value=0)
cons_price_idx = st.number_input("Consumer Price Index", value=93.0)
month_may = st.number_input("month_may (1=yes, 0=no)", min_value=0, max_value=1, value=0)
default_unknown = st.number_input("default_unknown (1=yes, 0=no)", min_value=0, max_value=1, value=1)
job_blue_collar = st.number_input("job_blue-collar (1=yes, 0=no)", min_value=0, max_value=1, value=0)
campaign = st.number_input("Number of contacts during this campaign (campaign)", value=1)
poutcome_success = st.number_input("poutcome_success (1=yes, 0=no)", min_value=0, max_value=1, value=0)
previous = st.number_input("Number of contacts performed before this campaign (previous)", value=0)
month_mar = st.number_input("month_mar (1=yes, 0=no)", min_value=0, max_value=1, value=0)
month_oct = st.number_input("month_oct (1=yes, 0=no)", min_value=0, max_value=1, value=0)
month_sep = st.number_input("month_sep (1=yes, 0=no)", min_value=0, max_value=1, value=0)
job_student = st.number_input("job_student (1=yes, 0=no)", min_value=0, max_value=1, value=0)
job_retired = st.number_input("job_retired (1=yes, 0=no)", min_value=0, max_value=1, value=0)
month_dec = st.number_input("month_dec (1=yes, 0=no)", min_value=0, max_value=1, value=0)
cons_conf_idx = st.number_input("Consumer Confidence Index", value=-40.0)
marital_single = st.number_input("marital_single (1=yes, 0=no)", min_value=0, max_value=1, value=0)
education_university = st.number_input("education_university.degree (1=yes, 0=no)", min_value=0, max_value=1, value=0)
age = st.number_input("Client's Age", value=30)
education_unknown = st.number_input("education_unknown (1=yes, 0=no)", min_value=0, max_value=1, value=0)
job_unemployed = st.number_input("job_unemployed (1=yes, 0=no)", min_value=0, max_value=1, value=0)

# Make prediction when user clicks button
if st.button("Predict"):
    input_data = np.array([[nr_employed, pdays, euribor3m, emp_var_rate, poutcome_nonexistent, contact_telephone, cons_price_idx,
                            month_may, default_unknown, job_blue_collar, campaign, poutcome_success, previous, month_mar, month_oct,
                            month_sep, job_student, job_retired, month_dec, cons_conf_idx, marital_single, education_university, age,
                            education_unknown, job_unemployed]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Prediction: The client is likely to subscribe.")
    else:
        st.error("Prediction: The client is not likely to subscribe.")


# In[ ]:




