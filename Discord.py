import discord
import asyncio
from discord.ext import commands

#https://discordpy.readthedocs.io/en/latest/api.html#

client = discord.Client()
OwnerID = 766706020080549918

token = "WeirdChamp"

#Discord=Client

def Debug():
    #Quick and dirty host debug for host output | Also accessible though command
    print ("Discord Info: ", discord.version_info)
    print ("Logged In As: ", client.user.name)
    print ("Bot User Info: ", client.user)
    print ("ID: ", client.user.id)
    print ("Bot Version: Alpha 0.1")
    print ("Discord Version: ", discord.__version__)
    print ("Avatar URL: ", client.user.avatar_url)

DebugCall = 1

@client.event
async def on_ready():
    print("Logged In Dank Meme Lord's Bot!")
    activity = discord.Game(name="Andrewsj.co.uk")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    if DebugCall == 1:
        Debug()

@client.event
async def on_message(message):
    # We do not want the bot to reply to itself - Purely cause it fucks the Oracle thing up lmfaoo
    if message.author == client.user:
        return

    if message.content == "!Commands":
        await message.channel.send ("!Commands, !Author, !Website, !Version, , , !Bot, , !ServerInfo, !Help, !Invite")

    elif message.content == "!Author":
        await message.channel.send ("@Andrew A#4644")

    elif message.content == "!Website":
        await message.channel.send ("https://andrewsj.co.uk")

    elif message.content == "!Version":
        await message.channel.send ("Bot Version: Alpha 0.1")

    elif message.content == "!Debug":
    #Quick and dirty host debug
        await message.channel.send ("Discord Info: " + str(discord.version_info))
        await message.channel.send ("Logged In As: " + str(client.user.name))
        await message.channel.send ("Bot User Info: " + str(client.user))
        await message.channel.send ("ID: " + str(client.user.id))
        await message.channel.send ("Bot Version: Alpha 0.1")
        await message.channel.send ("Python Discord Version: " + str(discord.__version__))
        await message.channel.send ("Avatar URL: " + str(client.user.avatar_url))

#EasterEggs
    elif message.content == "!100Spam":
        for i in range(100):
            await message.channel.send ("Easter Egg Found! Wow!")
            await message.add_reaction("😮")

    elif message.content == "!Bot":
        await message.channel.send("I am the spirit of George, I live on as this bot. #420BlazeIt")
        await message.channel.send(file=discord.File('Picture/Bot.webp'))
        await message.channel.send("I was created by the wonderful @Andrew A#4644")
        await message.channel.send("I was programmed to replace @Mee6, even though he's a bot, he's a bellend,")
        await message.channel.send("I know what you're thinking, how can a bot be a bellend?")
        await message.channel.send("```Because he is, fuck you @Mee6.```")

    elif "Oracle" in message.content:
        await message.channel.send("Oracle LUL")
        await message.channel.send(file=discord.File('Picture/Oracle.jpg'))

    elif "Andrew" and  "alcoholic" in message.content:
        await message.add_reaction("🤔")
        await message.channel.send("Hmmmm")
        await message.channel.send(file=discord.File('Picture/ALCCMM.png'))

    elif message.content == "!ServerInfo":
        await message.channel.send ("Server Name: " + message.guild.name)
        await message.channel.send ("Server ID: " + str(message.guild.id))
        await message.channel.send ("Server Emojis: " + str(message.guild.emojis))
        await message.channel.send ("Server Icon: " + message.guild.icon)
        await message.channel.send ("Server Owner ID: " + str(message.guild.owner_id))
        await message.channel.send ("Server Banner: " + str(message.guild.banner))
        await message.channel.send ("Server Description: " + str(message.guild.description))
        await message.channel.send ("Server Channels: " + str(message.guild.channels))
        await message.channel.send ("Server Roles: " + str(message.guild.roles))

    elif message.content == "!Help":
        await message.channel.send ("Try !Commands")

    elif message.content == "!Invite":
        await message.channel.send ("Here's an invite link if you want me in your server https://discordapp.com/oauth2/authorize?scope=bot&client_id=267409712612376584")

#Quick and Dirtyyy Exception Handling
async def on_error(event, *args, **kwargs):
    message = event + args + kwargs #Gets the message object
    await message.channel.send("You caused an error!", message) #send the message to the channel
    print (message)

client.run(token)
