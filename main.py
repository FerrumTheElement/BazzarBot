import discord
import requests
from discord.ext import commands

API_KEY = "apikey" #do /api new on hypixel
c = requests.get(f"https://api.hypixel.net/skyblock/bazaar?key={API_KEY}").json()

client = commands.Bot(command_prefix = '!b ')
    
@client.event
async def on_ready():
    print("Ready!")

@client.command()
async def commands(ctx):
    await ctx.channel.send(f"<@{ctx.author.id}>\n*List Of Commands*\n!b help (assists on how to use !b search)\n!b search <item_name>")

async def help(ctx):
    await ctx.channel.send(f"<@{ctx.author.id}>\nstart with !b <item>. Replace the <space> on an item with a _\nExample: !b search oak_wood")

async def search(ctx,text):
    # text is to read what ever item is after 
    # !b search <whatever item>
        ftext = text.upper()
        # to remove case sensitive
#==========================================================================================
        if ftext == "POTATO":
            ftext = "ITEM_POTATO"
        elif ftext == "RED_MUSHROOM_BLOCK":
            ftext = "HUGE_MUSHROOM_2"
        elif ftext == "ENCHANTED_RED_MUSHROOM_BLOCK":
            ftext = "ENCHANTED_HUGE_MUSHROOM_2"
        elif ftext == "BROWN_MUSHROOM_BLOCK":
            ftext = "HUGE_MUSHROOM_1"
        elif ftext == "ENCHANTED_BROWN_MUSHROOM_BLOCK":
            ftext = "ENCHANTED_HUGE_MUSHROOM_1"
        elif ftext == "COCOA_BEANS":
            ftext = "INK_SACK:3"
        elif ftext == "ENCHANTED_COCOA_BEAN":
            ftext = "ENCHANTED_COCOA"
        elif ftext == "RAW_PORKCHOP":
            ftext = "PORK"
        elif ftext == "RAW_RABBIT":
            ftext = "RABBIT"
        elif ftext == "ENCHANTED_RAW_RABBIT":
            ftext = "ENCHANTED_RABBIT"
        elif ftext == "NETHER_WART":
            ftext = "NETHER_STALK"
        elif ftext == "GUNPOWDER":
            ftext = "SULPHUR"
        elif ftext == "SLIMEBALL":
            ftext = "SLIME_BALL"
        elif ftext == "ENCHANTED_SLIMEBALL":
            ftext = "ENCHANTED_SLIME_BALL"
        elif ftext == "LAPIS_LAZULI":
            ftext = "INK_SACK:4"
        elif ftext == "ENCHANTED_LAPIS_BLOCK":
            ftext = "ENCHANTED_LAPIS_LAZULI_BLOCK"
        elif ftext == "QUARTZ":
            ftext = "NETHER_QUARTZ"
        elif ftext == "END_STONE":
            ftext = "ENDER_STONE"
        elif ftext == "ENCHANTED_END_STONE":
            ftext = "ENCHANTED_ENDSTONE"
        elif ftext == "SNOWBALL":
            ftext = "SNOW_BALL"
        elif ftext == "OAK_WOOD":
            ftext = "LOG"
        elif ftext == "ENCHANTED_OAK_WOOD":
            ftext = "ENCHANTED_OAK_LOG"
        elif ftext == "SPRUCE_WOOD":
            ftext = "LOG:1"
        elif ftext == "ENCHANTED_SPRUCE_WOOD":
            ftext = "ENCHANTED_SPRUCE_LOG"
        elif ftext == "BIRCH_WOOD":
            ftext = "LOG:2"
        elif ftext == "ENCHANTED_BIRCH_WOOD":
            ftext = "ENCHANTED_BIRCH_LOG"
        elif ftext == "DARK_OAK_WOOD":
            ftext = "LOG_2:1"
        elif ftext == "ENCHANTED_DARK_OAK_WOOD":
            ftext = "ENCHANTED_DARK_OAK_LOG"
        elif ftext == "ACACIA_WOOD":
            ftext = "LOG_2"
        elif ftext == "ENCHANTED ACACIA_WOOF":
            ftext = "ENCHANTED_ACACIA_LOG"
        elif ftext == "JUNGLE_WOOD":
            ftext = "LOG:3"
        elif ftext == "ENCHANTED_JUNGLE_WOOD":
            ftext = "ENCHANTED_JUNGLE_LOG"
        elif ftext == "RAW_SALMON":
            ftext = "RAW_FISH:1"
        elif ftext == "CLOWNFISH":
            ftext = "RAW_FISH:2"
        elif ftext == "PUFFERFISH":
            ftext = "RAW_FISH:3"
        elif ftext == "CLAY":
            ftext = "CLAY_BALL"
        elif ftext == "ENCHANTED_CLAY":
            ftext = "ENCHANTED_CLAY_BALL"
        elif ftext == "LILY_PAD":
            ftext = "WATER_LILY"
        elif ftext == "ENCHANTED_LILY_PAD":
            ftext = "ENCHANTED_WATER_LILY"
        elif ftext == "OLD_DRAGON_FRAGMENT":
            ftext = "OLD_FRAGMENT"
        elif ftext == "UNSTABLE_DRAGON_FRAGMENT":
            ftext = "UNSTABLE_FRAGMENT"
        elif ftext == "STRONG_DRAGON_FRAGMENT":
            ftext = "STRONG_FRAGMENT"
        elif ftext == "YOUNG_DRAGON_FRAGMENT":
            ftext = "YOUNG_FRAGMENT"
        elif ftext == "WISE_DRAGON_FRAGMENT":
            ftext = "WISE_FRAGMENT"
        elif ftext == "SUPERIOR_DRAGON_FRAGMENT":
            ftext = "SUPERIOR_FRAGMENT"
        elif ftext == "ENCHANTED_CARROT_ON_A_STICK":
            ftext = "ENCHANTED_CARROT_STICK"
#=================================================================================================================
# wanted to put this in a function but i forgot that ftext needs to be defined before the elif stuff
        
        sell_price = c["products"][ftext]["quick_status"]["sellPrice"]
        buy_price = c["products"][ftext]["quick_status"]["buyPrice"]
        finalx = round(sell_price, 2)
        finaly = round(buy_price, 2)
        # rounding off by 2 decimal places
        await ctx.channel.send(f"<@{ctx.author.id}>\n*{ftext}*\nSell Price: ${finalx}\nBuy Price: ${finaly}")
    
    
    
    
client.run('token',bot=True, reconnect=True)
