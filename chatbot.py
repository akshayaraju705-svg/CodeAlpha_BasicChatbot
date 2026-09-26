# CodeAlpha Internship - Task 4
# Basic Chatbot

print("Chatbot: Hello! I am your basic chatbot.")
print("Chatbot: You can ask me simple questions.")
print("Chatbot: Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Chatbot: Hello! How are you?")

    elif "how are you" in user_input:
        print("Chatbot: I am fine, thank you! How can I help you?")

    elif "your name" in user_input:
        print("Chatbot: My name is CodeBot.")

    elif "what can you do" in user_input:
        print("Chatbot: I can have a simple conversation with you.")

    elif "thank" in user_input:
        print("Chatbot: You're welcome!")

    elif user_input == "bye" or user_input == "exit":
        print("Chatbot: Goodbye! Have a nice day!")
        break

    else:
        print("Chatbot: Sorry, I don't understand that.")

