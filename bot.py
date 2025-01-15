import discord
import random

intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)

#these two are tests atm
jaydnid = 947418695192436756
smallsid = 429634654190960650
bannedidlist = [jaydnid, smallsid]
#lets you add more people to the banned list
while True:
    print("Banned ID list: ", bannedidlist)
    print("Enter the ID of the user you want to ban from messaging snake. If you are done, type 'done'")
    bannedid = input()
    if bannedid == "done":
        break
    bannedidlist.append(int(bannedid))
#possible replys to blacklisted users
possiblereply = ["shut up", "stop", "no", "nope", "nah", "stop being weird", "you arent allowed to message snake", "think before you speak", "back off my goat", "SOMEONE HELP","negative", "nuh-uh", "no way", "not happening", "forget it", "MODS HELP "  ]



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')



#this part of the code is what makes the bot reply to messages
@client.event 
async def on_message(message):
    if message.author == client.user:
        return
    message.content = message.content.lower()   
    if "snake" in message.content and message.author.id in bannedidlist:
        print("message found")
        await message.channel.send(random.choice(possiblereply), reference=message)
    elif "SNAKE" in message.content and message.author.id in bannedidlist:      
        print("message found")
        await message.channel.send(random.choice(possiblereply), reference=message)


#api key 
apikey = input("Enter your bot token: ")
client.run(apikey)
