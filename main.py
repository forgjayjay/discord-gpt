import os
import discord
import random

from discord.ext import commands
from dotenv import load_dotenv
from bot.gptapi import ask_gpt
from bot.emoticons import emoticons

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command(help='Sends a kaomoji symbolizing *Oh My God*')
async def omg(ctx):
    print(f'sending kaomoji (๑>ᴗ<๑)')
    await ctx.send('(๑•́o•̀๑)')

@bot.command(help='Sends a random kaomoji')
async def kaomoji(ctx):
    await ctx.send(random.choice(emoticons))

@bot.slash_command(name='gpt', help='Asks a trusty gpt-3.5 with a given argument')
async def gpt(ctx, argument):
    await ctx.defer()
    response = ask_gpt(argument)
    await ctx.respond(response)

@bot.event
async def on_ready():
    print(f'{bot.user} is ready and online!')

bot.run(TOKEN)