# This example requires the 'message_content' intent.
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from MYgroq import respondToDiscordMessage

load_dotenv()
DISCORD_API_KEY_PY = os.environ.get("DISC_API_KEY")
CHANNEL_ID = 1173578978993393695
startChars = '--'

intents = discord.Intents.default()
intents.message_content = True

#bot = commands.Bot(command_prefix='--', intents=intents)
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    channelHere = bot.get_channel(CHANNEL_ID)
    #await channelHere.send('Hello!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith(startChars):
        answer = respondToDiscordMessage(message.content[len(startChars):])
        await message.channel.send(answer)


bot.run(DISCORD_API_KEY_PY)
