import requests

# Replace '/path/to/your/image.jpg' with the actual path to the image file you want to upload
files = {'image': open('./test_image.jpg', 'rb')}
response = requests.post('http://localhost:5000/search', files=files)

print(response.json())  # Display the response as JSON
