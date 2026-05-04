import discord
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Phoenix online')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '!phönix':
        await message.channel.send('Ritter Georg, Galaxia lebt!')

client.run(os.getenv("TOKEN"))

