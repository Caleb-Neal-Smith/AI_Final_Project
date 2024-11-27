import requests
from pprint import pprint
# key = "XO4JD953SJMKVQM8BOSVVSJCAGUJ5BGX" # Noah's key
key = "QD3LVJOE28KMD9E6C820ET3GAUDUOCSC" # Caleb's key

class RGBStyle:
    ADMIRING = (255, 128, 255)      # Bright Violet - warm admiration
    AMUSED = (255, 215, 64)         # Bright Golden Yellow - playful energy
    ANGRY = (255, 64, 64)           # Bright Red - intense anger
    ANNOYED = (205,28,24)           # Chili red - annoyance/irritation
    APPROVING = (128, 255, 128)     # Bright Lime Green - positive approval
    AWARE = (255, 255, 128)         # Bright Lemon Yellow - clarity
    CONFIDENT = (108,59,170)        # Royal Purple (Reference: https://www.figma.com/colors/royal-purple/) - confidence
    CONFUSED = (137,137,137)        # Gray (Reference: https://www.figma.com/colors/gray/) - confusion
    CURIOUS = (128, 200, 255)       # Bright Sky Blue - inquisitive
    EAGER = (255, 159, 64)          # Bright Pumpkin Orange - enthusiastic
    DISAPPOINTED = (160, 160, 192)   # Bright Slate Gray - letdown
    DISAPPROVING = (203,203,203)    # Cool gray - disapproval
    EMBARRASSED = (255,29,141)      # Rose - embarrassed
    EXCITED = (255,75,51)          # Red-orange - excitement
    FEARFUL = (109,129,150)        # Slate Gray - fear
    GRATEFUL = (128, 255, 192)      # Bright Mint Green - thankful
    JOYFUL = (255, 255, 64)         # Bright Sunshine Yellow - pure joy
    LOVING = (255, 128, 192)        # Bright Rose Pink - affection
    MOURNFUL = (211,211,211)        # Light Gray - mourning
    NEUTRAL = (242,240,239)         # Off-white - neutral
    OPTIMISTIC = (137,243,54)       # Lime green - optimistic (joy combined with interest)
    RELIEVED = (128, 255, 255)      # Bright Aqua Blue - tension release
    REMORSEFUL = (203,203,203)      # Cool gray - regret
    REPULSED = (137,81,41)          # Brown - disgust
    SAD = (217,217,217)             # Platinum - sadness
    WORRIED = (160, 160, 160)       # Bright Neutral Gray - concern
    SURPRISED = (255, 192, 64)      # Bright Marigold - unexpected
    SYMPATHETIC = (106,137,167)     # Blue-gray - sympathy/compassion

def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def color_to_rgb(color):
    r, g, b = color
    return rgb_to_ansi(r, g, b)

# Function to print colored gradient from top to bottom
def print_gradient_emoji(text, color, emoji):
    # ANSI escape codes for colors
    def rgb_to_ansi(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"
    
    # Calculate the intermediate color based on the vertical position
    r, g, b = color
    
    # Apply the color to the entire line
    print(f"{rgb_to_ansi(r, g, b)}{text}\033[0m" + emoji)

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
    j = 0
    finalSentence = ''
    for i in emotions['sents']:
        sentenceTogether = i + emotions['results'][j][0][2]
        finalSentence = finalSentence + ' ' + sentenceTogether
        j = j + 1
    return finalSentence

def colorifyText(emotions):
    j = 0
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

        elif emotions['results'][k][0][1] == "amused":
            # print(RGBStyle.LIGHTVIOLET_BG + RGBStyle.RED + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.AMUSED) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "neutral":
            # print(RGBStyle.LIGHTVIOLET_BG + RGBStyle.RED + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.NEUTRAL) + str(emotions['sents'][k]) + "\033[0m"
            finalSentence = finalSentence + ' ' + sentenceTogether

    return finalSentence

def toneColorEmoji(emotions):
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

        elif emotions['results'][k][0][1] == "amused":
            # print(RGBStyle.LIGHTVIOLET_BG + RGBStyle.RED + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.AMUSED) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

        elif emotions['results'][k][0][1] == "neutral":
            # print(RGBStyle.LIGHTVIOLET_BG + RGBStyle.RED + str(contentList[j]) + "\033[0m")
            sentenceTogether = color_to_rgb(RGBStyle.NEUTRAL) + str(emotions['sents'][k]) + "\033[0m" + emotions['results'][k][0][2]
            finalSentence = finalSentence + ' ' + sentenceTogether

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
    if option == '1': # emojify your email
        print(getEmoji(emotions))

    if option == '2': # colorify your email
        print(colorifyText(emotions))

    if option == '3': # do both
        print(toneColorEmoji(emotions))

    if option == '4': # look up synonyms
        getSynonyms()