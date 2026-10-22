def get_reply(user_input):
    """Return a predefined reply based on the user's message."""
    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "what is your name":
        return "I'm a simple chatbot made with Python."
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


def chat():
    print("=== Simple Chatbot ===")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print("Bot:", reply)

        if user_input.lower().strip() == "bye":
            break


chat()