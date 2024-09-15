import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    (r"hi|hello|hey", ["Hello! How can I help you?", "Hi there!", "Hey!"]),
    (r"what is your name?", ["I am a chatbot created to help you. What's your name?"]),
    (r"my name is (.*)", ["Nice to meet you, %1. How can I assist you today?"]),
    (r"how are you?", ["I'm just a program, but I'm functioning as expected. How about you?"]),
    (r"(.*) created you?", ["I was created by a team of Python developers."]),
    (r"(.*) weather (.*)", ["I am not capable of checking real-time weather, but you can use an app for that!"]),
    (r"bye|exit|quit", ["Goodbye!", "See you later!"]),
    (r"(.*)", ["I'm not sure how to respond to that. Could you rephrase?"])
]

chatbot = Chat(pairs, reflections)
print("Chatbot: Hi! I am a basic chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ").lower()
    if user_input == "bye":
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print(f"Chatbot: {response}")
D:\INTERN PROJECT\library-management-project-python\library-management-project-python\basic chatbot.py