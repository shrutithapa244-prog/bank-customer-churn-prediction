import streamlit as st
import pandas as pd
import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "Model", "churn_model.pkl")
scaler_path = os.path.join(BASE_DIR, "Model", "scaler.pkl")

model = pickle.load(open(model_path, "rb"))
scaler = pickle.load(open(scaler_path, "rb"))

st.title("Bank Customer Churn Prediction System")
st.markdown(
    "Enter customer information below to predict whether the customer is likely to leave the bank."
)

credit_score = st.number_input(
    "Credit Score",
    min_value=300,
    max_value=900,
    value=650
)

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=35
)

balance = st.number_input(
    "Balance",
    value=50000.0
)

num_products = st.number_input(
    "Number of Products",
    min_value=1,
    max_value=4,
    value=1
)

active_member = st.selectbox(
    "Active Member",
    ["No", "Yes"]
)

tenure = st.number_input(
    "Tenure (Years with Bank)",
    min_value=0,
    max_value=10,
    value=5
)

has_card = st.selectbox(
    "Has Credit Card",
    ["No", "Yes"]
)

estimated_salary = st.number_input(
    "Estimated Salary",
    value=50000.0
)

geography = st.selectbox(
    "Geography",
    ["France", "Germany", "Spain"]
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

if st.button("Predict Churn"):

    active_member_num = 1 if active_member == "Yes" else 0
    has_card_num = 1 if has_card == "Yes" else 0

    geography_germany = 1 if geography == "Germany" else 0
    geography_spain = 1 if geography == "Spain" else 0

    gender_male = 1 if gender == "Male" else 0

    input_data = pd.DataFrame({
        'CreditScore': [credit_score],
        'Age': [age],
        'Tenure': [tenure],
        'Balance': [balance],
        'NumOfProducts': [num_products],
        'HasCrCard': [has_card_num],
        'IsActiveMember': [active_member_num],
        'EstimatedSalary': [estimated_salary],
        'Geography_Germany': [geography_germany],
        'Geography_Spain': [geography_spain],
        'Gender_Male': [gender_male]
    })

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)
    
    probability = model.predict_proba(input_scaled)
    
    risk = probability[0][1] * 100
    
    st.write(
    f"Churn Probability: {risk:.2f}%"
    )
    if prediction[0] == 1:
        st.error("Customer Will Churn")
    else:
        st.success("Customer Will Stay")
    if risk < 30:
        st.success("Low Risk")
    elif risk < 70:
        st.warning("Medium Risk")
    else:
        st.error("High Risk")