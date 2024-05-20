from dotenv import load_dotenv
import openai
import os


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


def main():

    print("Welcome to the GPT-3 text generation program.")
    print("Enter 'exit' if you decide you want to exit the program.")
    print("Enter a prompt just as you would on the web interface.")

    chat_history = [];

    while True:
        prompt = input("\nENTER PROMPT HERE: ")
        if prompt == 'exit':
            break

        chat_history.append({"role": "user", "content": prompt})

        try:
            completion = openai.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=chat_history,
                max_tokens=150
        )
            chat_history.append({"role": "assistant", "content": completion.choices[0].message.content});
            print(completion.choices[0].message.content)
        except Exception as e:
                print("An error occurred: ", e)

    print("Exiting the program.")

if __name__ == "__main__":
    main()