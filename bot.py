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


#TODO this is where the real mess is
@bot.command(name='dlchat', help='Downloads all chat messages of a specified person with their @ mention name **without links**')
async def dlchat2(ctx, author_handle, scan_length=None):
    if scan_length is not None: scan_length = int(scan_length)
    author_handle = str(re.sub(r'[^0-9]', '', author_handle))
    file = open(f"msgs_by_{author_handle}_in_#{ctx.channel}_in_server-{ctx.guild}.txt", 'w')
    print(f"Running dlchat in #{ctx.channel} in {ctx.guild}...")
    async for message in ctx.channel.history(limit=scan_length):
        if str(message.author.id) == author_handle:
            msg = re.sub(r'https?://\S+', '', message.content) #TODO make this work when a link comes after text ex. "hello http://q.com hello" should be "hello hello"
            if msg != "":
                try:
                    file.write(msg + "\n")
                except:
                    print(f'Skipping the following message due to an error:\n{msg}')
                    #TODO get actual handling for errors here (the one I had was UnicodeEncodeError when mapping \u30c4 [Katakana Tsu])
                    #It was also a part of CommandInvokeError from discord.ext
    file.close()
    await ctx.channel.send(f'Messages from user <@{author_handle}> in the channel #{ctx.channel} have been downloaded (without links) and saved to the text file in the operating directory.')
    print("Chat downloading completed running! check the output for the messages")


#TODO update this command to be a little cleaner
@bot.command(name='dlallchat', help='Downloads all chat messages of a specified person with their @ mention name')
async def dlchat(ctx, handle, scan_length):
    handle = str(re.sub(r'[^0-9]', '', handle))
    file = open(f"msgs_by_{handle}_in_#{ctx.channel}_in_server-{ctx.guild}.txt", 'w')
    print(f"Running dlchat in #{ctx.channel} in {ctx.guild}...")
    async for message in ctx.channel.history(limit=int(scan_length)):
        if str(message.author.id) == handle:
            if message.content != "":
                try:
                    file.write(message.content + "\n")
                except:
                    print("Probably ran into a unusable character. Skipping...")
                    #TODO get actual handling for errors here (the one I had was UnicodeEncodeError when mapping \u30c4 [Katakana Tsu])
                    #It was also a part of CommandInvokeError from discord.ext
    file.close()
    await ctx.channel.send(f'Messages from user <@{handle}> in the channel #{ctx.channel} have been downloaded and saved to the text file in the operating directory.')
    print("Chat downloading completed running! check the output for the messages")


bot.run(token)
