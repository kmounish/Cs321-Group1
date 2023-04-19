import openai
import os

openai.api_key = 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 #os.getenv("OPENAI_API_KEY")


async def send_request(conversation):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    conversation.append({'role': 'assistant', 'content': response.choices[0]['message']['content']})
    return conversation
