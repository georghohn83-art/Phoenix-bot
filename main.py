import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print(f'Bot ist online als {client.user}')

@client.command()
async def ping(ctx):
    await ctx.send("Pong! Ich lebe endlich.")

client.run(os.getenv("DISCORD_TOKEN"))
