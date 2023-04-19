import discord
import dalle
import chat
import moderator
import responses
import traceback

<<<<<<< Updated upstream
=======
conversations = []
token=MTA3MTU1MTY1OTc2MDY4MDk4MQ.GR5YJR.TrHbiKmO5zczGyKcvJxz_RGiX8vyqojIyw8Z0E


async def handle_dalle(msg, user_msg):
    if moderator.moderate(user_msg):
        await msg.channel.send("This message violates the OpenAI content policy.")
    else:
        response = await dalle.send_request(user_msg)
        await msg.channel.send(response)


async def handle_chat(msg, user_msg):
    user_msg = user_msg[len('!chat '):].strip()
    if user_msg.startswith('clear'):
        for i in range(len(conversations)):
            if msg.author in conversations[i]:
                conversations.remove(conversations[i])
                await msg.channel.send("Conversation cleared.")
                return
    else:
        if moderator.moderate(user_msg):
            await msg.channel.send("This message violates the OpenAI content policy.")
            return
        convo_exists = False
        for i in range(len(conversations)):
            if msg.author in conversations[i]:
                conversations[i][msg.author].append({'role': 'user', 'content': user_msg})
                convo = conversations[i][msg.author]
                convo_exists = True
        if not convo_exists:
            conversation = [{'role': 'user', 'content': user_msg}]
            convo = conversation
            conversations.append({msg.author: convo})
        response = await chat.send_request(convo)
        await msg.channel.send(response[-1]['content'])


async def handle_davinci(msg, user_msg):
    if moderator.moderate(user_msg):
        await msg.channel.send("This message violates the OpenAI content policy.")
    else:
        prompt = user_msg[len('!davinci '):].strip()
        response = await davinci.send_request(prompt)
        await msg.channel.send(response)


async def handle_help(msg, user_msg):
    response = responses.handle_response("help")
    await msg.channel.send(response)

commands = {
    "!dalle": handle_dalle,
    "!davinci": handle_davinci,
    "!chat": handle_chat,
    "!help": handle_help,
}

>>>>>>> Stashed changes

async def send_message(msg, user_msg):
    try:
        if user_msg.startswith("!dalle"):
            if moderator.moderate(user_msg):
                response = await dalle.send_request(user_msg)
                await msg.channel.send(response)
        elif user_msg.startswith("!chat"):
            if moderator.moderate(user_msg):
                response = await chat.send_request(user_msg)
                await msg.channel.send(response)
        elif user_msg == "!help":
            response = responses.handle_response(user_msg)
            await msg.channel.send(response)
    except Exception as e:
        traceback.print_exc()


def run_discord_bot():
    token = 'MTA3MTU1MTY1OTc2MDY4MDk4MQ.GR5YJR.TrHbiKmO5zczGyKcvJxz_RGiX8vyqojIyw8Z0E'
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_msg = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_msg}' ({channel})")

        await send_message(message, user_msg)
    client.run(token)
