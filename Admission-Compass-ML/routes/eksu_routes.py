from flask import Blueprint, jsonify, request
import joblib
import pandas as pd
import os

# unique blueprint name
eksu_bp = Blueprint("eksu_bp", __name__)

# Load model safely
model_path = os.path.join("models", "eksu_admission_model.pkl")
with open(model_path, "rb") as f:
    eksu_model = joblib.load(f)


@eksu_bp.route("/", methods=["POST"])
def predict_eksu():
    data = request.get_json()

    if "features" not in data:
        return jsonify({"error": "Missing features in request"}), 400

    features = data["features"]

    df = pd.DataFrame([features], columns=[
        'UTME_Score',
        'Screening_Score',
        'Olevel_Valid',
        'olevel_avg_points',
        'Faculty',
        'Department',
    ])

    prediction = eksu_model.predict(df)
    return jsonify({"prediction": prediction.tolist()})
