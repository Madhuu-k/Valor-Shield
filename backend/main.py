from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    # Inputs
    worker = data.get("worker")
    hours = int(data.get("hours"))
    time = data.get("time")
    weather = data.get("weather")

    # 🧠 Risk scoring system
    risk_score = 0

    # Worker risk
    if worker == "driver":
        risk_score += 3
    elif worker == "delivery":
        risk_score += 2
    else:
        risk_score += 1

    # Work duration risk
    if hours > 8:
        risk_score += 2
    elif hours > 5:
        risk_score += 1

    # Time risk
    if time == "night":
        risk_score += 2

    # Weather risk
    if weather == "moderate":
        risk_score += 1
    elif weather == "severe":
        risk_score += 2
    elif weather == "extreme":
        risk_score += 3

    # 🎯 Convert score → Risk level
    if risk_score <= 3:
        risk = "Low"
        premium = 50
    elif risk_score <= 6:
        risk = "Medium"
        premium = 100
    else:
        risk = "High"
        premium = 200

    # 🧠 Explanation (dynamic)
    explanation = (
        f"Risk influenced by {worker} work, {time} shift, "
        f"{weather} weather, and {hours} working hours"
    )

    # 🎯 Optional confidence (demo booster)
    if risk == "High":
        confidence = "95%"
    elif risk == "Medium":
        confidence = "90%"
    else:
        confidence = "85%"

    return jsonify({
        "risk": risk,
        "premium": premium,
        "explanation": explanation,
        "confidence": confidence
    })


if __name__ == "__main__":
    app.run(debug=True)