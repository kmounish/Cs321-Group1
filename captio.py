import discord
import dalle
import chat
import moderator
import responses
import traceback

conversations = []


async def send_message(msg, user_msg):
    try:
        if user_msg.startswith("!dalle"):
            if moderator.moderate(user_msg):
                await msg.channel.send("This message violates the OpenAI content policy.")
            else:
                response = await dalle.send_request(user_msg)
                await msg.channel.send(response)
        elif user_msg.startswith("!chat"):
            user_msg = user_msg[len('!chat '):].strip()
            if user_msg.startswith('clear'):
                for i in range(len(conversations)):
                    if msg.author in conversations[i]:
                        conversations.remove(conversations[i])
                        await msg.channel.send("conversation cleared.")
            else:
                if moderator.moderate(user_msg):
                    await msg.channel.send("This message violates the OpenAI content policy.")
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
                        conversations.append({msg.author:convo})
                    response = await chat.send_request(convo)
                    await msg.channel.send(response[-1]['content'])
        elif user_msg == "!help":
            response = responses.handle_response(user_msg)
            await msg.channel.send(response)
    except Exception as e:
        traceback.print_exc()
        await msg.channel.send("There was a problem sending your request. Check if OpenAI is down.")


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
