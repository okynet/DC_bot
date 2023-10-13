import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def topla(ctx,sayi1=0, sayi2=0):
    toplam = sayi1 + sayi2
    await ctx.send(toplam)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *liste: str):
    await ctx.send(random.choice(liste))


bot.run("MTE1OTkyMjQ0OTM4Nzg5Mjc0Nw.G4uZqE.YRYG6BMLZAOlmTlxHRh33QxgcZV8wAhQWXMjBE")

