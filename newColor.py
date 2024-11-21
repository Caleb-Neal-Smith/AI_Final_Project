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

# class RGBStyle:
#     ADMIRING = (255, 128, 255)      # Bright Violet
#     AMUSED = (255, 215, 64)         # Bright Golden Yellow
#     ANGRY = (255, 64, 64)           # Bright Red
#     ANNOYED = (255, 128, 80)        # Bright Orange-Red
#     APPROVING = (128, 255, 128)     # Bright Lime Green
#     AWARE = (255, 255, 128)         # Bright Lemon Yellow
#     CONFIDENT = (64, 128, 255)      # Bright Royal Blue
#     CONFUSED = (192, 128, 255)      # Bright Lavender
#     CURIOUS = (128, 200, 255)       # Bright Sky Blue
#     EAGER = (255, 159, 64)          # Bright Pumpkin Orange
#     DISAPPOINTED = (160, 160, 192)  # Bright Slate Gray
#     DISAPPROVING = (192, 128, 64)   # Bright Warm Brown
#     EMBARRASSED = (255, 128, 160)   # Bright Blush Pink
#     EXCITED = (255, 96, 64)         # Bright Flame Red
#     FEARFUL = (160, 80, 40)         # Bright Chestnut Brown
#     GRATEFUL = (128, 255, 192)      # Bright Mint Green
#     JOYFUL = (255, 255, 64)         # Bright Sunshine Yellow
#     LOVING = (255, 128, 192)        # Bright Rose Pink
#     MOURNFUL = (96, 128, 160)       # Bright Steel Blue
#     NEUTRAL = (192, 192, 192)       # Bright Silver Gray
#     OPTIMISTIC = (255, 223, 64)     # Bright Goldenrod
#     RELIEVED = (128, 255, 255)      # Bright Aqua Blue
#     REMORSEFUL = (192, 96, 64)      # Bright Russet
#     REPULSED = (160, 255, 160)      # Bright Soft Green
#     SAD = (96, 160, 255)            # Bright Cerulean Blue
#     WORRIED = (160, 160, 160)       # Bright Neutral Gray
#     SURPRISED = (255, 192, 64)      # Bright Marigold
#     SYMPATHETIC = (255, 128, 128)   # Bright Coral

# class RGBStyle:
#     ADMIRING = (255, 182, 193)      # Light Pink
#     AMUSED = (255, 215, 0)          # Gold
#     ANGRY = (255, 0, 0)             # Red
#     ANNOYED = (255, 107, 107)       # Coral Red
#     APPROVING = (144, 238, 144)     # Light Green
#     AWARE = (230, 230, 250)         # Lavender
#     CONFIDENT = (65, 105, 225)      # Royal Blue
#     CONFUSED = (221, 160, 221)      # Plum
#     CURIOUS = (255, 165, 0)         # Orange
#     EAGER = (255, 228, 181)         # Moccasin
#     DISAPPOINTED = (119, 136, 153)   # Light Slate Gray
#     DISAPPROVING = (139, 0, 0)      # Dark Red
#     EMBARRASSED = (255, 182, 193)    # Light Pink
#     EXCITED = (255, 105, 180)       # Hot Pink
#     FEARFUL = (128, 0, 0)           # Maroon
#     GRATEFUL = (152, 251, 152)      # Pale Green
#     JOYFUL = (255, 255, 0)          # Yellow
#     LOVING = (255, 105, 180)        # Hot Pink
#     MOURNFUL = (72, 61, 139)        # Dark Slate Blue
#     NEUTRAL = (128, 128, 128)       # Gray
#     OPTIMISTIC = (135, 206, 235)    # Sky Blue
#     RELIEVED = (176, 224, 230)      # Powder Blue
#     REMORSEFUL = (105, 105, 105)    # Dim Gray
#     REPULSED = (85, 107, 47)        # Dark Olive Green
#     SAD = (70, 130, 180)            # Steel Blue
#     WORRIED = (147, 112, 219)       # Medium Purple
#     SURPRISED = (0, 255, 255)       # Cyan
#     SYMPATHETIC = (222, 184, 135)   # Burlywood

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