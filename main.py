import asyncio
import sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())



import discord
import re
import requests


TOKEN = os.environ["TOKEN"]
CANALRAID = 1313162554889076906     

WEBHOOK = os.environ["WEBHOOK"]
ROLAVISO = 1401954486972579952   

invite_regex = re.compile(r"(discord\.gg/|discord\.com/invite/)\S+", re.IGNORECASE)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'conectado como {self.user} ({self.user.id})')

    async def on_message(self, message):
        if message.channel.id != CANALRAID:
            return
        if invite_regex.search(message.content):
            contenido_webhook = f"<@&{ROLAVISO}> {message.content}"
            requests.post(WEBHOOK)
            print("mensaje reenviado al webhook")

client = MyClient()
client.run(TOKEN)
