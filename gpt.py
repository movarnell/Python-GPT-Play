from dotenv import load_dotenv
import openai
import os

load_dotenv()


# Set the OpenAI API key
# apiKey = os.getenv("OPENAI_API_KEY")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY




# prompt the user for input

def main():
    # Set the OpenAI API key
    # openai.api_key = apiKey



    print("Welcome to the GPT-3 text generation program.")
    print("Enter a prompt to generate text based on that prompt.")
    print("Enter 'exit' to exit the program.")

    chat_history = [];

    while True:
        prompt = input("Enter a prompt: ")
        if prompt == 'exit':
            break

        chat_history.append({"role": "user", "content": prompt})

        try:
            completion = openai.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=chat_history,
                max_tokens=400
        )
            chat_history.append({"role": "assistant", "content": completion.choices[0].message.content});
            print(completion.choices[0].message.content)
        except Exception as e:
                print("An error occurred: ", e)

    print("Exiting the program.")

if __name__ == "__main__":
    main()