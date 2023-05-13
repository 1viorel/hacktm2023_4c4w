import requests, json

BASE_URI = 'https://api.bing.microsoft.com/v7.0/images/visualsearch'
SUBSCRIPTION_KEY = '438b8e05404840cd9726c5d9802f9f16'
filePath = 'test_image.jpg'

#formData = '{"knowledgeRequest":{"invokedSkills": ["SimilarImages"]}}'

#file = {'knowledgeRequest': (None, formData)}

file = {'image' : ('myfile', open(filePath, 'rb'))}


HEADERS = {'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

def print_json(obj):
    """Print the object as json"""
    print(json.dumps(obj, sort_keys=True, indent=2, separators=(',', ': ')))

def save_json(obj, file_path):
    with open(file_path, "w") as json_file:
        json.dump(obj, json_file)

try:
    response = requests.post(BASE_URI, headers=HEADERS, files=file)
    response.raise_for_status()
    #tags = response.json().tags
    #print(len(tags))
    #print_json(response.json())
    #print(response.json()["tags"])
    save_json(response.json(), "response.json")
    
except Exception as ex:
    raise ex
