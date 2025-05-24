def preprocess_input(user_input):
    # Function to clean and prepare user input
    cleaned_input = user_input.strip().lower()
    return cleaned_input

def log_response(response):
    # Function to log the chatbot's responses
    with open("chatbot_log.txt", "a") as log_file:
        log_file.write(response + "\n")