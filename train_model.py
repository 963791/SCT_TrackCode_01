import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load data
df = pd.read_csv('housing.csv')

# Select features and target
X = df[[
    'Avg. Area Income',
    'Avg. Area House Age',
    'Avg. Area Number of Rooms',
    'Avg. Area Number of Bedrooms',
    'Area Population'
]]
y = df['Price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, 'model.pkl')
print("Model trained and saved to model.pkl")
