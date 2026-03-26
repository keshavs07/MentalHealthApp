from flask import Flask, render_template, request, jsonify
from modules.sentiment import predict_sentiment
from modules.emotion import detect_emotion
from modules.chatbot import chatbot_response

app = Flask(__name__)

def generate_response(text):
    sentiment = predict_sentiment(text)
    emotion = detect_emotion(text)

    if emotion in ["sadness", "depression"]:
        reply = "I'm here for you. Want to talk about it?"
    elif emotion in ["anger"]:
        reply = "Take a deep breath. Let's calm down."
    elif emotion in ["fear", "anxiety"]:
        reply = "You're safe. Try to relax."
    else:
        reply = chatbot_response(text)

    return sentiment, emotion, reply


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text"]

        sentiment, emotion, response = generate_response(text)

        return render_template(
            "index.html",
            text=text,
            sentiment=sentiment,
            emotion=emotion,
            response=response
        )

    return render_template("index.html")


@app.route("/voice", methods=["POST"])
def voice():
    data = request.get_json()
    text = data.get("text", "")
    sentiment, emotion, response = generate_response(text)

    return jsonify({
        "text": text,
        "sentiment": sentiment,
        "emotion": emotion,
        "response": response
    })


if __name__ == "__main__":
    app.run(debug=True)