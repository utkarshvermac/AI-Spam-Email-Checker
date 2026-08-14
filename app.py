from flask import Flask, render_template, request, jsonify
import os
import re
import joblib

app = Flask(__name__)

MODEL_PATH = "model.pkl"
model = None

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)


def analyze_text(text):
    words = re.findall(r"\b[\w']+\b", text)
    links = re.findall(r"https?://\S+|www\.\S+", text, flags=re.I)

    suspicious_terms = [
        "free", "winner", "won", "prize", "cash", "urgent",
        "claim", "click here", "lottery", "bonus", "congratulations",
        "verify your account", "limited time", "offer"
    ]
    lower = text.lower()
    suspicious = sum(lower.count(term) for term in suspicious_terms)

    return {
        "words": len(words),
        "characters": len(text),
        "links": len(links),
        "suspicious": suspicious
    }


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    global model

    if model is None:
        return jsonify({
            "error": "Model not found. Run 'python train_model.py' first."
        }), 500

    data = request.get_json(silent=True) or {}
    text = (data.get("email") or "").strip()

    if len(text) < 5:
        return jsonify({"error": "Please enter a longer email message."}), 400

    prediction = int(model.predict([text])[0])
    probabilities = model.predict_proba([text])[0]
    spam_probability = float(probabilities[1] * 100)

    result = "SPAM" if prediction == 1 else "NOT SPAM"

    return jsonify({
        "result": result,
        "spam_probability": round(spam_probability, 2),
        "analysis": analyze_text(text)
    })


if __name__ == "__main__":
    app.run(debug=True)
