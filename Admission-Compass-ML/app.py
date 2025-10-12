from flask import Flask
from routes.eksu_routes import eksu_bp
from routes.lasu_routes import lasu_bp

app = Flask(__name__)

# Register your blueprints with unique prefixes
app.register_blueprint(eksu_bp, url_prefix="/eksu")
app.register_blueprint(lasu_bp, url_prefix="/lasu")


@app.route("/")
def home():
    return "Welcome to the Admission Prediction API"


if __name__ == "__main__":
    app.run(debug=True)
