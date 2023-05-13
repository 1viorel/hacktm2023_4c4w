import os
import openai
from flask import Flask, request, make_response
from flask_cors import CORS

from googleapiclient.http import MediaIoBaseUpload
import io
from GoogleSearch import Search
import requests, json

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

from name_extractor.Source import ParseJsonResponseFromBing

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

# Replace 'YOUR_API_KEY' with your actual Google API key
API_KEY = 'AIzaSyDCH7RlmJEzcXxs7t4bv1oQ6bn5sqI0Tc4 '
API_SERVICE_NAME = 'customsearch'
API_VERSION = 'v1'
SEARCH_ENGINE_ID = 'c775d0dff03614e78'

OPENAI_KEY = 'ask alex'

BASE_URI = 'https://api.bing.microsoft.com/v7.0/images/visualsearch'
SUBSCRIPTION_KEY = '438b8e05404840cd9726c5d9802f9f16'

def print_json(obj):
    """Print the object as json"""
    print(json.dumps(obj, sort_keys=True, indent=2, separators=(',', ': ')))

def save_json(obj, file_path):
    with open(file_path, "w") as json_file:
        json.dump(obj, json_file)

def CallGPTAbout(keywords):
    # Your OpenAI API key
    api_key = OPENAI_KEY

    # OpenAI ChatGPT API endpoint
    endpoint = 'https://api.openai.com/v1/chat/completions'

    # Prepare the list of messages
    message_list = [{'role': 'system', 'content': 'You are a helpful assistant.'}]
    user_msg = "What do you know about: "

    for msg in keywords:
        user_msg += msg
        user_msg += " "

    print(user_msg)

    user_msg += ". Tell me some fun facts about this car, and also tell me its specifications, in maximum 256 words."
    message_list.append({'role': 'user', 'content': user_msg})

    # Prepare the payload
    payload = {
        'messages': message_list
    }

    # Set up the API client
    openai.api_key = api_key

    # Make the API call
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=payload['messages'],
        max_tokens=512,
        n=1
    )

    # Retrieve and return the assistant's reply
    assistant_reply = response['choices'][0]['message']['content']
    return assistant_reply

@app.route('/search', methods=['POST'])
def search_image():
    # Check if the 'image' file is present in the request
    #if 'image' not in request.files:
    #    return 'No image file found', 400

    print(request.files)
    # Save the uploaded image to a temporary file
    image_file = request.files['image']
    image_path = 'uploaded_image.jpg'
    image_file.save(image_path)

    HEADERS = {'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

    # WATCH OUT, ONLY THE OLD IMAGE IS USED
    # DANGER 
    # DANGER
    # DANGER
    file = {'image' : ('myfile', open("test_image.jpg", 'rb'))}
    # DANGER 
    # DANGER
    # DANGER

    #formData = '{"imageInfo":{"imageInsightsToken":"' + insightsToken + '", }, "knowledgeRequest":{"invokedSkills": ["SimilarImages"]}}'

    #file = {'knowledgeRequest': (None, formData)}

    #file = {'image' : ('myfile', open(filePath, 'rb'))}

    try:
        response = requests.post(BASE_URI, headers=HEADERS, files=file)
        response.raise_for_status()
        save_json(response.json(), "response.json")
        print("response JSON")
        #temporarily reload json
        with open("response.json", 'r') as file:
            data = json.load(file)
        
        #call word counter
        list_of_keywords = ParseJsonResponseFromBing(data, 5)

        print(list_of_keywords)

        
        #call gpt with prompt "What do you know about?"
        gpt_reponse = CallGPTAbout(list_of_keywords)
        print(gpt_reponse)
        
    except Exception as ex:
        raise ex
    
    response = make_response( {"message":gpt_reponse} );
    response.status_code = 200
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
