import discord
import os
import sys

print("1. Script startet")
TOKEN = os.getenv("TOKEN")
print("2. Token da:", bool(TOKEN))

if not TOKEN:
    print("FEHLER: TOKEN fehlt komplett")
    sys.exit(1)

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"PHOENIX ONLINE ALS {bot.user}")

print("3. Vor bot.run")
try:
    bot.run(TOKEN)
except Exception as e:
    print("FEHLER BEIM LOGIN:", e)
    sys.exit(1)
