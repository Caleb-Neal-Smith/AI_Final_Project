import requests

# Your Sapling API key
key = 'QD3LVJOE28KMD9E6C820ET3GAUDUOCSC'
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
