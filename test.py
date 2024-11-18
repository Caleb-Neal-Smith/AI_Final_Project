import requests
from pprint import pprint
key = "QD3LVJOE28KMD9E6C820ET3GAUDUOCSC"

def getEmoji(text):
    response = emojiAPI(text) # API call

    emotions = response.json()
    j = 0
    finalSentence = ''
    sentenceTogether = ''
    for i in emotions['sents']:
        # finalSentence = finalSentence + sentenceTogether
        sentenceTogether = i + emotions['results'][j][0][2]
        finalSentence = finalSentence + ' ' + sentenceTogether
        j = j + 1
    return finalSentence


def emojiAPI(text):
    response = requests.post(
        "https://api.sapling.ai/api/v1/tone",
        json={
            "key": key,
            "text": text
        }
    )
    return response


# start of our normal code
option = 0
# start if for menu here
while option != '5':
    print("PLEASE SELECT ONE OF OUR MENU OPTIONS")
    option = input("1. Emojify your text\n2. Colorify your text\n3. Do BOTH\n4. Get a Synonym for a word\n5. Leave.\n")
    if option == '1': # emojify your code
        text = input("Type your text: ")
        print(getEmoji(text))

    if option == '2':
        pass

    if option == '3':
        pass

    if option == '4':
        pass

