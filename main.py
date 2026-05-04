import os,threading,discord
from http.server import BaseHTTPRequestHandler, HTTPServer

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Bot is running')

threading.Thread(target=lambda:HTTPServer(('0.0.0.0',int(os.getenv('PORT',10000))),H).serve_forever(),daemon=True).start()

bot=discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot laeuft")

bot.run(os.getenv('DISCORD_TOKEN'))
