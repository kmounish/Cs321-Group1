import captio
import os

if __name__ == '__main__':

    # retrieve Discord bot token from environment variable
    token = os.getenv('DISCORD_BOT_TOKEN')

    if not token:
        # Print error message if token does not exist
        print("Environment variable DISCORD_BOT_TOKEN is not set.")
    else:
        captio.run_discord_bot(token)
