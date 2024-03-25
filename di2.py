import os
from dotenv import load_dotenv
load_dotenv()
import discord
def handle_response(response) -> str:
    message = response.lower()
    if "kdo jsi" in message:
        return "Jsem Patrice, česky mluvící chat bot"

    if "jak se máš" in message:
        return "Dobře, díky"
    
async def sendMessage(message, userMessage, private = False):
    try:
        response = handle_response(userMessage)
        if private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e)


def runDiscordBot():
    Dis_key = os.environ.get("DISCORD_API_KEY")

    client = discord.Client()

    @client.event 
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    client.run(Dis_key)
'''    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('kdo jsi?'):
            await sendMessage(message, "kdo jsi?")

        if message.content.startswith('jak se máš?'):
            await sendMessage(message, "jak se máš?")'''

    


if __name__ == "__main__":
    runDiscordBot()