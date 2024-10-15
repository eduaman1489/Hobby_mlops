import streamlit as st
import json
import numpy as np
import joblib

model_path = "regmodel.pkl"
model = joblib.load(model_path)

def predict(data):
    data = np.array(data).reshape(1, -1)
    prediction = model.predict(data)
    return prediction[0]

st.title("Diabetes Progression Prediction")
st.write("Enter the input data for the model:")

input_features = []
for i in range(10):  # As the model takes 10 features
    value = st.number_input(f"Feature {i + 1}", value=0.0)
    input_features.append(value)

if st.button("Predict"):
    input_data = {"data": [input_features]} # Data preparation as per the model
    prediction = predict(input_features)
    explanation = f"The model predicts a disease progression value of {prediction:.2f} one year after the baseline."
    st.success(f"Prediction: {prediction:.2f}")
    st.write(explanation)
