import requests
from pprint import pprint

response = requests.post(
    "https://api.sapling.ai/api/v1/tone",
    json={
        "key": "QD3LVJOE28KMD9E6C820ET3GAUDUOCSC",
        "text": "Really stoked about this! Will it be ready by next week?"
    }
)
emotions = response.json()
j = 0
finalSentence = ''
sentenceTogether = ''
for i in emotions['sents']:
    #finalSentence = finalSentence + sentenceTogether
    sentenceTogether = i + emotions['results'][j][0][2]
    finalSentence = finalSentence + ' ' + sentenceTogether
    j = j + 1
print(finalSentence)

#print(len(joe["results"]))
#print(joe["results"][1][2][2])
# pprint(response.json())