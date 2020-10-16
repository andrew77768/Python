import discord
import asyncio
from discord.ext import commands

#https://discordpy.readthedocs.io/en/latest/api.html#

client = discord.Client()

token = "WeirdChamp"

#Discord=Client

def Debug():
    print ("Discord Info: ", discord.version_info)
    print ("Logged In As: ", client.user.name)
    print ("Bot User Info: ", client.user)
    print ("ID: ", client.user.id)
    print ("Bot Version: Alpha 0.1")
    print ("Discord Version: ", discord.__version__)
    print ("Avatar URL: ", client.user.avatar_url)

DebugCall = 0

@client.event
async def on_ready():
    print("Logged In! ")
    activity = discord.Game(name="Andrewsj.co.uk")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    if DebugCall == 1:
        Debug()

@client.event
async def on_message(message):
    if message.content == "!Commands":
        await message.channel.send ("!Commands, !Author, !Website, !Version, !Debug")
    elif message.content == "!Author":
        await message.channel.send ("@Andrew A#4644")
    elif message.content == "!Website":
        await message.channel.send ("https://andrewsj.co.uk")
    elif message.content == "!Version":
        await message.channel.send ("Alpha 0.1")
    elif message.content == "!Debug":
        #DebugOut = Debug()
        await message.channel.send ("```" + Debug() + "```")
#Exception Handling
    elif message.content == "raise-exception":
        raise discord.DiscordException
        await message.channel.send (discord.DiscordException)

client.run(token)
