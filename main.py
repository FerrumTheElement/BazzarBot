import requests
import commandfile
from discord.ext import commands

API_KEY = "YOUR_API"
c = requests.get(f"https://api.hypixel.net/skyblock/bazaar?key={API_KEY}").json()
#Requests stuff from the hypixel api when the variable "c" is used
client = commands.Bot(command_prefix = '!b ')
    
@client.event
async def on_ready():
    print("Ready!")
    
@client.command()
async def search(ctx,text):
  await commandfile.search(ctx,text)
#Uses the file "commandfile.py" to search the prices of bazzar in the hypixel api & to print out the output.
client.run('token',bot=True, reconnect=True)
