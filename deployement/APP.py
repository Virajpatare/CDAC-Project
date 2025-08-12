from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model
xgb_model = pickle.load(open("xgb_model.pkl", "rb"))
model_columns = pickle.load(open("model_columns.pkl", "rb"))

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.form.to_dict()
    print("🔍 Incoming UI data:", data)

    # Convert Yes/No checkboxes (if checked, they are in the data)
    yes_no_features = [
        'Furnishing_Yes', 'Parking_Yes', 'Lift_Yes',
        'Security_Yes', 'Gym_Yes', 'Swimming_Yes', 'Power_Yes'
    ]
    input_data = {
        'State': data['state'],
        'City': data['city'],
        'Size_in_SqFt': int(data['size']),
        'BHK': int(data['bhk']),
        'Age_of_Property': int(data['age'])
    }

    for feature in yes_no_features:
        input_data[feature] = 1 if feature in data else 0

    df = pd.DataFrame([input_data])

    # One-hot encode and align with training columns
    df_encoded = pd.get_dummies(df)
    df_encoded = df_encoded.reindex(columns=model_columns, fill_value=0)

    prediction = xgb_model.predict(df_encoded)[0]
    return render_template("index.html", prediction=round(prediction, 2))

if __name__ == "__main__":
    app.run(debug=True)
