import openai
import os

def generate_response(prompt, api_key):
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()

def main():
    api_key = os.environ.get("OPENAI_API_KEY")

    if api_key is None:
        print("Error: Please set the OPENAI_API_KEY environment variable.")
        exit(1)

    print("Welcome to HadiGPT")
    print("Type 'quit' to exit.")

    conversation_history = ""

    while True:
        prompt = input("You: ")

        if prompt.lower() == "quit":
            break

        response = generate_response(prompt, api_key)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
