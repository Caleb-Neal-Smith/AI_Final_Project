import requests
from pprint import pprint
key = "QD3LVJOE28KMD9E6C820ET3GAUDUOCSC"

# This class sets the variable for each color
class style:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    LIGHTCYAN = '\033[96m'
    WHITE = '\033[37m'
    ORANGE = '\033[33m'
    DARKPURPLE = '\033[35m'
    LIGHTGREY = '\033[37m'
    DARKGREY = '\033[90m'
    PINK = '\033[95m'
    LIGHTRED = '\033[91m'
    DARKYELLOW = '\033[33m'
    DARKRED = '\033[31m'
    DARKGREEN = '\033[32m'
    DARKBLUE = '\033[34m'
    RED_BG = '\033[41m'
    GREEN_BG = '\033[42m'
    ORANGE_BG = '\033[43m'
    BLUE_BG = '\033[44m'
    YELLOW_BG = '\033[103m'
    VIOLET_BG = '\033[45m'
    LIGHTVIOLET_BG = '\033[105m'
    CYAN_BG = '\033[46m'
    LIGHTGREY_BG = '\033[47m'
    DARKGREY_BG = '\033[100m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


# reading the email from specified file
# we can make this a command line argument later
# Don't need this (?)
"""
with open('example_added.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    # print(content) # for Debugging
"""

def getEmoji(content):
    response = responseAPI(content) # API call

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


def responseAPI(content):
    response = requests.post(
        "https://api.sapling.ai/api/v1/tone",
        json={
            "key": key,
            "text": content
        }
    )
    return response

def colorifyText(content):
    # delimiting the list
    # splitting the contents every newline character
    contentList = content.split(".") #Use period or newline here?

    # pprint(contentList) # for Debugging

    responseList = []
    i = 0

    # iterating through the list of content
    # the code inside the while loop is pretty much straight from the sapling website
    while i < len(contentList):
        response = responseAPI(contentList[i])
        # print(response.json()) # for Debugging
        responseList.append(response)  # appending the response to the response list
        # pprint(responseList[i].json())
        i = i + 1  # iterating

    # pprint(responseList.json()) # for Debugging
    # print(style.BLUE + "Hello, World!" + "\033[0m") # for Debugging
    j = 0

    # iterating through the response list
    while j < len(responseList):
        val = responseList[j].json()
        # pprint(val['results'][0][0][1])

        # checking the returned emotion/ tone value
        # and changing output color appropriately
        if val['results'][0][0][1] == "angry":
            print(style.RED + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "admiring":
            print(style.DARKYELLOW + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "curious":
            print(style.CYAN + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "confused":
            print(style.GREEN + str(contentList[j]) + "\033[0m")

        # TEMP BLOW to add more
        elif val['results'][0][0][1] == "joyful":
            print(style.YELLOW + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "loving":
            print(style.PINK + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "excited":
            print(style.ORANGE + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "fearful":
            print(style.DARKPURPLE + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "worried":
            print(style.DARKGREY + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "embarrassed":
            print(style.MAGENTA + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "sympathetic":
            print(style.LIGHTRED + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "annoyed":
            print(style.DARKRED + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "approving":
            print(style.MAGENTA + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "aware":
            print(style.LIGHTGREY_BG + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "confident":
            print(style.LIGHTVIOLET_BG + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "eager":
            print(style.ORANGE_BG + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "disappointed":
            print(style.LIGHTGREY + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "disapproving":
            print(style.DARKGREY + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "grateful":
            print(style.YELLOW_BG + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "mournful":
            print(style.DARKGREY_BG + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "optimistic":
            print(style.GREEN_BG + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "relieved":
            print(style.CYAN_BG + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "remorseful":
            print(style.BLUE_BG + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "repulsed":
            print(style.DARKGREEN + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "sad":
            print(style.BLUE + str(contentList[j]) + "\033[0m")

        elif val['results'][0][0][1] == "surprised":
            print(style.LIGHTVIOLET_BG + style.RED + str(contentList[j]) + "\033[0m")

        # ^^^^^^^^^ ADD MORE ^^^^^^^^^

        j = j + 1  # iterating

def toneColorEmoji(content):
    # reading the email from specified file
    # we can make this a command line argument later
    """
    with open('example_added.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        # print(content) # for Debugging
    """

    # content = input("Enter an email: ") # Don't need this now

    # delimiting the list
    # splitting the contents every newline character
    contentList = content.split(".")

    # pprint(contentList) # for Debugging

    responseList = []
    i = 0

    # iterating through the list of content
    # the code inside the while loop is pretty much straight from the sapling website
    while i < len(contentList):
        response = requests.post(
            "https://api.sapling.ai/api/v1/tone",
            json={
                "key": "XO4JD953SJMKVQM8BOSVVSJCAGUJ5BGX",
                "text": contentList[i]  # sending the data of the list
            }
        )
        # print(response.json()) # for Debugging
        responseList.append(response)  # appending the response to the response list
        # pprint(responseList[i].json())
        i = i + 1  # iterating

    # pprint(responseList.json()) # for Debugging
    # print(style.BLUE + "Hello, World!" + "\033[0m") # for Debugging
    j = 0

    # iterating through the response list
    while j < len(responseList):
        val = responseList[j].json()
        # pprint(val['results'][0][0][1])

        # checking the returned emotion/ tone value
        # and changing output color appropriately
        if val['results'][0][0][1] == "angry":
            print(style.RED + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "admiring":
            print(style.DARKYELLOW + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "curious":
            print(style.CYAN + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "confused":
            print(style.GREEN + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        # TEMP BLOW to add more
        elif val['results'][0][0][1] == "joyful":
            print(style.YELLOW + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "loving":
            print(style.PINK + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "excited":
            print(style.ORANGE + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "fearful":
            print(style.DARKPURPLE + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "worried":
            print(style.DARKGREY + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "embarrassed":
            print(style.MAGENTA + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "sympathetic":
            print(style.LIGHTRED + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "annoyed":
            print(style.DARKRED + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "approving":
            print(style.MAGENTA + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "aware":
            print(style.LIGHTGREY_BG + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "confident":
            print(style.LIGHTVIOLET_BG + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "eager":
            print(style.ORANGE_BG + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "disappointed":
            print(style.LIGHTGREY + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "disapproving":
            print(style.DARKGREY + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "grateful":
            print(style.YELLOW_BG + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "mournful":
            print(style.DARKGREY_BG + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "optimistic":
            print(style.GREEN_BG + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "relieved":
            print(style.CYAN_BG + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "remorseful":
            print(style.BLUE_BG + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "repulsed":
            print(style.DARKGREEN + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "sad":
            print(style.BLUE + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        elif val['results'][0][0][1] == "surprised":
            print(style.LIGHTVIOLET_BG + style.RED + str(contentList[j]) + "\033[0m" + val['results'][0][0][2])

        # ^^^^^^^^^ ADD MORE ^^^^^^^^^

        j = j + 1  # iterating




with open('example_added.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    # print(content) # for Debugging
    # start of our normal code
    option = 0
    # start if for menu here
    while option != '5':
        print("PLEASE SELECT ONE OF OUR MENU OPTIONS")
        option = input("1. Emojify your text\n2. Colorify your text\n3. Do BOTH\n4. Get a Synonym for a word\n5. Leave.\n")
        if option == '1': # emojify your code
            # text = input("Type your text: ") # Don't need this
            print(getEmoji(content))

        if option == '2':
            colorifyText(content)

        if option == '3':
            # text = input("Type your text: ") # Don't need this
            toneColorEmoji(content)

        if option == '4':
            pass
