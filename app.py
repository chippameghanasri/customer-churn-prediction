import streamlit as st
import joblib
import pandas as pd

model = joblib.load("model.pkl")

st.title("Customer Churn Prediction")

CreditScore = st.number_input("Credit Score")
Age = st.number_input("Age")
Tenure = st.number_input("Tenure")
Balance = st.number_input("Balance")
NumOfProducts = st.number_input("Num Of Products")
HasCrCard = st.selectbox("Has Credit Card", [0, 1])
IsActiveMember = st.selectbox("Is Active Member", [0, 1])
EstimatedSalary = st.number_input("Estimated Salary")

Gender_Male = st.selectbox("Gender Male", [0, 1])
Geography_Germany = st.selectbox("Germany", [0, 1])
Geography_Spain = st.selectbox("Spain", [0, 1])

if st.button("Predict"):

    data = pd.DataFrame([[

        CreditScore,
        Age,
        Tenure,
        Balance,
        NumOfProducts,
        HasCrCard,
        IsActiveMember,
        EstimatedSalary,
        Gender_Male,
        Geography_Germany,
        Geography_Spain

    ]],

    columns=[

        'CreditScore',
        'Age',
        'Tenure',
        'Balance',
        'NumOfProducts',
        'HasCrCard',
        'IsActiveMember',
        'EstimatedSalary',
        'Gender_Male',
        'Geography_Germany',
        'Geography_Spain'

    ])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Customer likely to churn")
    else:
        st.success("Customer likely to stay")

