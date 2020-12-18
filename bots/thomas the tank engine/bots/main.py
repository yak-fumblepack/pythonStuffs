import discord
import os
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
import requests
import keys
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
    embed = discord.Embed(
        colour= discord.Colour.green()
    )

    embed.set_author(name='help')
    embed.add_field(name=';;ginfo', value='Gives the info of guilds', inline=False)
    embed.add_field(name=';;websay', value="Lets you talk through a webhook to a predetermined server", inline=False)
    embed.add_field(name=';;define', value="Searches Wikipedia for a definition pertaining to the word", inline=False)
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
    requests.post(keys.GENERAL_CHAT_WEBHOOK, data=json.dumps({'content': string_to_output}), headers={'Content-type': 'application/json'})
    requests.post

def wiki_summary(arg):
    definition = wikipedia.summary(arg, sentences=25, chars=1000000000000, auto_suggest=True, redirect=True)
    return definition

@bot.event
async def on_message(message):
    words = message.content.split()
    important_words = words[1:]

    if message.content.startswith(';;define'):
        words = message.content.split()
        important_words = words[1:]
        search = discord.Embed(
            title="Searching Wikipedia...",
            description=wiki_summary(important_words), 
            color=0x9966cc,
        )
        await message.channel.send(content=None, embed=search)


bot.run(token)