import os
import logging
import discord
import asyncio
import re

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')
bot = commands.Bot(command_prefix='h!')
#TODO Change logging level whenever merging to master ##########################
logging.basicConfig(level=logging.WARN)


@bot.event
async def on_ready():
    print(f"CONNECTED!\nBot client: [{bot.user}]\n~~~~~~~~")
    print("Connected to the following guilds:")
    for guild in bot.guilds:
        print(f" - {guild}")
    activity = discord.Activity(name='the words fly by', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)


@bot.command(name='dlchat', help='Downloads all chat messages of a specified person with their @ mention name')
async def dlchat(ctx, arg):
    arg = str(re.sub(r'[^0-9]', '', arg))
    file = open(f"msgs_by_{arg}_in_#{ctx.channel}_in_server-{ctx.guild}.txt", 'w')
    print(f"Running dlchat in #{ctx.channel} in {ctx.guild}...")
    async for message in ctx.channel.history(limit=200):
        if str(message.author.id) == arg:
            file.write(message.content + "\n")
    file.close()
    await ctx.channel.send(f'Messages from user <@{arg}> in the channel #{ctx.channel} have been downloaded and saved to the text file in the operating directory.')
    print("dlchat completed running! check the output for the messages")


bot.run(token)
