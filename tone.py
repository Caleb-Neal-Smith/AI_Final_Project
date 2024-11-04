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
print("\033[1;31;40m '{content}' \033[0m")

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.BLUE + "Hello, World!")
print("\033[0m")