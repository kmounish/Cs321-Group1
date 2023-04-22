import openai
import os

# Set the API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")


async def send_request(prompt):
    try:
        # Make API call to DaVinci
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )
        # Filter the response text and return it
        unfiltered_response = response.choices[0].text.strip()
        filtered_response = "```"+unfiltered_response+"```"
        return filtered_response

    except Exception as e:
        # Print error message if an exception is raised
        print(e)
        return "There was a problem sending your request, wait a moment and try again."
