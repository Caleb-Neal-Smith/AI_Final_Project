import requests
from pprint import pprint

# This class sets the variable for each color
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

# reading the email from sepcified file
# we can make this a command line argmunet later
with open('example.txt', 'r') as file:
    content = file.read()
    # print(content) # for Debugging

# delimiting the list
# spliting the contents every newline character
contentList = content.split("\n")

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
            "text": contentList[i] # sending the data of the list
        }
    )
    # print(response.json()) # for Debugging
    responseList.append(response) # appending the response to the response list
    # pprint(responseList[i].json())
    i = i + 1 # iterating

# pprint(responseList.json()) # for Debugging
# print(style.BLUE + "Hello, World!" + "\033[0m") # for Debugging
j = 0

# iterating through the response list
while j < len(responseList):
    val = responseList[j].json()
    # pprint(val['results'][0][0][1])
    
    # checking the returned emotion/ tone value
    # and changing output color appropriatly
    if val['results'][0][0][1] == "angry":
        print(style.RED + str(contentList[j]) + "\033[0m")
        
    elif val['results'][0][0][1] == "admiring":
        print(style.BLUE + str(contentList[j]) + "\033[0m")
        
    elif val['results'][0][0][1] == "curious":
        print(style.CYAN + str(contentList[j]) + "\033[0m")
        
    elif val['results'][0][0][1] == "confused":
        print(style.GREEN + str(contentList[j]) + "\033[0m")
        
    # TEMP BLOW to add more 
    # elif val['results'][0][0][1] == "##":
    #     print(style.RED + str(contentList[j]) + "\033[0m")
        
    # elif val['results'][0][0][1] == "##":
    #     print(style.RED + str(contentList[j]) + "\033[0m")
        
    # elif val['results'][0][0][1] == "##":
    #     print(style.RED + str(contentList[j]) + "\033[0m")
    # ^^^^^^^^^ ADD MORE ^^^^^^^^^
        
    j = j + 1 # iterating