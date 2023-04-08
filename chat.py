import openai
import asyncio

openai.api_key = "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"


async def send_request(user_msg):
    conversation = [{'role': 'user', 'content': user_msg}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    conversation.append({'role': 'AI', 'content': response.choices[0]['message']['content']})
    print(conversation)
    return conversation[-1]['content']
