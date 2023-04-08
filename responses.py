def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == '!help':
        return 'To query dalle-2: type !dalle, followed by an image description.\nTo query ChatGPT, type !chat, ' \
               'followed by your message.'
