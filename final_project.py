import requests
from pprint import pprint
key = "XO4JD953SJMKVQM8BOSVVSJCAGUJ5BGX"

# This class sets the variable for each color
# class style:
#     BLACK = '\033[30m'
#     RED = '\033[31m'
#     GREEN = '\033[32m'
#     YELLOW = '\033[93m'
#     BLUE = '\033[94m'
#     MAGENTA = '\033[35m'
#     CYAN = '\033[36m'
#     LIGHTCYAN = '\033[96m'
#     WHITE = '\033[37m'
#     ORANGE = '\033[33m'
#     DARKPURPLE = '\033[35m'
#     LIGHTGREY = '\033[37m'
#     DARKGREY = '\033[90m'
#     PINK = '\033[95m'
#     LIGHTRED = '\033[91m'
#     DARKYELLOW = '\033[33m'
#     DARKRED = '\033[31m'
#     DARKGREEN = '\033[32m'
#     DARKBLUE = '\033[34m'
#     RED_BG = '\033[41m'
#     GREEN_BG = '\033[42m'
#     ORANGE_BG = '\033[43m'
#     BLUE_BG = '\033[44m'
#     YELLOW_BG = '\033[103m'
#     VIOLET_BG = '\033[45m'
#     LIGHTVIOLET_BG = '\033[105m'
#     CYAN_BG = '\033[46m'
#     LIGHTGREY_BG = '\033[47m'
#     DARKGREY_BG = '\033[100m'
#     UNDERLINE = '\033[4m'
#     RESET = '\033[0m'

class RGBStyle:
    ADMIRING = (255, 128, 255)      # Bright Violet - warm admiration
    AMUSED = (255, 215, 64)         # Bright Golden Yellow - playful energy
    ANGRY = (255, 64, 64)           # Bright Red - intense anger
    ANNOYED = (255, 128, 80)        # Bright Orange-Red - irritation
    APPROVING = (128, 255, 128)     # Bright Lime Green - positive approval
    AWARE = (255, 255, 128)         # Bright Lemon Yellow - clarity
    CONFIDENT = (64, 128, 255)      # Bright Royal Blue - strong confidence
    CONFUSED = (192, 128, 255)      # Bright Lavender - uncertainty
    CURIOUS = (128, 200, 255)       # Bright Sky Blue - inquisitive
    EAGER = (255, 159, 64)          # Bright Pumpkin Orange - enthusiastic
    DISAPPOINTED = (160, 160, 192)   # Bright Slate Gray - letdown
    DISAPPROVING = (192, 128, 64)    # Bright Warm Brown - negative judgment
    EMBARRASSED = (255, 128, 160)    # Bright Blush Pink - flustered
    EXCITED = (255, 96, 64)         # Bright Flame Red - high energy
    FEARFUL = (160, 80, 40)         # Bright Chestnut Brown - fear
    GRATEFUL = (128, 255, 192)      # Bright Mint Green - thankful
    JOYFUL = (255, 255, 64)         # Bright Sunshine Yellow - pure joy
    LOVING = (255, 128, 192)        # Bright Rose Pink - affection
    MOURNFUL = (96, 128, 160)       # Bright Steel Blue - deep sadness
    NEUTRAL = (192, 192, 192)       # Bright Silver Gray - balanced
    OPTIMISTIC = (255, 223, 64)     # Bright Goldenrod - hopeful
    RELIEVED = (128, 255, 255)      # Bright Aqua Blue - tension release
    REMORSEFUL = (192, 96, 64)      # Bright Russet - regret
    REPULSED = (160, 255, 160)      # Bright Soft Green - disgust
    SAD = (96, 160, 255)            # Bright Cerulean Blue - melancholy
    WORRIED = (160, 160, 160)       # Bright Neutral Gray - concern
    SURPRISED = (255, 192, 64)      # Bright Marigold - unexpected
    SYMPATHETIC = (255, 128, 128)   # Bright Coral - compassion

def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def color_to_rgb(color):
    r, g, b = color
    return rgb_to_ansi(r, g, b)



# # Function to print colored gradient from top to bottom
# def print_gradient(text, color, tone):
#     # ANSI escape codes for colors
#     def rgb_to_ansi(r, g, b):
#         return f"\033[38;2;{r};{g};{b}m"
    
#     # Calculate the intermediate color based on the vertical position
#     r, g, b = color
    
#     # Apply the color to the entire line
#     print(f"{rgb_to_ansi(r, g, b)}{text}\033[0m")

# Function to print colored gradient from top to bottom
def print_gradient_emoji(text, color, emoji):
    # ANSI escape codes for colors
    def rgb_to_ansi(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"
    
    # Calculate the intermediate color based on the vertical position
    r, g, b = color
    
    # Apply the color to the entire line
    print(f"{rgb_to_ansi(r, g, b)}{text}\033[0m" + emoji)


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

    # pprint(emotions) # for Debugging

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
            # print(RGBStyle.RED + str(contentList[j]) + "\033[0m") # May not need this
            sentenceTogether = color_to_rgb(RGBStyle.ANGRY) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "admiring":
             # print(RGBStyle.DARKYELLOW + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.ADMIRING) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "curious":
            # print(RGBStyle.CYAN + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.CURIOUS) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "confused":
            # print(RGBStyle.GREEN + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.CONFUSED) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        # TEMP BLOW to add more # Take out this comment?
        elif emotions['results'][k][0][1] == "joyful":
            # print(RGBStyle.YELLOW + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.JOYFUL) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "loving":
            # print(RGBStyle.PINK + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.LOVING) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "excited":
            # print(RGBStyle.ORANGE + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.EXCITED) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "fearful":
            # print(RGBStyle.DARKPURPLE + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.FEARFUL) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "worried":
            # print(RGBStyle.DARKGREY + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.WORRIED) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "embarrassed":
            # print(RGBStyle.MAGENTA + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.EMBARRASSED) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "sympathetic":
            # print(RGBStyle.LIGHTRED + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.SYMPATHETIC) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "annoyed":
            # print(RGBStyle.DARKRED + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.ANNOYED) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "approving":
            # print(RGBStyle.MAGENTA + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.APPROVING) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "aware":
            # print(RGBStyle.LIGHTGREY_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.AWARE) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "confident":
            # print(RGBStyle.LIGHTVIOLET_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.CONFIDENT) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "eager":
            # print(RGBStyle.ORANGE_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.EAGER) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "disappointed":
            # print(RGBStyle.LIGHTGREY + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.DISAPPOINTED) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "disapproving":
            # print(RGBStyle.DARKGREY + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.DISAPPROVING) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "grateful":
            # print(RGBStyle.YELLOW_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.GRATEFUL) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "mournful":
            # print(RGBStyle.DARKGREY_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.MOURNFUL) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "optimistic":
            # print(RGBStyle.GREEN_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.OPTIMISTIC) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "relieved":
            # print(RGBStyle.CYAN_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.RELIEVED) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "remorseful":
            # print(RGBStyle.BLUE_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.REMORSEFUL) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "repulsed":
            # print(RGBStyle.DARKGREEN + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.REPULSED) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "sad":
            # print(RGBStyle.BLUE + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.SAD) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "surprised":
            # print(RGBStyle.LIGHTVIOLET_BG + RGBStyle.RED + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.SURPRISED) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        # ^^^^^^^^^ ADD MORE ^^^^^^^^^ # Should we add the two missing tones?

        # j = j + 1  # iterating # may not need this

        
        # pprint(emotions)

        # if emotions['results'][k][0][1] == "angry":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.ANGRY, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "admiring":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.ADMIRING, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "curious":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.CURIOUS, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "confused":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.CONFUSED, emotions['results'][k][0][1])

        # # TEMP BLOW to add more 
        # elif emotions['results'][k][0][1] == "joyful":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.JOYFUL, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "loving":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.LOVING, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "excited":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.EXCITED, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "fearful":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.FEARFUL, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "worried":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.WORRIED, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "embarrassed":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.EMBARRASSED, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "sympathetic":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.SYMPATHETIC, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "annoyed":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.ANNOYED, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "approving":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.APPROVING, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "aware":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.AWARE, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "confident":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.CONFIDENT, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "eager":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.EAGER, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "disappointed":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.DISAPPOINTED, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "disapproving":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.DISAPPROVING, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "grateful":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.GRATEFUL, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "mournful":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.MOURNFUL, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "optimistic":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.OPTIMISTIC, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "relieved":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.RELIEVED, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "remorseful":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.REMORSEFUL, emotions['results'][k][0][1])
        # elif emotions['results'][k][0][1] == "repulsed":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.REPULSED, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "sad":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.SAD, emotions['results'][k][0][1])

        # elif emotions['results'][k][0][1] == "surprised":
        #     print_gradient(str(emotions['sents'][k]), RGBStyle.SURPRISED, emotions['results'][k][0][1])

        # # ^^^^^^^^^ ADD MORE ^^^^^^^^^

        # j = j + 1  # iterating

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
            # print(RGBStyle.RED + str(contentList[j]) + "\033[0m") # May not need this
            sentenceTogether = color_to_rgb(RGBStyle.ANGRY) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "admiring":
             # print(RGBStyle.DARKYELLOW + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.ADMIRING) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "curious":
            # print(RGBStyle.CYAN + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.CURIOUS) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "confused":
            # print(RGBStyle.GREEN + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.CONFUSED) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        # TEMP BLOW to add more # Take out this comment?
        elif emotions['results'][k][0][1] == "joyful":
            # print(RGBStyle.YELLOW + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.JOYFUL) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "loving":
            # print(RGBStyle.PINK + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.LOVING) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "excited":
            # print(RGBStyle.ORANGE + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.EXCITED) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "fearful":
            # print(RGBStyle.DARKPURPLE + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.FEARFUL) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "worried":
            # print(RGBStyle.DARKGREY + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.WORRIED) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "embarrassed":
            # print(RGBStyle.MAGENTA + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.EMBARRASSED) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "sympathetic":
            # print(RGBStyle.LIGHTRED + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.SYMPATHETIC) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "annoyed":
            # print(RGBStyle.DARKRED + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.ANNOYED) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "approving":
            # print(RGBStyle.MAGENTA + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.APPROVING) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "aware":
            # print(RGBStyle.LIGHTGREY_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.AWARE) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "confident":
            # print(RGBStyle.LIGHTVIOLET_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.CONFIDENT) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "eager":
            # print(RGBStyle.ORANGE_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.EAGER) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "disappointed":
            # print(RGBStyle.LIGHTGREY + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.DISAPPOINTED) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "disapproving":
            # print(RGBStyle.DARKGREY + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.DISAPPROVING) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "grateful":
            # print(RGBStyle.YELLOW_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.GRATEFUL) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "mournful":
            # print(RGBStyle.DARKGREY_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.MOURNFUL) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "optimistic":
            # print(RGBStyle.GREEN_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.OPTIMISTIC) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "relieved":
            # print(RGBStyle.CYAN_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.RELIEVED) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "remorseful":
            # print(RGBStyle.BLUE_BG + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.REMORSEFUL) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "repulsed":
            # print(RGBStyle.DARKGREEN + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.REPULSED) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "sad":
            # print(RGBStyle.BLUE + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.SAD) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "surprised":
            # print(RGBStyle.LIGHTVIOLET_BG + RGBStyle.RED + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.SURPRISED) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        # ^^^^^^^^^ ADD MORE ^^^^^^^^^ # Should we add the two missing tones?

        # j = j + 1  # iterating # may not need this
        # if emotions['results'][k][0][1] == "angry":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.ANGRY, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "admiring":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.ADMIRING, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "curious":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.CURIOUS, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "confused":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.CONFUSED, emotions['results'][k][0][2])

        # # TEMP BLOW to add more 
        # elif emotions['results'][k][0][1] == "joyful":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.JOYFUL, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "loving":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.LOVING, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "excited":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.EXCITED, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "fearful":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.FEARFUL, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "worried":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.WORRIED, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "embarrassed":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.EMBARRASSED, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "sympathetic":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.SYMPATHETIC, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "annoyed":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.ANNOYED, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "approving":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.APPROVING, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "aware":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.AWARE, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "confident":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.CONFIDENT, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "eager":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.EAGER, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "disappointed":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.DISAPPOINTED, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "disapproving":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.DISAPPROVING, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "grateful":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.GRATEFUL, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "mournful":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.MOURNFUL, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "optimistic":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.OPTIMISTIC, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "relieved":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.RELIEVED, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "remorseful":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.REMORSEFUL, emotions['results'][k][0][2])
            
        # elif emotions['results'][k][0][1] == "repulsed":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.REPULSED, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "sad":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.SAD, emotions['results'][k][0][2])

        # elif emotions['results'][k][0][1] == "surprised":
        #     print_gradient_emoji(str(emotions['sents'][k]), RGBStyle.SURPRISED, emotions['results'][k][0][2])

        # ^^^^^^^^^ ADD MORE ^^^^^^^^^

        # j = j + 1  # iterating

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

# Function to print colored gradient from left to right
def print_gradient_left_to_right(text, color_start, color_end):
    # ANSI escape codes for colors
    def rgb_to_ansi(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"
    
    gradient_steps = len(text)
    
    # Extract RGB components for start and end colors
    r_start, g_start, b_start = color_start
    r_end, g_end, b_end = color_end
    
    for i, char in enumerate(text):
        # Calculate intermediate colors for the gradient from left to right
        r = int(r_start + (r_end - r_start) * i / gradient_steps)
        g = int(g_start + (g_end - g_start) * i / gradient_steps)
        b = int(b_start + (b_end - b_start) * i / gradient_steps)
        
        # Apply the color to the character
        print(f"{rgb_to_ansi(r, g, b)}{char}", end="")
    
    print("\033[0m")  # Reset to default color


# Your ASCII art
ascii_art = """
   ███████╗███╗   ███╗ █████╗ ██╗██╗         ████████╗ ██████╗ ███╗   ██╗███████╗
   ██╔════╝████╗ ████║██╔══██╗██║██║         ╚══██╔══╝██╔═══██╗████╗  ██║██╔════╝
   █████╗  ██╔████╔██║███████║██║██║            ██║   ██║   ██║██╔██╗ ██║█████╗
   ██╔══╝  ██║╚██╔╝██║██╔══██║██║██║            ██║   ██║   ██║██║╚██╗██║██╔══╝
   ██╔══╝  ██║╚██╔╝██║██╔══██║██║██║            ██║   ██║   ██║██║╚██╗██║██╔══╝
   ███████╗██║ ╚═╝ ██║██║  ██║██║███████╗       ██║   ╚██████╔╝██║ ╚████║███████╗
   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝       ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝
"""

# Define start and end colors for the gradient (yellow to red)
color_start = (255, 255, 0)  # Yellow RGB
color_end = (255, 0, 0)      # Red RGB

# Print the gradient from left to right for each line of the ASCII art
for line in ascii_art.splitlines():
    print_gradient_left_to_right(line, color_start, color_end)

with open('example_added.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    # print(content) # for Debugging

response = emotionsAPI(content) # API call

emotions = response.json()

# start of our normal code
option = 0
# start if for menu here
while option != '5':
    print("  \nPLEASE SELECT ONE OF OUR MENU OPTIONS")
    option = input("  ╔ 1. Emojify your text\n  ║ 2. Colorify your text\n  ║ 3. Do BOTH\n  ║ 4. Get a Synonym for a word\n  ╚ 5. Leave.\n")
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
