"""
This application runs a flask server for a web app to do sentiment analysis
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detection

app = Flask(__name__)

@app.route("/")
def index_route():
    """
    index route to render 
    """
    return render_template("index.html")

@app.route('/emotionDetector')
def emotion_detector():
    """
    returns the emotion in query string textToAnalyze passed in the url 
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detection.emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}. "
        f"The dominant emotion is  {response['dominant_emotion']}"
    )
    return formatted_response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
