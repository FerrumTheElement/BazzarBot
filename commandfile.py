from discord.ext import commands
import requests
import discord

API_KEY = "YOUR API"
c = requests.get(f"https://api.hypixel.net/skyblock/bazaar?key={API_KEY}").json()

async def on_message(message):
  print(message.content)

@commands.command()
async def search(ctx, text):
    ftext = text.upper()
        # to remove case sensitive
        #==========================================================================================
    if ftext == "POTATO":
        ftext = "POTATO_ITEM"
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
        ftext = "WISE_FRAAGMENT"
    elif ftext == "SUPERIOR_DRAGON_FRAGMENT":
        ftext = "SUPERIOR_FRAGMENT"
    elif ftext == "ENCHANTED_CARROT_ON_A_STICK":
        ftext = "ENCHANTED_CARROT_STICK"
    elif ftext == "ROUGH_RUBY_GEMSTONE":
        ftext = "ROUGH_RUBY_GEM"
    elif ftext == "FLAWED_RUBY_GEMSTONE":
        ftext = "FLAWED_RUBY_GEM"
    elif ftext == "FLAWLESS_RUBY_GEMSTONE":
        ftext = "FLAWLESS_RUBY_GEM"
    elif ftext == "FINE_RUBY_GEMSTONE":
        ftext = "FINE_RUBY_GEM"
    elif ftext == "PERFECT_RUBY_GEMSTONE":
        ftext = "PERFECT_RUBY_GEM"
    elif ftext == "MITHRIL":
        ftext = "MITHRIL_ORE"
    elif ftext == "TITANIUM":
        ftext = "TITANIUM_ORE"
    elif ftext == "GOLDEN_JERRY_BOX":
        ftext = "JERRY_BOX_GOLDEN"
    elif ftext == "PURPLE_JERRY_BOX":
        ftext = "JERRY_BOX_PURPLE"
    elif ftext == "GREEN_JERRY_BOX":
        ftext = "JERRY_BOX_GREEN"
    elif ftext == "BLUE_JERRY_BOX":
        ftext = "JERRY_BOX_BLUE"
    elif ftext == "DWARVEN_SUPER_COMPACTOR":
        ftext = "DWARVEN_COMPACTOR"
    elif ftext == "ROUGH_JADE_GEMSTONE":
        ftext = "ROUGH_JADE_GEM"
    elif ftext == "FLAWED_JADE_GEMSTONE":
        ftext = "FLAWED_JADE_GEM"
    elif ftext == "FINE_JADE_GEMSTONE":
        ftext = "FINE_JADE_GEM"
    elif ftext == "FLAWLESS_JADE_GEMSTONE":
        ftext = "FLAWLESS_JADE_GEM"
    elif ftext == "PERFECT_JADE_GEMSTONE":
        ftext = "PERFECT_JADE_GEM"
    elif ftext == "ROUGH_AMBER_GEMSTONE":
        ftext = "ROUGH_AMBER_GEM"
    elif ftext == "FLAWED_AMBER_GEMSTONE":
        ftext = "FLAWED_AMBER_GEM"
    elif ftext == "FINE_AMBER_GEMSTONE":
        ftext = "FINE_AMBER_GEM"
    elif ftext == "FLAWLESS_AMBER_GEMSTONE":
        ftext = "FLAWLESS_AMBER_GEM"
    elif ftext == "PERFECT_AMBER_GEMSTONE":
        ftext = "PERFECT_AMBER_GEM"
    elif ftext == "ROUGH_TOPAZ_GEMSTONE":
        ftext = "ROUGH_TOPAZ_GEM"
    elif ftext == "FLAWED_TOPAZ_GEMSTONE":
        ftext = "FLAWED_TOPAZ_GEM"
    elif ftext == "FINE_TOPAZ_GEMSTONE":
        ftext = "FINE_TOPAZ_GEM"
    elif ftext == "FLAWLESS_TOPAZ_GEMSTONE":
        ftext = "FLAWLESS_TOPAZ_GEM"
    elif ftext == "PERFECT_TOPAZ_GEMSTONE":
        ftext = "PERFECT_TOPAZ_GEM"
    elif ftext == "ROUGH_SAPPHIRE_GEMSTONE":
        ftext = "ROUGH_SAPPHIRE_GEM"
    elif ftext == "FLAWED_SAPPHIRE_GEMSTONE":
        ftext = "FLAWED_SAPPHIRE_GEM"
    elif ftext == "FINE_SAPPHIRE_GEMSTONE":
        ftext = "FINE_SAPPHIRE_GEM"
    elif ftext == "FLAWLESS_SAPPHIRE_GEMSTONE":
        ftext = "FLAWLESS_SAPPHIRE_GEM"
    elif ftext == "PERFECT_SAPPHIRE_GEMSTONE":
        ftext = "PERFECT_SAPPHIRE_GEM"
    elif ftext == "ROUGH_AMETHYST_GEMSTONE":
        ftext = "ROUGH_AMETHYST_GEM"
    elif ftext == "FLAWED_AMETHYST_GEMSTONE":
        ftext = "FLAWED_AMETHYST_GEM"
    elif ftext == "FINE_AMETHYST_GEMSTONE":
        ftext = "FINE_AMETHYST_GEM"
    elif ftext == "FLAWLESS_AMETHYST_GEMSTONE":
        ftext = "FLAWLESS_AMETHYST_GEM"
    elif ftext == "PERFECT_AMETHYST_GEMSTONE":
        ftext = "PERFECT_AMETHYST_GEM"
    elif ftext == "ROUGH_JASPER_GEMSTONE":
        ftext = "ROUGH_JASPER_GEM"
    elif ftext == "FLAWED_JASPER_GEMSTONE":
        ftext = "FLAWED_JASPER_GEM"
    elif ftext == "FINE_JASPER_GEMSTONE":
        ftext = "FINE_JASPER_GEM"
    elif ftext == "FLAWLESS_JASPER_GEMSTONE":
        ftext = "FLAWLESS_JASPER_GEM"
    elif ftext == "PERFECT_JASPER_GEMSTONE":
        ftext = "PERFECT_JASPER_GEM"
    elif ftext == "GREEN_GOBLIN_EGG":
        ftext = "GOBLIN_EGG_GREEN"
    elif ftext == "BLUE_GOBLIN_EGG":
        ftext = "GOBLIN_EGG_BLUE"
    elif ftext == "RED_GOBLIN_EGG":
        ftext = "GOBLIN_EGG_RED"
    elif ftext == "YELLOW_GOBLIN_EGG":
        ftext = "GOBLIN_EGG_YELLOW"
    elif ftext == "ARACHNE'S_KEEPER_FRAGMENT":
        ftext = "ARACHNE_KEEPER_FRAGMENT"
    elif ftext == "CHEESE":
        ftext = "CHEESE_FUEL"
#==========================================================
#Converts visible itemname into item_id so that the hypixel api can read it
    sell_price = c["products"][ftext]["quick_status"]["sellPrice"]
    buy_price = c["products"][ftext]["quick_status"]["buyPrice"]
    buy_orderprice = c["products"][ftext]["buy_summary"][0]["pricePerUnit"]
    sell_orderprice = c["products"][ftext]["sell_summary"][0]["pricePerUnit"]
#requests things to the hypixel api
    finalx = round(sell_price, 2)
    finaly = round(buy_price, 2)
    title_text = text.title()
#just making it look nice :)
    embed=discord.Embed(title=f"Price info for {title_text}", description=f"Sell Price: ${finalx}\nSell OrderPrice: ${sell_orderprice}\n\nBuy Price: ${finaly}\nBuy OrderPrice: ${buy_orderprice}", color=discord.Color.blue())
    await ctx.channel.send(embed=embed)
    #sends text


      


