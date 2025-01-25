from flask import Flask, render_template, jsonify,request
import pandas as pd
from datetime import datetime
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained Random Forest model
model = joblib.load("random_forest_model.pkl")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            # Get user input from form
            month = int(request.form["month"])
            year = int(request.form["year"])
            day_of_week = int(request.form["day_of_week"])

            # Validate input
            if not (1 <= month <= 12):
                raise ValueError("Month must be between 1 and 12.")
            if not (0 <= day_of_week <= 6):
                raise ValueError("Day of the week must be between 0 (Monday) and 6 (Sunday).")

            # Prepare input data for prediction
            input_data = np.array([[month, year, day_of_week]])

            # Make prediction
            prediction = model.predict(input_data)[0]
        
        except Exception as e:
            error = str(e)

    return render_template("index.html", prediction=prediction, error=error)

# Route to serve the dashboard page
@app.route('/visualize')
def index():
    return render_template('dashboard.html')  # Ensure index.html is inside 'templates' folder

# Route to fetch processed crop price data
@app.route('/get_price_data')
def get_price_data():
    df = pd.read_csv('dataset.csv')

    # Aggregate Modal_Price by Year and round to 1 decimal place
    yearly_prices = df.groupby('year')['Modal_Price'].mean().round(0).reset_index()
    yearly_prices = yearly_prices.to_dict(orient='records')

    # Aggregate Modal_Price by Month and round to 1 decimal place
    monthly_prices = df.groupby('month')['Modal_Price'].mean().round(0).reset_index()
    monthly_prices = monthly_prices.to_dict(orient='records')

    return jsonify({'yearly_prices': yearly_prices, 'monthly_prices': monthly_prices})
@app.route('/')
def home():
    # Fetching today's date
    today_date = datetime.today().strftime('%B %d, %Y')

    # Sample crop prices, you can replace them with actual data
    wheat_price = 3405
    rice_price = 3340
    maize_price = 3553
    barley_price = 3560

    # Sample max and min prices
    max_price = 3600
    min_price = 3200

    return render_template('home.html', 
                           today_date=today_date, 
                           wheat_price=wheat_price, 
                           rice_price=rice_price,
                           maize_price=maize_price, 
                           barley_price=barley_price, 
                           max_price=max_price, 
                           min_price=min_price)

if __name__ == '__main__':
    app.run(debug=True)
