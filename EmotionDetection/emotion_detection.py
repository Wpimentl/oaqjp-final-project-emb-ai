import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        all_emotions = formatted_response['emotionPredictions'][0]['emotion']
        largest_value = max(all_emotions.values())
        key_with_largest_value = max(all_emotions, key=all_emotions.get)
        dominant_emotion = key_with_largest_value
        all_emotions['dominant_emotion'] = dominant_emotion
    elif response.status_code == 400:
        formatted_response = {
                            'anger': None,
                            'disgust': None, 
                            'fear': None, 
                            'joy': None, 
                            'sadness': None, 
                            'dominant_emotion': None}
        return formatted_response
    return (all_emotions)