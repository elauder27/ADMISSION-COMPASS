from flask import Blueprint, jsonify, request
import joblib
import pandas as pd
import os

lasu_bp = Blueprint("lasu_bp", __name__)

model_path = os.path.join("models", "lasu_admission_model.pkl")
with open(model_path, "rb") as f:
    lasu_model = joblib.load(f)


@lasu_bp.route("/", methods=["POST"])
def predict_lasu():
    data = request.get_json()

    if "features" not in data:
        return jsonify({"error": "Missing features in request"}), 400

    features = data["features"]

    df = pd.DataFrame([features], columns=[
        "utme_score",
        "screening_score",
        "faculty",
        "department",
        "olevel_passed",
        "olevel_avg_points"
    ])

    prediction = lasu_model.predict(df)
    return jsonify({"prediction": prediction.tolist()})
