from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib
import os

app = Flask(__name__)

MODEL_PATH = os.path.join("models", "aqi_random_forest_model.pkl")
FEATURE_PATH = os.path.join("models", "feature_columns.pkl")

model = joblib.load(MODEL_PATH)
feature_columns = joblib.load(FEATURE_PATH)


SKEWED_FEATURES = [
    'pm2.5', 'pm10', 'no', 'no2', 'n_ox',
    'nh3', 'co', 'so2', 'o3', 'benzene', 'toluene'
]


def get_cities():
    return sorted(
        col.replace("city_", "")
        for col in feature_columns
        if col.startswith("city_")
    )


@app.route("/")
def home():
    return render_template(
        "index.html",
        cities=get_cities()
    )


@app.route("/predict", methods=["POST"])
def predict():
    try:
        
        input_df = pd.DataFrame(
            np.zeros((1, len(feature_columns))),
            columns=feature_columns
        )

        
        numeric_inputs = {
            'pm2.5': float(request.form['pm2_5']),
            'pm10': float(request.form['pm10']),
            'no': float(request.form['no']),
            'no2': float(request.form['no2']),
            'n_ox': float(request.form['n_ox']),
            'nh3': float(request.form['nh3']),
            'co': float(request.form['co']),
            'so2': float(request.form['so2']),
            'o3': float(request.form['o3']),
            'benzene': float(request.form['benzene']),
            'toluene': float(request.form['toluene']),
            'is_weekend': int(request.form['is_weekend']),
            'season': int(request.form['season'])
        }

        
        for col in SKEWED_FEATURES:
            numeric_inputs[col] = np.log1p(numeric_inputs[col])

        
        for key, value in numeric_inputs.items():
            input_df.at[0, key] = value

        
        selected_city = request.form['city']
        city_col = f"city_{selected_city}"

        if city_col in input_df.columns:
            input_df.at[0, city_col] = 1

        
        prediction = model.predict(input_df)[0]

        return render_template(
            "index.html",
            prediction_text=f"Predicted AQI: {prediction:.2f}",
            cities=get_cities(),
            selected_city=selected_city
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}",
            cities=get_cities()
        )

if __name__ == "__main__":
    app.run(debug=True)
