import os
from flask import Flask, request

from googleapiclient.http import MediaIoBaseUpload
import io
from GoogleSearch import Search
import requests, json

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual Google API key
API_KEY = 'AIzaSyDCH7RlmJEzcXxs7t4bv1oQ6bn5sqI0Tc4 '
API_SERVICE_NAME = 'customsearch'
API_VERSION = 'v1'
SEARCH_ENGINE_ID = 'c775d0dff03614e78'

BASE_URI = 'https://api.bing.microsoft.com/v7.0/images/visualsearch'
SUBSCRIPTION_KEY = '438b8e05404840cd9726c5d9802f9f16'

def print_json(obj):
    """Print the object as json"""
    print(json.dumps(obj, sort_keys=True, indent=2, separators=(',', ': ')))

@app.route('/search', methods=['POST'])
def search_image():
    # Check if the 'image' file is present in the request
    #if 'image' not in request.files:
    #    return 'No image file found', 400

    # Save the uploaded image to a temporary file
    image_file = request.files['image']
    image_path = 'uploaded_image.jpg'
    image_file.save(image_path)

    HEADERS = {'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

    file = {'image' : ('myfile', open(image_path, 'rb'))}

    #formData = '{"imageInfo":{"imageInsightsToken":"' + insightsToken + '", }, "knowledgeRequest":{"invokedSkills": ["SimilarImages"]}}'

    #file = {'knowledgeRequest': (None, formData)}

    #file = {'image' : ('myfile', open(filePath, 'rb'))}

    try:
        response = requests.post(BASE_URI, headers=HEADERS, files=file)
        response.raise_for_status()
        print_json(response.json())
        
    except Exception as ex:
        raise ex

if __name__ == '__main__':
    app.run()
