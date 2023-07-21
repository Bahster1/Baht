import asyncio
import random
import time
import discord
from discord.ext import commands


class General(commands.Cog):
    """
    General commands that offer little primary bot use.
    """
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx: commands.Context):
        """
        Measures how long it takes for me to respond to a command.
        """
        before = time.monotonic()
        ping = round((time.monotonic() - before) * 1000, 1)

        await ctx.send(f"Pong! `{ping}ms`")

    @commands.command(name='roll')
    async def roll(self, ctx: commands.Context, maximum: int):
        """
        Rolls a number between 1 and a specified maximum number.
        """
        await ctx.send(f"You got a {random.randint(0, abs(maximum))}")

    @commands.command(name='flip')
    async def flip(self, ctx: commands.Context):
        """
        Flips a coin for heads or tails.
        """
        await ctx.send("You got heads!" if random.randint(0, 1) < 1 else "You got tails!")

    @commands.command(name='say')
    async def say(self, ctx: commands.Context, *, say):
        """
        Repeats the author's message.
        """
        await ctx.message.delete()
        await ctx.send(say)

    @commands.command(name='ding')
    async def ding(self, ctx: commands.Context, user: discord.User):
        """
        Be annoying.
        """
        await ctx.send(f"{user.mention}")

    @commands.command(name='pingme')
    async def pingme(self, ctx: commands.Context, user: discord.User, pings: int):
        """
        Be even more annoying.
        """
        while pings > 0:
            await ctx.send(user.mention)
            pings -= 1
            await asyncio.sleep(1)


async def setup(bot: commands.Bot):
    await bot.add_cog(General(bot))
