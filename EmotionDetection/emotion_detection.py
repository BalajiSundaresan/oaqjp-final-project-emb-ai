import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers = headers, json = input)
    formatted_response = json.loads(response.text)
    output = {}
    emotion_score_max = 0.0
    dominant_emotion = ""
    emotionResponse = formatted_response['emotionPredictions'][0]['emotion']
    for key, value in emotionResponse.items():
        output[key] = value
        if value > emotion_score_max:
            dominant_emotion = key
            emotion_score_max = value
    output["dominant_emotion"] = dominant_emotion
    return output