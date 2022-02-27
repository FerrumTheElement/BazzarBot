import requests
import list
from discord.ext import commands



API_KEY = "cd6d59c7-811a-45de-a5b2-76af30a3e719"
c = requests.get(f"https://api.hypixel.net/skyblock/bazaar?key={API_KEY}").json()

client = commands.Bot(command_prefix = '!b ')
    
@client.event
async def on_ready():
    print("Ready!")
@client.command()
async def search(ctx,text):
  await list.search(ctx,text)


    
client.run('OTQyOTkxNTQ4MTM4Nzk1MDQ4.YgsjUQ.GIzrLAQDVWL5-8M4Qyyb7NoKCBk',bot=True, reconnect=True)