import discord
from discord.ext import commands
import os

from keep_alive import keep_alive
from dotenv import load_dotenv
from time import sleep

import functions

# initialize the bot
client = commands.Bot(command_prefix = "-")

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

# sends a random quote
@client.command()
async def quote(ctx):
    quote = functions.get_quote()
    await ctx.send(quote)

# calculates numbers (only addition, subtracion, multiplication, division and power)
@client.command()
async def calc(ctx, num1 = 'x', op = 'x', num2 = 'x'):
    ans = functions.calculate(num1, op, num2)
    await ctx.send(ans)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(str(amount) + " messages removed")
    sleep(2)
    await ctx.channel.purge(limit=1)

keep_alive()
load_dotenv('.env')
client.run(os.getenv('DISCORD_TOKEN'))
