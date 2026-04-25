import streamlit as st
import pandas as pd
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))
model_columns = pickle.load(open('columns.pkl', 'rb'))

st.title("Customer Churn Predictor")
st.write("Enter customer details to check if they will leave or stay.")

age = st.number_input("Age", min_value=18, max_value=100, value=30)
services = st.number_input("Services Opted", min_value=1, max_value=10, value=2)
frequent_flyer = st.selectbox("Frequent Flyer?", ["No", "Yes", "Yes, Frequent"])
income = st.selectbox("Annual Income Class", ["Low", "Middle", "High"])
social_media = st.selectbox("Account Synced to Social Media?", ["No", "Yes"])
hotel_booking = st.selectbox("Booked Hotel or Not?", ["No", "Yes"])

if st.button("Predict"):
    input_data = pd.DataFrame([[age, services, frequent_flyer, income, social_media, hotel_booking]], 
                              columns=['Age', 'ServicesOpted', 'FrequentFlyer', 'AnnualIncomeClass', 'AccountSyncedToSocialMedia', 'BookedHotelOrNot'])
    
    input_encoded = pd.get_dummies(input_data)
    final_input = pd.DataFrame(0, index=[0], columns=model_columns)
    
    for col in input_encoded.columns:
        if col in final_input.columns:
            final_input[col] = input_encoded[col]

    prediction = model.predict(final_input)
    
    if prediction[0] == 1:
        st.error("Prediction: Customer might CHURN!")
    else:
        st.success("Prediction: Customer will STAY!")
