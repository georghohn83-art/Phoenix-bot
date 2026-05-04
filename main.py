import os,threading,discord
from http.server import *
class H(BaseHTTPRequestHandler):def do_GET(self):s.send_response(200);s.end_headers()
threading.Thread(target=lambda:HTTPServer(('0.0.0.0',int(os.getenv('PORT',10000))),H).serve_forever(),daemon=1).start()
bot=discord.Client(intents=discord.Intents.all())
@bot.event
async def on_ready():print("Bot laeuft")
bot.run(os.getenv('DISCORD_TOKEN'))
