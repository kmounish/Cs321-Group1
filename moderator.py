import openai


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

    print('in moderate', moderation_flag)
    return moderation_flag
