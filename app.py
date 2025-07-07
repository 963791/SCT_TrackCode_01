import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('model.pkl')

# UI
st.title("🏡 House Price Prediction")
st.write("Enter the details below to predict the house price:")

income = st.number_input("Average Area Income", min_value=10000.0, max_value=200000.0, value=50000.0)
house_age = st.number_input("Average Area House Age", min_value=0.0, max_value=20.0, value=5.0)
rooms = st.number_input("Average Area Number of Rooms", min_value=1.0, max_value=10.0, value=5.0)
bedrooms = st.number_input("Average Area Number of Bedrooms", min_value=1.0, max_value=10.0, value=3.0)
population = st.number_input("Area Population", min_value=100.0, max_value=100000.0, value=30000.0)

if st.button("Predict Price"):
    input_data = np.array([[income, house_age, rooms, bedrooms, population]])
    predicted_price = model.predict(input_data)[0]
    st.success(f"💰 Predicted House Price: ${predicted_price:,.2f}")

