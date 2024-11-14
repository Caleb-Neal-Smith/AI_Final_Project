import openai

# Load your OpenAI API key
openai.api_key = "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"

def generate_chatgpt_response(prompt):
    # Corrected function call
    response = openai.completions.create(
        model="gpt-3.5-turbo",  # Use the desired GPT model
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Usage example
if __name__ == "__main__":
    user_input = input("Ask ChatGPT: ")
    chatgpt_response = generate_chatgpt_response(user_input)
    print(f"ChatGPT says: {chatgpt_response}")
