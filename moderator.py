import openai
import os


openai.api_key = os.getenv("OPENAI_API_KEY")


def moderate(user_msg):
    response = openai.Moderation.create(
        input=user_msg
    )
    moderation_flag = False
    output = response["results"][0]["categories"]
    for categories in output.keys():
        if output[categories]:
            print(
                f"This message is contains {categories} messages, can not perform task")
            moderation_flag = True

    return moderation_flag
