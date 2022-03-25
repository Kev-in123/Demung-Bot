import random
import discord
from helpers import utils
from discord.ext import commands


class levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ignored_channels = ()

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.bot or not msg.guild or msg.channel.id in self.ignored_channels:
            return

        cmd = msg.content.split()
        cmd_check = msg.content and cmd[0] == 'dem' and len(cmd) >= 2 and cmd[1] in [
            a.name for a in self.bot.commands]

        await utils.start(msg.author.id)
        users = await utils.get_users()
        
        if not users[str(msg.author.id)]['blacklisted'] and not cmd_check:
            await utils.add_xp(msg.author.id, random.randrange(1, 26))
            lvl_up = await utils.lvl_up(msg.author.id)
            if lvl_up:
                lvl = await utils.get_lvl(msg.author.id)
                em = discord.Embed(
                    description=f'{msg.author}, leveled up! **{lvl-1} ➜ {lvl}**')
                await msg.channel.send(embed=em)

    @commands.command(name='level')
    async def _level(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        if user not in await utils.get_users():
            await utils.start(user.id)
        lvl = await utils.get_lvl(user.id)
        xp = await utils.get_xp(user.id)
        embed = discord.Embed(title=f'level {lvl}\n{xp} xp')
        embed.set_author(
            name=f'{user.name}#{user.discriminator}', icon_url=user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name='leaderboard', aliases=['lb'])
    async def _lb(self, ctx):
        users = await utils.get_users()
        leader_board = {}
        total = []
        for user in users:
            leader_board[users[user]["xp"]] = int(user)
            total.append(users[user]["xp"])
        total = sorted(total, reverse=True)

        em = discord.Embed(title="The Legion - Leaderboard")
        index = 1
        for amt in total:
            id_ = leader_board[amt]
            member = self.bot.get_user(id_)
            em.add_field(
                name=f"{index}. {member.name}#{member.discriminator}", value=f"{amt} xp",  inline=False)
            if index == 10:
                break
            else:
                index += 1

        em.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(levels(bot))
