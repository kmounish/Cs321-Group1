def handle_response(message) -> str:
    msg = message.lower()

    if msg == 'help':

        # Print a helpful message detailing the usage of the bot
        return ("Welcome to Captio! Here's a list of available commands:\n\n"
                "!dalle: Generates an image based on your input.\n\n"
                "!davinci: Provides a text response based on your input.\n\n"
                "!chat: Engages in a chat with the AI based on your input.\n\n"
                "!chat remembers conversation history, clear it with !chat clear.\n\n"
                "You can send Captio private messages or talk with it in any channel."
                )
