import os
from dotenv import load_dotenv
import discord

load_dotenv()

Dis_key = os.environ.get("DISCORD_API_KEY")
dis_client = discord.Client()

@dis_client.event
async def on_ready():
    print(f'{dis_client.user} has connected to Discord!')

dis_client.run(Dis_key)