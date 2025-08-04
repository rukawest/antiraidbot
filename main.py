import asyncio
import sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())



import discord
import re
import requests


TOKEN = "MTQwMTUwNTE3MDA5Mjg1NTMyNg.GQIhy6.AHBCHFSSDJlk9rDpBlN8Qt04SioJr0zY3spgog"
CANALRAID = 1313162554889076906     

WEBHOOK = "https://discord.com/api/webhooks/1401955007569592360/xT31w-AaeZdIzgrBkMyhzXsEkT0hdGkVE52Tsc8gaS55936yuHf4DFmcaE3P7vQtiyXQ"
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
