import streamlit as st
import joblib
import numpy as np
import os

# Check for model
if not os.path.exists("model.pkl"):
    st.error("❌ model.pkl not found. Please upload or train the model.")
    st.stop()

# Load model
model = joblib.load("model.pkl")

# App UI
st.set_page_config(page_title="House Price Predictor 🏠", layout="centered")

st.title("🏠 House Price Prediction (in ₹ INR)")
st.markdown("Predict the estimated price of a house based on area demographics using a machine learning model.")

st.markdown("---")

# Create input sections with columns
col1, col2 = st.columns(2)

with col1:
    income = st.number_input("🧾 Avg. Area Income (₹)", min_value=10000.0, max_value=200000.0, value=50000.0, step=1000.0)
    house_age = st.slider("📅 Avg. House Age (years)", 0.0, 20.0, 5.0)

with col2:
    rooms = st.slider("🛏️ Avg. Number of Rooms", 1.0, 10.0, 5.0)
    bedrooms = st.slider("🛌 Avg. Number of Bedrooms", 1.0, 10.0, 3.0)
    population = st.number_input("👥 Area Population", min_value=100.0, max_value=100000.0, value=30000.0, step=1000.0)

st.markdown("---")

if st.button("🔍 Predict Price"):
    input_data = np.array([[income, house_age, rooms, bedrooms, population]])
    predicted_price = model.predict(input_data)[0]

    st.success(f"💰 **Estimated Price:** ₹ {predicted_price:,.2f}")
    st.markdown(
        f"""
        ### 📋 Summary:
        - **Income:** ₹{income:,.0f}
        - **House Age:** {house_age} years  
        - **Rooms:** {rooms}  
        - **Bedrooms:** {bedrooms}  
        - **Population:** {population:,.0f}
        """
    )
