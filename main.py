
import discord
import os
from dotenv import load_dotenv
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

load_dotenv()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content:
        print(message.content)
        await message.channel.send(f"you have send the message {message.content} and more thing darling fuck you")
client.run(os.getenv('TOKEN'))
