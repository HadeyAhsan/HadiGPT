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

    print("Welcome to HadiGPT")
    print("Type 'quit' to exit.")

    while True:
        prompt = input("You: ")

        if prompt.lower() == "quit":
            break

        response = generate_response(prompt, api_key)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
