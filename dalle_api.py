import requests


async def send_request(user_message):
    try:
        if user_message.startswith('!dalle '):
            # Extract the text to generate an image from the user message
            text = user_message[len('!dalle '):].strip()

            # Make the API call to DALLE-2
            response = requests.post('https://api.openai.com/v1/images/generations', json={
                'model': 'image-alpha-001',
                'prompt': f'{text}\n\nImage:',
                'num_images': 1,
                'size': '512x512',
                'response_format': 'url'
            }, headers={
                'Authorization': f'Bearer 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'
            })

            # Parse the response to get the generated image URL
            response.raise_for_status()
            response_data = response.json()
            image_url = response_data['data'][0]['url']

            return image_url
    except Exception as e:
        print(e)