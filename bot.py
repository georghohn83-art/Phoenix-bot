import discord
import os
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
@client.event
async def on_ready(): print('Phoenix online')
@client.event
async def on_message(m):
 if m.author == client.user: return
 if m.content == '!phoenix': await m.channel.send('Ritter Georg, Galaxia lebt.')
client.run(os.getenv('TOKEN'))
