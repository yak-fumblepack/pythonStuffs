import discord
import os
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
import requests
import bots.keys
from functools import reduce
import json, wikipedia

load_dotenv()
bot = commands.Bot(command_prefix= ';;')
bot.remove_command("help")
token = os.environ['token']

@bot.event 
async def on_ready():
    print('Bot is online and running')

@bot.command()
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(colour=discord.Colour.green())
    embed.set_author(name='help')
    embed.add_field(
        name=';;ginfo', value='Gives the info of guilds', inline=False)
    embed.add_field(
        name=';;websay',
        value="Lets you talk through a webhook to a predetermined server (admin)",
        inline=False)
    embed.add_field(
        name=";;dmu <userid>", 
        value="Lets you dm a user (admin)", 
        inline=False)
    embed.add_field(
        name=";;dmc <channelid>",
        value="Lets you send messages into another channel",
        inline=False)
    await ctx.send(author, embed=embed)

@bot.command()
async def ginfo(ctx):
    for guild in bot.guilds:
        embed = discord.Embed(title=str(guild), color=0x9966cc)
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name="Owner:", value=guild.owner, inline=False)
        embed.add_field(name="Member count:", value=guild.member_count, inline=False)
        embed.add_field(name="Member names:", value=guild.members, inline=False)
        await ctx.send(embed=embed)

@bot.command()
async def websay(ctx, *args):
    string_to_output = reduce(lambda acc, x: acc+x+' ', args, "")
    requests.post(bot.keys.GENERAL_CHAT_WEBHOOK, data=json.dumps({'content': string_to_output}), headers={'Content-type': 'application/json'})
    requests.post

bot.run(token)