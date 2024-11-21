import requests
from pprint import pprint
key = "QD3LVJOE28KMD9E6C820ET3GAUDUOCSC"

# class RGBStyle:
#     AMUSED = (255, 200, 87)         # Golden Yellow
#     ANGRY = (215, 38, 61)          # Bright Red
#     ANNOYED = (242, 92, 84)        # Muted Red-Orange
#     APPROVING = (109, 163, 77)     # Fresh Green
#     AWARE = (255, 210, 63)         # Golden Yellow
#     CONFIDENT = (72, 106, 176)     # Deep Blue
#     CONFUSED = (156, 139, 217)     # Lavender Purple
#     CURIOUS = (123, 189, 255)      # Sky Blue
#     EAGER = (255, 159, 67)         # Vivid Orange
#     DISAPPOINTED = (112, 128, 144) # Muted Gray-Blue
#     DISAPPROVING = (153, 76, 0)    # Earthy Brown
#     EMBARRASSED = (255, 182, 193)  # Pale Pink
#     EXCITED = (255, 99, 71)        # Tomato Red
#     FEARFUL = (112, 66, 20)        # Dark Brown
#     GRATEFUL = (144, 238, 144)     # Soft Green
#     JOYFUL = (255, 223, 0)         # Bright Yellow
#     LOVING = (255, 105, 180)       # Hot Pink
#     MOURNFUL = (47, 79, 79)        # Dark Slate Gray
#     NEUTRAL = (128, 128, 128)      # Neutral Gray
#     OPTIMISTIC = (255, 215, 0)     # Golden Yellow
#     RELIEVED = (135, 206, 235)     # Soft Sky Blue
#     REMORSEFUL = (139, 69, 19)     # Saddle Brown
#     REPULSED = (85, 107, 47)       # Olive Green
#     SAD = (70, 130, 180)           # Steel Blue
#     WORRIED = (169, 169, 169)      # Muted Gray
#     SURPRISED = (255, 140, 0)      # Bright Orange
#     SYMPATHETIC = (205, 92, 92)    # Rosy Red
#     ADMIRING = (148, 0, 211)       # Soft Violet (RGB for Violet)
#     YELLOW = (255, 255, 0)  # Yellow RGB

class RGBStyle:
    ADMIRING = (255, 128, 255)      # Bright Violet
    AMUSED = (255, 215, 64)         # Bright Golden Yellow
    ANGRY = (255, 64, 64)           # Bright Red
    ANNOYED = (255, 128, 80)        # Bright Orange-Red
    APPROVING = (128, 255, 128)     # Bright Lime Green
    AWARE = (255, 255, 128)         # Bright Lemon Yellow
    CONFIDENT = (64, 128, 255)      # Bright Royal Blue
    CONFUSED = (192, 128, 255)      # Bright Lavender
    CURIOUS = (128, 200, 255)       # Bright Sky Blue
    EAGER = (255, 159, 64)          # Bright Pumpkin Orange
    DISAPPOINTED = (160, 160, 192)  # Bright Slate Gray
    DISAPPROVING = (192, 128, 64)   # Bright Warm Brown
    EMBARRASSED = (255, 128, 160)   # Bright Blush Pink
    EXCITED = (255, 96, 64)         # Bright Flame Red
    FEARFUL = (160, 80, 40)         # Bright Chestnut Brown
    GRATEFUL = (128, 255, 192)      # Bright Mint Green
    JOYFUL = (255, 255, 64)         # Bright Sunshine Yellow
    LOVING = (255, 128, 192)        # Bright Rose Pink
    MOURNFUL = (96, 128, 160)       # Bright Steel Blue
    NEUTRAL = (192, 192, 192)       # Bright Silver Gray
    OPTIMISTIC = (255, 223, 64)     # Bright Goldenrod
    RELIEVED = (128, 255, 255)      # Bright Aqua Blue
    REMORSEFUL = (192, 96, 64)      # Bright Russet
    REPULSED = (160, 255, 160)      # Bright Soft Green
    SAD = (96, 160, 255)            # Bright Cerulean Blue
    WORRIED = (160, 160, 160)       # Bright Neutral Gray
    SURPRISED = (255, 192, 64)      # Bright Marigold
    SYMPATHETIC = (255, 128, 128)   # Bright Coral

# Function to print colored gradient from top to bottom
def print_gradient(text, color, tone):
    # ANSI escape codes for colors
    def rgb_to_ansi(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"
    
    # Calculate the intermediate color based on the vertical position
    r, g, b = color
    
    # Apply the color to the entire line
    print(f"{rgb_to_ansi(r, g, b)}{text}\033[0m" + " " + str(color) + " " + tone + "\033[0m")

def responseAPI(text):
    response = requests.post(
        "https://api.sapling.ai/api/v1/tone",
        json={
            "key": key,
            "text": text
        }
    )
    return response

ascii_art = """Testing this stuv out
Thank you so much for your help—it truly means a lot to me.
This is one of the best days ever; I feel like I'm walking on sunshine!
I care about you deeply and will always be here for you.
Their loss has left a huge void; it's hard to imagine life without them.
I don't have strong feelings about this one way or the other.
I really believe that things are going to get better soon.
I'm so glad that worked out; a huge weight has been lifted.
I deeply regret what happened, and I wish I could change it.
That's absolutely disgusting; I can't even look at it.
I've been feeling down lately; it's been a tough time.
I can't stop thinking about what might go wrong.
I didn't see that coming at all—what a shock!
I'm here for you, and I truly understand what you're going through."""

# # Total number of lines in the ASCII art
# total_lines_list = ascii_art.split('\n')
# total_lines = len(total_lines_list)

# # Print the gradient from top to bottom
# for step, line in enumerate(ascii_art.split('\n')):
#     print_gradient(line, color)


# res = emojiAPI(ascii_art)


# print_gradient(ascii_art, RGBStyle.REPULSED)
with open('example_added.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# delimiting the list
# splitting the contents every newline character
contentList = content.split("\n") #Use period or newline here?

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
    
    # debugging
    # pprint(val['results'][0][0][1])

    # checking the returned emotion/ tone value
    # and changing output color appropriately
    if val['results'][0][0][1] == "angry":
        print_gradient(str(contentList[j]), RGBStyle.ANGRY, val['results'][0][0][1])

    elif val['results'][0][0][1] == "admiring":
        print_gradient(str(contentList[j]), RGBStyle.ADMIRING, val['results'][0][0][1])

    elif val['results'][0][0][1] == "curious":
        print_gradient(str(contentList[j]), RGBStyle.CURIOUS, val['results'][0][0][1])

    elif val['results'][0][0][1] == "confused":
        print_gradient(str(contentList[j]), RGBStyle.CONFUSED, val['results'][0][0][1])

    # TEMP BLOW to add more 
    elif val['results'][0][0][1] == "joyful":
        print_gradient(str(contentList[j]), RGBStyle.JOYFUL, val['results'][0][0][1])

    elif val['results'][0][0][1] == "loving":
        print_gradient(str(contentList[j]), RGBStyle.LOVING, val['results'][0][0][1])

    elif val['results'][0][0][1] == "excited":
        print_gradient(str(contentList[j]), RGBStyle.EXCITED, val['results'][0][0][1])

    elif val['results'][0][0][1] == "fearful":
        print_gradient(str(contentList[j]), RGBStyle.FEARFUL, val['results'][0][0][1])

    elif val['results'][0][0][1] == "worried":
        print_gradient(str(contentList[j]), RGBStyle.WORRIED, val['results'][0][0][1])

    elif val['results'][0][0][1] == "embarrassed":
        print_gradient(str(contentList[j]), RGBStyle.EMBARRASSED, val['results'][0][0][1])

    elif val['results'][0][0][1] == "sympathetic":
        print_gradient(str(contentList[j]), RGBStyle.SYMPATHETIC, val['results'][0][0][1])

    elif val['results'][0][0][1] == "annoyed":
        print_gradient(str(contentList[j]), RGBStyle.ANNOYED, val['results'][0][0][1])

    elif val['results'][0][0][1] == "approving":
        print_gradient(str(contentList[j]), RGBStyle.APPROVING, val['results'][0][0][1])

    elif val['results'][0][0][1] == "aware":
        print_gradient(str(contentList[j]), RGBStyle.AWARE, val['results'][0][0][1])

    elif val['results'][0][0][1] == "confident":
        print_gradient(str(contentList[j]), RGBStyle.CONFIDENT, val['results'][0][0][1])

    elif val['results'][0][0][1] == "eager":
        print_gradient(str(contentList[j]), RGBStyle.EAGER, val['results'][0][0][1])

    elif val['results'][0][0][1] == "disappointed":
        print_gradient(str(contentList[j]), RGBStyle.DISAPPOINTED, val['results'][0][0][1])

    elif val['results'][0][0][1] == "disapproving":
        print_gradient(str(contentList[j]), RGBStyle.DISAPPROVING, val['results'][0][0][1])

    elif val['results'][0][0][1] == "grateful":
        print_gradient(str(contentList[j]), RGBStyle.GRATEFUL, val['results'][0][0][1])

    elif val['results'][0][0][1] == "mournful":
        print_gradient(str(contentList[j]), RGBStyle.MOURNFUL, val['results'][0][0][1])

    elif val['results'][0][0][1] == "optimistic":
        print_gradient(str(contentList[j]), RGBStyle.OPTIMISTIC, val['results'][0][0][1])

    elif val['results'][0][0][1] == "relieved":
        print_gradient(str(contentList[j]), RGBStyle.RELIEVED, val['results'][0][0][1])

    elif val['results'][0][0][1] == "remorseful":
        print_gradient(str(contentList[j]), RGBStyle.REMORSEFUL, val['results'][0][0][1])
    elif val['results'][0][0][1] == "repulsed":
        print_gradient(str(contentList[j]), RGBStyle.REPULSED, val['results'][0][0][1])

    elif val['results'][0][0][1] == "sad":
        print_gradient(str(contentList[j]), RGBStyle.SAD, val['results'][0][0][1])

    elif val['results'][0][0][1] == "surprised":
        print_gradient(str(contentList[j]), RGBStyle.SURPRISED, val['results'][0][0][1])

    # ^^^^^^^^^ ADD MORE ^^^^^^^^^

    j = j + 1  # iterating



###############################################################################################################################################################
# import requests
# from pprint import pprint

# class RGBStyle:
#     ADMIRING = '\033[35m'       # Soft Violet
#     AMUSED = '\033[93m'         # Golden Yellow
#     ANGRY = '\033[91m'          # Bright Red
#     ANNOYED = '\033[91m'        # Muted Red-Orange
#     APPROVING = '\033[32m'      # Fresh Green
#     AWARE = '\033[93m'          # Golden Yellow
#     CONFIDENT = '\033[94m'      # Deep Blue
#     CONFUSED = '\033[95m'       # Lavender Purple
#     CURIOUS = '\033[96m'        # Sky Blue
#     EAGER = '\033[33m'          # Vivid Orange
#     DISAPPOINTED = '\033[90m'   # Muted Gray-Blue
#     DISAPPROVING = '\033[33m'   # Earthy Brown
#     EMBARRASSED = '\033[95m'    # Pale Pink
#     EXCITED = '\033[91m'        # Tomato Red
#     FEARFUL = '\033[90m'        # Dark Brown
#     GRATEFUL = '\033[92m'       # Soft Green
#     JOYFUL = '\033[93m'         # Bright Yellow
#     LOVING = '\033[95m'         # Hot Pink
#     MOURNFUL = '\033[90m'       # Dark Slate Gray
#     NEUTRAL = '\033[37m'        # Neutral Gray
#     OPTIMISTIC = '\033[93m'     # Golden Yellow
#     RELIEVED = '\033[96m'       # Soft Sky Blue
#     REMORSEFUL = '\033[33m'     # Saddle Brown
#     REPULSED = '\033[32m'       # Olive Green
#     SAD = '\033[94m'            # Steel Blue
#     WORRIED = '\033[90m'        # Muted Gray
#     SURPRISED = '\033[33m'      # Bright Orange
#     SYMPATHETIC = '\033[91m'    # Rosy Red

#     RESET = '\033[0m'
    
    
# # reading the email from specified file
# # we can make this a command line argument later
# with open('example_added.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     # print(content) # for Debugging

# # delimiting the list
# # splitting the contents every newline character
# contentList = content.split("\n")

# # pprint(contentList) # for Debugging

# responseList = []
# i = 0

# # iterating through the list of content
# # the code inside the while loop is pretty much straight from the sapling website
# while i < len(contentList):
#     response = requests.post(
#         "https://api.sapling.ai/api/v1/tone",
#         json={
#             "key": "XO4JD953SJMKVQM8BOSVVSJCAGUJ5BGX",
#             "text": contentList[i]  # sending the data of the list
#         }
#     )
#     # print(response.json()) # for Debugging
#     responseList.append(response)  # appending the response to the response list
#     # pprint(responseList[i].json())
#     i = i + 1  # iterating

# # pprint(responseList.json()) # for Debugging
# # print(RGBStyle.BLUE + "Hello, World!" + "\033[0m") # for Debugging
# j = 0

# # iterating through the response list
# while j < len(responseList):
#     val = responseList[j].json()
#     # pprint(val['results'][0][0][1])

#     # checking the returned emotion/ tone value
#     # and changing output color appropriately
#     if val['results'][0][0][1] == "angry":
#         print(RGBStyle.ANGRY + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "admiring":
#         print(RGBStyle.ADMIRING + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "curious":
#         print(RGBStyle.CURIOUS + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "confused":
#         print(RGBStyle.CONFUSED + str(contentList[j]) + "\033[0m")

#     # TEMP BLOW to add more 
#     elif val['results'][0][0][1] == "joyful":
#         print(RGBStyle.JOYFUL + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "loving":
#         print(RGBStyle.LOVING + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "excited":
#         print(RGBStyle.EXCITED + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "fearful":
#         print(RGBStyle.FEARFUL + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "worried":
#         print(RGBStyle.WORRIED + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "embarrassed":
#         print(RGBStyle.EMBARRASSED + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "sympathetic":
#         print(RGBStyle.SYMPATHETIC + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "annoyed":
#         print(RGBStyle.ANNOYED + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "approving":
#         print(RGBStyle.APPROVING + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "aware":
#         print(RGBStyle.AWARE + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "confident":
#         print(RGBStyle.CONFIDENT + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "eager":
#         print(RGBStyle.EAGER + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "disappointed":
#         print(RGBStyle.DISAPPOINTED + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "disapproving":
#         print(RGBStyle.DISAPPROVING + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "grateful":
#         print(RGBStyle.GRATEFUL + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "mournful":
#         print(RGBStyle.MOURNFUL + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "optimistic":
#         print(RGBStyle.OPTIMISTIC + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "relieved":
#         print(RGBStyle.RELIEVED + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "remorseful":
#         print(RGBStyle.REMORSEFUL)
#     elif val['results'][0][0][1] == "repulsed":
#         print(RGBStyle.REPULSED + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "sad":
#         print(RGBStyle.SAD + str(contentList[j]) + "\033[0m")

#     elif val['results'][0][0][1] == "surprised":
#         print(RGBStyle.SURPRISED + RGBStyle.RED + str(contentList[j]) + "\033[0m")

#     # ^^^^^^^^^ ADD MORE ^^^^^^^^^

#     j = j + 1  # iterating
