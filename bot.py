import discord
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot ist online als {client.user}')
    print(f'Shard ID 0 hat sich mit dem Gateway verbunden')

client.run(os.getenv("DISCORD_BOT_TOKEN"))
