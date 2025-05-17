import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Create the payload with the text to be analyzed
    payload = { "raw_document": { "text": text_to_analyse } }

    # Make a POST request to the API with the headers and payload
    response = requests.post(url, headers=header, json=payload)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # Get the dominant emotion
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)

    emotions['dominant_emotion'] = dominant_emotion
    return emotions

