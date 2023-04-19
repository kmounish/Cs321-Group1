import captio
import os

if __name__ == '__main__':
    token = MTA3MTU1MTY1OTc2MDY4MDk4MQ.GR5YJR.TrHbiKmO5zczGyKcvJxz_RGiX8vyqojIyw8Z0E #os.getenv('DISCORD_BOT_TOKEN')
    if not token:
        print("Environment variable DISCORD_BOT_TOKEN is not set.")
    else:
        captio.run_discord_bot(token)
