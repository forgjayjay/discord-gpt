import os

import discord

from dotenv import load_dotenv
from discord.ext import commands
from bot.gptapi import ask_gpt

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready and online!')

@bot.command(help='Sends a kaomoji symbolizing *Oh My God*')
async def omg(ctx):
    print(f'sending kaomoji (๑>ᴗ<๑)')
    await ctx.send('(๑•́o•̀๑)')

@bot.slash_command(name='gpt', help='Asks a trusty gpt-3.5 with a given argument')
async def gpt(ctx, arg):
    response = ask_gpt(arg)
    await ctx.respond(response)

bot.run(TOKEN)