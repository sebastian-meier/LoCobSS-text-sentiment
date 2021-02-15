import requests

url = 'https://sentiment-rzuu3ecqxa-ey.a.run.app/predict'

body = {
    "text": "The insurance company is evil!"
}

response = requests.post(url, data=body)

print(response.json())