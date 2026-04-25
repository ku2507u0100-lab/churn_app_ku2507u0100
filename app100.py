import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('model100.pkl', 'rb'))
model_columns = pickle.load(open('columns.pkl', 'rb'))

st.title("Customer Churn Predictor")
# ... baki ka pura app code jo maine pehle diya tha ...
