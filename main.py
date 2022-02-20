import os
import discord
from bot import DemBot

bot = DemBot(token=os.environ['TOKEN'],
             intents=discord.Intents.all(),
             activity=discord.Activity(
                 type=discord.ActivityType.watching, name='demung'),
             help_command=None)

bot.starter()
