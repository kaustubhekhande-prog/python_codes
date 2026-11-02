def run():
    print("Chatbot: Hello! How can I help you?")

    while True:
        user = input("You: ").lower().strip()

        if user in ("hello", "hi"):
            print("Bot: Hello! Nice to meet you.")
        elif user == "how are you":
            print("Bot: I am fine. What about you?")
        elif user == "your name":
            print("Bot: I am a Python Chatbot.")
        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I don't understand.")


if __name__ == "__main__":
    run()
