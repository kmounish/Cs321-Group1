import discord
import dalle
import davinci
import chat
import responses
import traceback

conversations = []


async def handle_dalle(msg, user_msg):
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
    prompt = user_msg[len('!davinci '):].strip()
    response = await davinci.send_request(prompt)
    await msg.channel.send(response)


async def handle_help(msg, user_msg):
    response = responses.handle_response("help")
    display_response = "```"+response+"```"
    await msg.channel.send(display_response)


commands = {
    "!dalle": handle_dalle,
    "!davinci": handle_davinci,
    "!chat": handle_chat,
    "!help": handle_help,
}


async def send_message(msg, user_msg):
    try:
        for command, handler in commands.items():
            if user_msg.startswith(command):
                await handler(msg, user_msg)
                return
        # await msg.channel.send("Invalid command. Type '@Captio' or '!help' for a list of available commands.")
    except Exception as e:
        traceback.print_exc()
        await msg.channel.send(f"There was a problem sending your request: {str(e)}")


def run_discord_bot(token):
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
