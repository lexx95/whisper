class IntentHandler:
    def __init__(self):
        self.intents = {}

    def load_intents(self, file_path):
        import json
        with open(file_path, 'r') as file:
            self.intents = json.load(file)

    def get_response(self, user_input):
        for intent, data in self.intents.items():
            if user_input in data['patterns']:
                return data['responses'][0]
        return "I'm sorry, I don't understand that."