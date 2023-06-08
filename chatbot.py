import random

# Define a dictionary with some sample responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I'm doing well, thanks!", "Not too bad, thanks for asking.", "I'm doing great!"],
    "what is your name?": ["My name is ChatBot.", "I'm ChatBot!", "You can call me ChatBot."],
    "who created you?": ["I was created by you."],
    "what can you do?": ["I can answer some common questions.","I can help you with the answers."],
    "bye":["Bye!!","Bye...until next time."],
    "default": ["I'm sorry, I didn't understand. Can you please rephrase that?", "I'm not sure what you mean. Can you please clarify?"]
}

# Define a function to generate a response to user input
def respond(message):
    if message.lower() in responses:
        return random.choice(responses[message.lower()])
    else:
        return random.choice(responses["default"])

# Main loop to keep the chatbot running
print("Hi, I'm ChatBot! How can I help you today?")
while True:
    message = input("You: ")
    print("ChatBot:", respond(message))