import requests

url = 'http://localhost:5050/predict'

body = {
    "text": "The insurance company is evil!"
}

response = requests.post(url, data=body)

print(response.json())