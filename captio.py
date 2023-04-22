import discord
import dalle
import davinci
import chat
import responses
import traceback

# Create a list to store chatGPT conversation history
conversations = []


# Define functions to handle the commands
async def handle_dalle(msg, user_msg):
    response = await dalle.send_request(user_msg)
    await msg.channel.send(response)


async def handle_chat(msg, user_msg):
    # Extract message from user input
    user_msg = user_msg[len('!chat '):].strip()

    # If the user input is "clear", remove user's history from conversations
    if user_msg.startswith('clear'):
        for i in range(len(conversations)):
            if msg.author in conversations[i]:
                conversations.remove(conversations[i])
                await msg.channel.send("Conversation cleared.")
                return
    else:
        # Check if the user has an ongoing conversation
        convo_exists = False
        for i in range(len(conversations)):
            if msg.author in conversations[i]:
                conversations[i][msg.author].append({'role': 'user', 'content': user_msg})
                convo = conversations[i][msg.author]
                convo_exists = True

        # Create a conversation record for user if none exists
        if not convo_exists:
            conversation = [{'role': 'user', 'content': user_msg}]
            convo = conversation
            conversations.append({msg.author: convo})

        # Send the request to ChatGPT and await the response
        response = await chat.send_request(convo)

        # Send the bot's response in Discord
        await msg.channel.send(response[-1]['content'])


async def handle_davinci(msg, user_msg):
    # Extract prompt from user input
    prompt = user_msg[len('!davinci '):].strip()

    # Send the prompt to Davinci and await the response
    response = await davinci.send_request(prompt)
    await msg.channel.send(response)


# Send a help message to the user
async def handle_help(msg, user_msg):
    response = responses.handle_response("help")
    display_response = "```"+response+"```"
    await msg.channel.send(display_response)


# Create a dictionary of commands corresponding to handler functions
commands = {
    "!dalle": handle_dalle,
    "!davinci": handle_davinci,
    "!chat": handle_chat,
    "!help": handle_help,
}


# Send user messages to the appropriate command handler
async def send_message(msg, user_msg):
    try:
        for command, handler in commands.items():
            if user_msg.startswith(command):
                await handler(msg, user_msg)
                return
    except Exception as e:

        # Print an error message if an exception is raised
        traceback.print_exc()
        await msg.channel.send(f"There was a problem sending your request: {str(e)}")


# Run the Discord bot
def run_discord_bot(token, test=False):
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():

        # Print confirmation when bot is ready
        print(f'{client.user} is now running')
        if test:
            exit(0)

    # Handle incoming messages
    @client.event
    async def on_message(message):

        # Ignore messages from the bot itself
        if message.author == client.user:
            return

        # Extract user information from messages
        username = str(message.author)
        user_msg = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_msg}' ({channel})")

        await send_message(message, user_msg)

    client.run(token)
