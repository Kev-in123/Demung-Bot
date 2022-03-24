import os
import discord
from bot import DemBot

bot = DemBot(token=os.environ['TOKEN'],
             intents=discord.Intents.all(),
             activity=discord.Activity(
                 type=discord.ActivityType.watching, name='demung'),
             help_command=None)


@bot.check
async def stuff(ctx):
    if ctx.author.id == bot.owner_id or ctx.guild:
        return True
    await ctx.send(f'The `{ctx.invoked_with}` command can only be used in a server')

bot.starter()
