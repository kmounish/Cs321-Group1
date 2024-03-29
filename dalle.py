import requests
import os

# Set the API key from environment variable
API_KEY = os.getenv("DALLE_API_KEY")


async def send_request(user_msg):
    try:
        if user_msg.startswith('!dalle '):
            # Extract the text to generate an image from the user message
            text = user_msg[len('!dalle '):].strip()

            # Make the API call to DALLE-2
            response = requests.post('https://api.openai.com/v1/images/generations', json={
                'model': 'image-alpha-001',
                'prompt': f'{text}\n\nImage:',
                'num_images': 1,
                'size': '512x512',
                'response_format': 'url'
            }, headers={
                'Authorization': f'Bearer {API_KEY}'
            })

            # Parse the response to get the generated image URL
            response.raise_for_status()
            response_data = response.json()
            image_url = response_data['data'][0]['url']

            return image_url

    except Exception as e:
        # Print error message if an exception is raised
        print(e)
        return "There was a problem sending your request, wait a moment and try again."
