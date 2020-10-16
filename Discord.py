import discord

client = discord.Client()

token = "WeirdChamp"

info = discord.version_info

def Debug():
    print (info)

debug = 0

if debug == 1:
           Debug()

@client.event
async def on_ready():
    print("The bot is ready and logged in!")
    activity = discord.Game(name="Andrewsj.co.uk")
    await client.change_presence(status=discord.Status.idle, activity=activity)

@client.event
async def on_message(message):
    if message.content == "!Author":
        await client.send_message(message.channel, "Andrew A")

client.run(token)
