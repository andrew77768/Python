import discord
import asyncio
from discord.ext import commands

#https://discordpy.readthedocs.io/en/latest/api.html#

client = discord.Client()
OwnerID = 766706020080549918

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
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content == "!Commands":
        await message.channel.send ("!Commands, !Author, !Website, !Version, , , !Bot, , !ServerInfo,")

    elif message.content == "!Author":
        await message.channel.send ("@Andrew A#4644")

    elif message.content == "!Website":
        await message.channel.send ("https://andrewsj.co.uk")

    elif message.content == "!Version":
        await message.channel.send ("Bot Version: Alpha 0.1")

    elif message.content == "!Debug":
        DebugOut = Debug()
        await message.channel.send ("```" + DebugOut + "```")

#EasterEggs
    elif message.content == "!100Spam":
        for i in range(100):
            await message.channel.send ("Easter Egg Found! 100 Spam!")

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

#Exception Handling
async def on_error(event, *args, **kwargs):
    message = args[0,1,2] #Gets the message object
    await message.channel.send("You caused an error!", message) #send the message to the channel

client.run(token)
