from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detection


app = Flask(__name__)

@app.route("/")
def index_route():
    return render_template("index.html")

@app.route('/emotionDetector')
def emotion_detector():
    textToAnalyze = request.args.get('textToAnalyze')
    response = emotion_detection.emotion_detector(textToAnalyze)
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