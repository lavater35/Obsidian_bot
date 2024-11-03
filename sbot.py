import discord
import json
from os import environ
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = environ["TOKEN"]
with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix='%', intents = intents)

@bot.event
async def on_ready():
    print("\"Water\" and \"Lava\" are ready!")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(jdata[int("welcomes")])
    await channel.send(f"{member} wants to make obsidian.")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(jdata[int("leaves")])
    await channel.send(f"{member} only could make Cobblestone QAQ")
@bot.command()
async def ping(ctx):
    await ctx.send(bot.latency)    

bot.run(token)