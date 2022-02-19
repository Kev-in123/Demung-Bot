import discord
from discord.ext import commands


class DemHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            em = discord.Embed(description=page)
            await destination.send(embed=em)


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        help_command = DemHelp()
        help_command.cog = self
        bot.help_command = help_command


def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))
