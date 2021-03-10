import discord
from discord.ext import commands

TOKEN ='ODExNTI0MDE2NzM2NTY3Mjk3.YCzcog.9GTeEKbgflHB-aHk5nx8-ui819I'

description = '''6SV Test'''
bot = commands.Bot(command_prefix='+6SVT', description=description)

@bot.event
async def on_ready():
    print('Loggato come')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def hello(ctx):
    """Says world"""
    await ctx.send("world")


@bot.command()
async def add(ctx, left : int, right : int):
    """Adds two numbers together."""
    await ctx.send(left + right)

bot.run(TOKEN)
