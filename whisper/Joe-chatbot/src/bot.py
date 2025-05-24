# FILE: /Joe-chatbot/Joe-chatbot/src/bot.py CONTENTS:
import json
from intents.index import IntentHandler
from utils.index import preprocess_input, log_response

class JoeChatbot:
    def __init__(self):
        self.intent_handler = IntentHandler()
        self.intent_handler.load_intents('intents/intents.json')

    def get_response(self, user_input):
        processed_input = preprocess_input(user_input)
        response = self.intent_handler.get_response(processed_input)
        log_response(user_input, response)
        return response

    def run(self):
        print("Hello! I'm Joe, your chatbot. Type 'exit' to end the conversation.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Joe: Goodbye!")
                break
            response = self.get_response(user_input)
            print(f"Joe: {response}")

if __name__ == "__main__":
    chatbot = JoeChatbot()
    chatbot.run()