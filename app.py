import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load('model.pkl')

# Streamlit App UI
st.title("🏠 House Price Prediction App")
st.write("Predict the price of a house based on square footage, bedrooms, and bathrooms.")

# Input fields
sqft = st.number_input("Square Footage", min_value=100, max_value=10000, value=1500)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)

if st.button("Predict Price"):
    input_data = np.array([[sqft, bedrooms, bathrooms]])
    predicted_price = model.predict(input_data)[0]
    st.success(f"🏡 Estimated House Price: ${predicted_price:,.2f}")
