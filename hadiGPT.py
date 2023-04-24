import openai

def generate_response(prompt, api_key):
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()

def main():
    api_key = "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"

    print("Welcome to the GPT-3 chatbot!")
    print("Type 'quit' to exit the chatbot.")

    while True:
        prompt = input("You: ")

        if prompt.lower() == "quit":
            break

        response = generate_response(prompt, api_key)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
