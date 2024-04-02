import requests
import json

url = "http://127.0.0.1:8000/image"

image_path = "0.jpg"
with open(image_path, "rb") as f:
    files = {'image': f}
    response = requests.post(url, files=files)
    print(json.loads(response.text)["Prediction"])