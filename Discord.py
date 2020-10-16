import discord
from discord.ext import commands

client = discord.Client()

token = "WeirdChamp"

info = discord.version_info

def Debug():
    print ("Discord Info: ", discord.version_info)
    print ("Logged In As: ", client.user.name)
    print ("ID: ", client.user.id)
    print ("Bot Version: 0.1")
    print ("Discord Version: ", discord.__version__)
    print ("Avatar URL: ", client.user.avatar_url)

debug = 0

if debug == 1:
    Debug()

async def Awake():
    Author = "Andrew A#4644"
    message = "I'm awake!"


@client.event
async def on_ready():
    print("Logged In! ")
    activity = discord.Game(name="Andrewsj.co.uk")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    #Doesn't work FeelsBadMan
    #await client.send_message(discord.Object(id="766457667903815752"), "I'm awake <3")

@client.event
async def on_message(message):
    if message.content == "!Author":
        await client.send_message(message.channel, "Andrew A#4644")
#Exception Handling
    elif message.content == "raise-exception":
        raise discord.DiscordException

client.run(token)

