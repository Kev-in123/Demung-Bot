import discord
from discord.ext import commands
from jishaku.codeblocks import codeblock_converter

from helpers import utils


class owner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        start = ('im', 'i\'m', 'i am')
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

    @commands.command(name='eval')
    @commands.is_owner()
    async def _eval(self, ctx, *, code: codeblock_converter):
        cog = self.bot.get_cog('Jishaku')
        await cog.jsk_python(ctx, argument=code)

    @commands.command(description='reload cogs')
    @commands.is_owner()
    async def reload(self, ctx, cog=None):
        if not cog:
            await ctx.send('Please specify a cog')
            return
        try:
            self.bot.reload_extension(f'cogs.{cog}')
        except commands.errors.ExtensionNotLoaded:
            await ctx.send(content=f'{cog} is not loaded')
            return
        await ctx.send(content=f'Done reloading `{cog}`')

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
