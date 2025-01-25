import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load your dataset
df = pd.read_csv("dataset.csv")  # Replace with your actual dataset file

# Define features (X) and target (y)
X = df[['month', 'year', 'day_of_week']]
y = df['Modal_Price']

# Train the Random Forest Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the new model
joblib.dump(model, "random_forest_model.pkl")

print("Model retrained and saved successfully!")
