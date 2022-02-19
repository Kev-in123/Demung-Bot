import os
import discord
from bot import DemBot

bot = DemBot(token=os.environ['TOKEN'],
             intents=discord.Intents.all(),
             activity=discord.Game("demung"),
             help_command=None)

bot.starter()
