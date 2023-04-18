def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'help':
        return ("Welcome to Captio! Here's a list of available commands:\n"
                "!dalle: Generates an image based on your input.\n"
                "!davinci: Provides a text response based on your input.\n"
                "!chat: Engages in a chat with the AI based on your input.\n"
                "!chat remembers conversation history, clear it with !chat clear."
                )
