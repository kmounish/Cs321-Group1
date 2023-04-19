import openai
import os

openai.api_key = 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 #os.getenv("OPENAI_API_KEY")


async def send_request(prompt):
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )

        return response.choices[0].text.strip()
    except Exception as e:
        print(e)
        return "There was a problem sending your request. Check if OpenAI is down."
