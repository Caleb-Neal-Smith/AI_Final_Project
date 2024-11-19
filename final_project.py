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

def emotionsAPI(content):
    response = requests.post(
        "https://api.sapling.ai/api/v1/tone",
        json={
            "key": key,
            "text": content
        }
    )
    return response

def getEmoji(emotions):
    # response = emotionsAPI(content) # API call
    #
    # emotions = response.json()
    j = 0
    finalSentence = ''
    # sentenceTogether = '' # May not need this line
    for i in emotions['sents']:
        # finalSentence = finalSentence + sentenceTogether
        sentenceTogether = i + emotions['results'][j][0][2]
        finalSentence = finalSentence + ' ' + sentenceTogether
        j = j + 1
    return finalSentence

# Maybe change parameter name from emotions back to 'content'?
def colorifyText(emotions):
    # delimiting the list
    # splitting the contents every newline character
    # contentList = content.split(".") #Use period or newline here? # Don't need this (?)

    # pprint(contentList) # for Debugging

    # responseList = []
    # i = 0

    """
    # iterating through the list of content
    # the code inside the while loop is pretty much straight from the sapling website
    while i < len(contentList):
        response = responseAPI(contentList[i])
        # print(response.json()) # for Debugging
        responseList.append(response)  # appending the response to the response list
        # pprint(responseList[i].json())
        i = i + 1  # iterating
    """


    # response = emotionsAPI(content)  # API call
    #
    # emotions = response.json()

    # responseList = [] # May not need this
    # i = 0 # Do we need to initialize "i"? # May not need this

    finalSentence = ''

    """
    for i in emotions:
        # response = responseAPI(contentList[i])
        # print(response.json()) # for Debugging
        responseList.append(i)  # appending the response to the response list
        # pprint(responseList[i].json())
        i = i + 1  # iterating
    """

    # pprint(responseList.json()) # for Debugging
    # print(style.BLUE + "Hello, World!" + "\033[0m") # for Debugging

    # response = responseAPI(content)  # API call

    # emotions = response.json()
    j = 0 # May not need this

    # iterating through the response list
    # IMPORTANT: Fix this function
    """
    while j < len(responseList):
        val = responseList[j].json()
        # pprint(val['results'][0][0][1])
    """
    # checking the returned emotion/ tone value
    # and changing output color appropriately
    for k in range (0, len(emotions['sents'])):
        if emotions['results'][k][0][1] == "angry":
            # print(style.RED + str(contentList[j]) + "\033[0m") # May not need this
            sentenceTogether = style.RED + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "admiring":
             # print(style.DARKYELLOW + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.DARKYELLOW + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "curious":
            # print(style.CYAN + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.CYAN + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "confused":
            # print(style.GREEN + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.GREEN + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        # TEMP BLOW to add more # Take out this comment?
        elif emotions['results'][k][0][1] == "joyful":
            # print(style.YELLOW + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.YELLOW + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "loving":
            # print(style.PINK + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.PINK + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "excited":
            # print(style.ORANGE + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.ORANGE + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "fearful":
            # print(style.DARKPURPLE + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.DARKPURPLE + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "worried":
            # print(style.DARKGREY + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.DARKGREY + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "embarrassed":
            # print(style.MAGENTA + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.MAGENTA + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "sympathetic":
            # print(style.LIGHTRED + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.LIGHTRED + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "annoyed":
            # print(style.DARKRED + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.DARKRED + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "approving":
            # print(style.MAGENTA + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.MAGENTA + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "aware":
            # print(style.LIGHTGREY_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.LIGHTGREY_BG + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "confident":
            # print(style.LIGHTVIOLET_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.LIGHTVIOLET_BG + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "eager":
            # print(style.ORANGE_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.ORANGE_BG + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "disappointed":
            # print(style.LIGHTGREY + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.LIGHTGREY + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "disapproving":
            # print(style.DARKGREY + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.DARKGREY + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "grateful":
            # print(style.YELLOW_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.YELLOW_BG + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "mournful":
            # print(style.DARKGREY_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.DARKGREY_BG + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "optimistic":
            # print(style.GREEN_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.GREEN_BG + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "relieved":
            # print(style.CYAN_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.CYAN_BG + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "remorseful":
            # print(style.BLUE_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.BLUE_BG + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "repulsed":
            # print(style.DARKGREEN + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.DARKGREEN + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "sad":
            # print(style.BLUE + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.BLUE + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "surprised":
            # print(style.LIGHTVIOLET_BG + style.RED + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.LIGHTVIOLET_BG + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        # ^^^^^^^^^ ADD MORE ^^^^^^^^^ # Should we add the two missing tones?

        # j = j + 1  # iterating # may not need this

    return finalSentence

def toneColorEmoji(emotions):
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
    # contentList = content.split(".") # May not need this

    # pprint(contentList) # for Debugging

    # responseList = [] # May not need this
    # i = 0 # May not need this

    # iterating through the list of content
    # the code inside the while loop is pretty much straight from the sapling website
    """
    while i < len(contentList):
        response = responseAPI(contentList[i])
        # print(response.json()) # for Debugging
        responseList.append(response)  # appending the response to the response list
        # pprint(responseList[i].json())
        i = i + 1  # iterating
    """

    # pprint(responseList.json()) # for Debugging
    # print(style.BLUE + "Hello, World!" + "\033[0m") # for Debugging
    # j = 0 # May not need this

    # May not need these lines that are commented out below (305-307)
    # response = emotionsAPI(content)  # API call
    #
    # emotions = response.json()

    finalSentence = ''

    # iterating through the response list
    # + emotions['results'][k][0][2] # For copying and pasting
    for k in range (0, len(emotions['sents'])):
        # val = responseList[j].json() # May not need this
        # pprint(val['results'][0][0][1]) # May not need this

        # checking the returned emotion/ tone value
        # and changing output color appropriately
        if emotions['results'][k][0][1] == "angry":
            # print(style.RED + str(contentList[j]) + "\033[0m") # May not need this
            sentenceTogether = style.RED + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "admiring":
            # print(style.DARKYELLOW + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.DARKYELLOW + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "curious":
            # print(style.CYAN + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.CYAN + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "confused":
            # print(style.GREEN + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.GREEN + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        # TEMP BLOW to add more # Take out this comment?
        elif emotions['results'][k][0][1] == "joyful":
            # print(style.YELLOW + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.YELLOW + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "loving":
            # print(style.PINK + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.PINK + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "excited":
            # print(style.ORANGE + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.ORANGE + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "fearful":
            # print(style.DARKPURPLE + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.DARKPURPLE + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "worried":
            # print(style.DARKGREY + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.DARKGREY + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "embarrassed":
            # print(style.MAGENTA + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.MAGENTA + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "sympathetic":
            # print(style.LIGHTRED + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.LIGHTRED + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "annoyed":
            # print(style.DARKRED + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.DARKRED + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "approving":
            # print(style.MAGENTA + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.MAGENTA + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "aware":
            # print(style.LIGHTGREY_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.LIGHTGREY_BG + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "confident":
            # print(style.LIGHTVIOLET_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.LIGHTVIOLET_BG + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "eager":
            # print(style.ORANGE_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.ORANGE_BG + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "disappointed":
            # print(style.LIGHTGREY + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.LIGHTGREY + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "disapproving":
            # print(style.DARKGREY + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.DARKGREY + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "grateful":
            # print(style.YELLOW_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.YELLOW_BG + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "mournful":
            # print(style.DARKGREY_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.DARKGREY_BG + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "optimistic":
            # print(style.GREEN_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.GREEN_BG + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "relieved":
            # print(style.CYAN_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.CYAN_BG + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "remorseful":
            # print(style.BLUE_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.BLUE_BG + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "repulsed":
            # print(style.DARKGREEN + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.DARKGREEN + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "sad":
            # print(style.BLUE + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.BLUE + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "surprised":
            # print(style.LIGHTVIOLET_BG + style.RED + str(contentList[j]) + "\033[0m")
            sentenceTogether = style.LIGHTVIOLET_BG + str(emotions['sents'][k]) + "\033[0m" + str(emotions['results'][k][0][2])
            finalSentence = finalSentence + ' ' + sentenceTogether

        # ^^^^^^^^^ ADD MORE ^^^^^^^^^ # Should we add the two missing tones?

        # j = j + 1  # iterating # may not need this

    """
    The toneColorEmoji() function wasn't working because I accidentally put the return statement
    inside of the "for in range" loop
    """
    return finalSentence

def getSynonyms():
    url = 'https://api.sapling.ai/api/v1/thesaurus'

    # Loop for multiple inputs until user types "exit"
    while True:
        # Ask the user for a word to search synonyms for
        word = input("Enter a word to get synonyms (or type 'exit' to quit): ").strip()

        if word.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break

        # Create the data payload for the request
        data = {
            'key': key,
            'query': word,
        }

        # Send the request to the Sapling API
        try:
            resp = requests.post(url, json=data)
            resp_json = resp.json()

            # Check the status of the response
            if 200 <= resp.status_code < 300:
                # Print the synonyms returned by the API
                print(f"Synonyms for '{word}':")
                synonyms = resp_json.get('synonyms', [])
                if synonyms:
                    for synonym in synonyms:
                        print(f"- {synonym}")
                else:
                    print("No synonyms found.")
            else:
                print('Error: ', resp_json)
        except Exception as e:
            print('Error: ', e)



with open('example_added.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    # print(content) # for Debugging

response = emotionsAPI(content) # API call

emotions = response.json()

# start of our normal code
option = 0
# start if for menu here
while option != '5':
    print("PLEASE SELECT ONE OF OUR MENU OPTIONS")
    option = input("1. Emojify your text\n2. Colorify your text\n3. Do BOTH\n4. Get a Synonym for a word\n5. Leave.\n")
    if option == '1': # emojify your code
        # text = input("Type your text: ") # Don't need this
        print(getEmoji(emotions))

    if option == '2':
        print(colorifyText(emotions))

    if option == '3':
        # text = input("Type your text: ") # Don't need this
        print(toneColorEmoji(emotions))

    if option == '4':
        getSynonyms()

    # Do we need an 'if' statement to check for "option == 5"?
