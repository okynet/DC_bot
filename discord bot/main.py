import discord

from botmantik import sifre_uret

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$password'):
        await message.channel.send(sifre_uret(10))
    else:
        await message.channel.send(message.content)

client.run("MTE1OTkyMjQ0OTM4Nzg5Mjc0Nw.GtYgem.YJnRpPpAOL3LX8d8Ux4siPXYIvio1P2hxyCmSQ")