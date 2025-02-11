from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend requests

# Load the model and scaler
try:
    model = joblib.load('diabetes_model.pkl')
    scaler = joblib.load('scaler.pkl')
    print("Model and scaler loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model, scaler = None, None

# Feature columns (should match training dataset)
feature_columns = [
    'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
    'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'BMI_Age'
]

@app.route('/')
def home():
    return render_template('index.html')  # Serve HTML page

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or scaler is None:
        return jsonify({'error': 'Model or scaler not loaded'}), 500

    try:
        # Validate JSON Input
        data = request.get_json()
        if not data or "features" not in data:
            return jsonify({'error': 'Missing "features" key in JSON input'}), 400
        
        features = data["features"]

        # Validate Feature Format
        if not isinstance(features, list) or len(features) != 8:
            return jsonify({'error': 'Invalid input: Expected 8 numerical features'}), 400

        # Convert to DataFrame
        input_df = pd.DataFrame([features], columns=feature_columns[:-1])  # Exclude 'BMI_Age' for now

        # **Feature Engineering: Add 'BMI_Age'**
        input_df['BMI_Age'] = input_df['BMI'] * input_df['Age']

        # Scale Input Data
        data_scaled = scaler.transform(input_df)

        # Make Prediction
        prediction = int(model.predict(data_scaled)[0])

        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
