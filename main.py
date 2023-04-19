import captio
import os

if __name__ == '__main__':
    token = os.getenv('DISCORD_BOT_TOKEN')
    if not token:
        print("Environment variable DISCORD_BOT_TOKEN is not set.")
    else:
        captio.run_discord_bot(token)
