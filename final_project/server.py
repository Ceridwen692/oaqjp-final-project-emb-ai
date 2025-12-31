"""
Flask server for the Emotion Detection application.

This module provides web routes to render the UI and to analyze emotions.
"""

from flask import Flask, render_template, request
from .EmotionDetection import emotion_detector

HOST = "0.0.0.0"
PORT = 5000

app = Flask(__name__)


@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Run emotion detection for the provided text and return a formatted response."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


def main():
    """Start the Flask development server."""
    app.run(host=HOST, port=PORT, debug=True)


if __name__ == "__main__":
    main()
