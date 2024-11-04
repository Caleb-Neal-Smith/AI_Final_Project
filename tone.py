import requests
from pprint import pprint

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

response = requests.post(
    "https://api.sapling.ai/api/v1/tone",
    json={
        "key": "XO4JD953SJMKVQM8BOSVVSJCAGUJ5BGX",
        "text": "{content}"
    }
)

pprint(response.json())