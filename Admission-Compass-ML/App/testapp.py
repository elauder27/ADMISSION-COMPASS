# lasu_inference_flask.py
from flask import Flask, request, render_template_string, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# --- Load model ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Current /App folder
MODEL_PATH = os.path.join(BASE_DIR, "..", "Models/lasu_admission_model.pkl")

# Normalize path for cross-platform compatibility
MODEL_PATH = os.path.normpath(MODEL_PATH)

print(f"📁 Loading model from: {MODEL_PATH}")

model = joblib.load(MODEL_PATH)
print("✅ Model loaded successfully!")

# LASU policy
LASU_MIN_SCREENING = 50.0
LASU_THRESHOLD_PROB = 0.65  # configurable threshold to say "likely admitted"

# simple HTML template for quick manual test
HTML = """
<!doctype html>
<title>LASU Admission Predictor</title>
<h1>LASU Admission Predictor</h1>
<form method=post>
  Faculty: <input name=faculty value="Science"><br>
  Department: <input name=department value="Computer Science"><br>
  UTME (120-400): <input name=utme_score value="202"><br>
  Screening (optional, 0-100): <input name=screening_score><br>
  O'Level Avg Points (0-10): <input name=olevel_avg_points value="7.4"><br>
  O'Level Passed? <select name=olevel_passed><option value="1">Yes</option><option value="0">No</option></select><br>
  <input type=submit value=Predict>
</form>
{% if result %}
  <h2>Result: {{ result }}</h2>
  <p>Probability: {{ prob }}%</p>
  <p>Screening used: {{ screening_used }}</p>
  <p>Note: If screening &lt; {{ min_screening }}, probability is penalized per LASU policy.</p>
{% endif %}
"""

def auto_calc_screening(utme_score, olevel_avg_points):
    # UTME out of 400 -> 50; O'Level total out of 50 -> 50
    # Note: olevel_avg_points is avg per subject (max 10). Convert to total for component.
    olevel_avg = olevel_avg_points * 5.0
    utme_component = (utme_score / 400.0) * 50.0
    olevel_component = (olevel_avg / 50.0) * 50.0
    screening = round(utme_component + olevel_component, 2)
    return screening

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    prob_pct = None
    screening_used = None

    if request.method == "POST":
        faculty = request.form.get("faculty", "Science")
        department = request.form.get("department", "Computer Science")
        utme_score = float(request.form.get("utme_score", 0))
        screening_input = request.form.get("screening_score", "").strip()
        olevel_avg_points = float(request.form.get("olevel_avg_points", 0))
        olevel_passed = int(request.form.get("olevel_passed", 0))

        # compute screening if not provided
        if screening_input == "":
            screening_score = auto_calc_screening(utme_score, olevel_avg_points)
            screening_used = f"auto-calculated: {screening_score}"
        else:
            screening_score = float(screening_input)
            screening_used = f"user-provided: {screening_score}"

        # Build input df consistent with model features
        input_df = pd.DataFrame([{
            "utme_score": utme_score,
            "screening_score": screening_score,
            "faculty": faculty,
            "department": department,
            "olevel_passed": olevel_passed,
            "olevel_avg_points": olevel_avg_points
        }])

        # Use model to predict probability
        proba = model.predict_proba(input_df)[0][1]  # prob of admission (0..1)

        # Penalize hard if screening below LASU minimum (to respect policy)
        if screening_score < LASU_MIN_SCREENING:
            # example penalty: scale probability down strongly
            # you can configure weight or multiplicative factor
            proba = proba * 0.3

        prob_pct = round(proba * 100, 2)
        admitted_flag = proba >= LASU_THRESHOLD_PROB
        result = "Likely Admitted ✅" if admitted_flag else "Unlikely to be Admitted ❌"

    return render_template_string(HTML, result=result, prob=prob_pct, screening_used=screening_used, min_screening=LASU_MIN_SCREENING)

@app.route("/api/predict", methods=["POST"])
def api_predict():
    # Accept JSON: faculty, department, utme_score, screening_score (optional), olevel_avg_points, olevel_passed
    data = request.get_json(force=True)
    faculty = data.get("faculty", "Science")
    department = data.get("department", "Computer Science")
    utme_score = float(data.get("utme_score", 0))
    screening_input = data.get("screening_score", None)
    olevel_avg_points = float(data.get("olevel_avg_points", 0))
    olevel_passed = int(data.get("olevel_passed", 0))

    if screening_input is None:
        screening_score = auto_calc_screening(utme_score, olevel_avg_points)
    else:
        screening_score = float(screening_input)

    input_df = pd.DataFrame([{
        "utme_score": utme_score,
        "screening_score": screening_score,
        "faculty": faculty,
        "department": department,
        "olevel_passed": olevel_passed,
        "olevel_avg_points": olevel_avg_points
    }])

    proba = model.predict_proba(input_df)[0][1]
    if screening_score < LASU_MIN_SCREENING:
        proba = proba * 0.3

    return jsonify({
        "probability": proba,
        "probability_pct": round(proba*100,2),
        "screening_used": screening_score,
        "likely_admitted": proba >= LASU_THRESHOLD_PROB
    })

if __name__ == "__main__":
    # Create static folder if missing to store charts from earlier steps
    os.makedirs("static", exist_ok=True)
    app.run(debug=True)
