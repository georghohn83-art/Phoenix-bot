
    import discord
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

token = os.getenv("DISCORD_TOKEN")

@client.event
async def on_ready():
    print(f'Bot ist online als {client.user}')

client.run(token)
