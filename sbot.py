import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix='%', intents = intents)

@bot.event
async def on_ready():
    print("\"Water\" and \"Lava\" are ready!")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1302535749295542354)
    await channel.send(f"{member} wants to make obsidian.")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1302565209973592085)
    await channel.send(f"{member} only could make Cobblestone QAQ")

bot.run("MTMwMjU0MDI0Mzk0NTI1OTA4OA.Gjc_Pe.dY61n9yReYgxRI6n4U7P5p_n-omJjMaz8z3ki4")