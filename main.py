import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f'Bot ist online als {client.user}')
    print('------')

@client.command()
async def ping(ctx):
    await ctx.send("Pong! Ich lebe.")

client.run(os.getenv("DISCORD_TOKEN"))
