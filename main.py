import discord
from discord.ext import commands
import os

from keep_alive import keep_alive
import functions

client = commands.Bot(command_prefix = "-")

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.command()
async def quote(ctx):
    quote = functions.get_quote()
    await ctx.send(quote)

@client.command()
async def calc(ctx, num1 = 'x', op = 'x', num2 = 'x'):
    ans = functions.calculate(num1, op, num2)
    await ctx.send(ans)

keep_alive()
client.run(os.getenv('TOKEN'))
