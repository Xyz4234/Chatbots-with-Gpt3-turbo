import openai
import os

# Retrieve the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("No API key found. Please set the OPENAI_API_KEY environment variable.")

messages = []

# Customizable user name
user_name = input("Please enter your name:\n")

# Greeting the user
greeting_msg = f"Hi {user_name}! Welcome to your personalized assistant."
print(greeting_msg)

# Adding the greeting to messages for context
messages.append({"role": "system", "content": greeting_msg})

# Informing about GPT
info_msg = (
    "You're currently interacting with a GPT-3.5-turbo model. "
    "This assistant can help you with various tasks, and you can even create your own model to meet specific needs."
)
print(info_msg)
messages.append({"role": "system", "content": info_msg})

# Asking the type of chatbot they want to create
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while True:
    message = input()
    if message.lower() == "quit()":
        print("Goodbye!")
        break
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
