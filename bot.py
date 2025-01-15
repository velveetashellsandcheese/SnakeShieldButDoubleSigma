import discord
import random

intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)

jaydnid = 947418695192436756
smallsid = 429634654190960650
possiblereply = ["shut up", "stop", "no", "nope", "nah", "stop being weird", "you arent allowed to message snake", "think before you speak"]
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Game(name="with ideas to counteract people being weird"))
@client.event # this part is telling to listen and respond
async def on_message(message):
    if message.author == client.user:
        return
    if "snake" in message.content and message.author.id == jaydnid or message.author.id == smallsid and "snake" in message.content:
        print("message found")
        await message.channel.send(random.choice(possiblereply), reference=message)
    elif "SNAKE" in message.content and message.author.id == jaydnid or message.author.id == smallsid and "SNAKE" in message.content:
        print("message found")
        await message.channel.send(random.choice(possiblereply), reference=message)

apikey = input("Enter your bot token: ")
client.run(apikey)
