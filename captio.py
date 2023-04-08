import discord
import dalle
import chat
import moderator
import responses
import traceback


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
