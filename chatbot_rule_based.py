print("Welcome to ChatBot! (Type 'bye' to exit)")

name = input("Bot: Before we start, what's your name?\nYou: ")
print(f"Bot: Nice to meet you, {name}! How can I help you?")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you today?")
    elif user_input in ["how are you?", "how are you", "what's up"]:
        print("Bot: I'm just a bot, but I'm doing great!  What about you?")
    elif user_input in ["i am fine", "i'm fine", "doing good"]:
        print("Bot: That's great to hear! How can I assist you?")
    elif "your name" in user_input:
        print("Bot: I'm a simple rule-based chatbot created in Python.")
    elif "help" in user_input:
        print("Bot: Sure! I can chat with you or answer simple questions. Try asking me something!")
    elif user_input in ["bye", "exit", "quit"]:
        print(f"Bot: Goodbye, {name}! Have a great day! ")
        break
    else:
        print("Bot: Sorry, I didn't understand that. Can you rephrase?")