from flask import Flask, render_template, request
from final_project.EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# IMPORTANT: route must be /emotionDetector
@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    text_to_analyze = request.args.get("textToAnalyze", "")

    # Handle empty input gracefully
    if not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    # result is a dict: anger, disgust, fear, joy, sadness, dominant_emotion
    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant_emotion = result["dominant_emotion"]

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
