import openai
import os

# Set the API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")


async def send_request(conversation):
    try:
        # Make API call to ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )

        # Add the response to the conversation history
        conversation.append(
            {'role': 'assistant', 'content': response.choices[0]['message']['content']})

        # Return the updated conversation
        return conversation

    except Exception as e:
        # Print error message if an exception is raised
        print(e)
        return "There was a problem sending your request, wait a moment and try again."
