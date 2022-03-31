import discord
from discord.ext import commands

from helpers import utils


class owner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        if not msg.guild:
            return
        start = ('im ', 'i\'m ', 'i am ')
        if msg.content.lower().startswith(start[0]):
            await msg.channel.send(f'hi {msg.content[3:]}, im Demung')
        elif msg.content.lower().startswith(start[1]):
            await msg.channel.send(f'hi {msg.content[4:]}, im Demung')
        elif msg.content.lower().startswith(start[2]):
            await msg.channel.send(f'hi {msg.content[5:]}, im Demung')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):
        if isinstance(err, commands.CommandNotFound):
            return

    @commands.command(description='blacklist a user')
    @commands.is_owner()
    async def blacklist(self, ctx, user: discord.Member):
        blacklist = await utils.blacklist(user.id)
        if blacklist:
            await ctx.send(f'user {user} has been blacklisted')
            return
        unblacklist = await utils.unblacklist(user.id)
        if unblacklist:
            await ctx.send(f'user {user}\'s  blacklist has been removed')
            return
        await ctx.send('u fked up')


def setup(bot):
    bot.add_cog(owner(bot))
