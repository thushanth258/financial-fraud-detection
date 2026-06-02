import streamlit as st
import joblib
import numpy as np
import os

model_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "fraud_model.pkl"
)
print("Model path:", model_path)
print("Exists:", os.path.exists(model_path))

model = joblib.load(model_path)

st.title("Financial Fraud Detection System")

amount = st.number_input("Enter Transaction Amount")

if st.button("Predict"):

    features = [[0]*29 + [amount]]
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("Fraud Transaction Detected")
    else:
        st.success("Genuine Transaction")