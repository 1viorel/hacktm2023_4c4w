import os
from flask import Flask, request

from googleapiclient.http import MediaIoBaseUpload
import io

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual Google API key
API_KEY = 'AIzaSyDCH7RlmJEzcXxs7t4bv1oQ6bn5sqI0Tc4 '
API_SERVICE_NAME = 'customsearch'
API_VERSION = 'v1'
SEARCH_ENGINE_ID = 'c775d0dff03614e78'

@app.route('/search', methods=['POST'])
def search_image():
    # Check if the 'image' file is present in the request
    #if 'image' not in request.files:
    #    return 'No image file found', 400

    # Save the uploaded image to a temporary file
    #image_file = request.files['image']
    #image_path = '/tmp/uploaded_image.jpg'
    #image_file.save(image_path)
    image_path = "test_image.jpg"

    # Create a Google API client
    try:
        service = build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)
    except Exception as e:
        return f'Error creating Google API client: {e}', 500
    
    # Read the image file
    with io.open(image_path, 'rb') as f:

        # Upload the image to Google for image search
        try:
            media = MediaIoBaseUpload(f, mimetype='image/jpeg')
            request = service.cse().list(
                q='',
                cx=SEARCH_ENGINE_ID,
                num=10,
                searchType='image',
                imgType='photo',
                imgSize='MEDIUM',
                fileType='jpg',
                safe='off'
            )
            response = request.execute()
        except HttpError as e:
            error_message = e.content if hasattr(e, 'content') else str(e)
            return f'Error executing Google image search: {error_message}', 500
        except Exception as e:
            return f'Error executing Google image search: {e}', 500

        print(response)
        # Process the search results
        items = response.get('items', [])
        search_results = []
        for item in items:
            search_results.append({
                'title': item['title'],
                'link': item['link'],
                'thumbnail': item['image']['thumbnailLink']
            })

        # Return the search results as JSON
        return {'results': search_results, 'response': response}

if __name__ == '__main__':
    app.run()
