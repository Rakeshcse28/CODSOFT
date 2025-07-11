✅ TASK 1: Chatbot with Rule-Based Responses

🔹 Goal:

Build a chatbot using if-else or pattern matching.

✅ Sample Code (Python):

def chatbot():
    print("Chatbot: Hello! How can I help you today?")
    while True:
        user_input = input("You: ").lower()
        
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How are you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm doing great!")
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a nice day!")
            break
        elif "your name" in user_input:
            print("Chatbot: I'm CodBot, your friendly assistant.")
        else:
            print("Chatbot: Sorry, I didn't understand that.")

chatbot()

📌 Output Example:

You: hi
Chatbot: Hello! How are you?

You: what is your name?
Chatbot: I'm CodBot, your friendly assistant.
