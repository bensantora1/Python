# Import libraries
import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot rules
pairs = [
    ['hi|hello', ['Hello! How can I assist you?']],
    ['what is your name', ['I am a chatbot created by you.']],
    ['how are you', ['I am fine, thank you!']],
    ['quit', ['Goodbye! Have a great day!']]
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

def main():
    print("Chatbot: Type 'quit' to exit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response if response else 'I do not understand that.'}")

if __name__ == "__main__":
    main()
