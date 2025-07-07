# SCT_TrackCode_01
# 🏡 House Price Prediction Web App

This project is a **Streamlit web application** that predicts house prices based on area demographics using a **Linear Regression** model. It uses a dataset from Kaggle that includes features such as average area income, house age, number of rooms, number of bedrooms, and population.

---

## 📊 Features

- Input area-specific details (income, house age, rooms, bedrooms, population)
- Predict house price instantly
- Built with `scikit-learn`, `pandas`, and `Streamlit`

---

## 📁 Dataset

- Dataset: [Kaggle - housing.csv](https://www.kaggle.com/datasets/huyngohoang/housingcsv)
- Key columns used:
  - `Avg. Area Income`
  - `Avg. Area House Age`
  - `Avg. Area Number of Rooms`
  - `Avg. Area Number of Bedrooms`
  - `Area Population`
  - `Price` (target)

---

## 🛠️ Installation

1. **Clone the repository** (or upload manually to GitHub):
   ```bash
   git clone https://github.com/your-username/house-price-prediction-streamlit.git
   cd house-price-prediction-streamlit
2 Install dependencies:

bash
Copy code
pip install -r requirements.txt
3. Train the model:

bash
Copy code
python train_model.py
4 Run the app:

bash
Copy code
streamlit run app.py
🌐 Streamlit Cloud Deployment (Optional)
Push the code to a GitHub repository.

Visit https://streamlit.io/cloud.

Connect your GitHub and select the repo.

Set app.py as the main entry point.

Deploy and get your shareable live link!

📦 Requirements
streamlit

scikit-learn

pandas

numpy

joblib

Install them using:

bash
Copy code
pip install -r requirements.txt
