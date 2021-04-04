import random
import time
from discord.ext import commands
from utils.Tools import represents_int
from utils.BotConfig import *


class General(commands.Cog):
    """
    General commands that offer little primary bot use.
    """
    def __init__(self, client):
        self.client = client

    @commands.command(name='PING')
    async def ping(self, ctx):
        """
        Check how long it takes for me to respond to a command.
        """
        before = time.monotonic()
        ping = round((time.monotonic() - before) * 1000, 1)

        await ctx.send("Pong!" + " `{0}ms`".format(ping))

    @commands.command(name='ROLL')
    async def roll(self, ctx, maximum=None):
        """
        Rolls a number between 1 and 10 or another specified maximum.
        """
        if represents_int(maximum) and int(maximum) > 0:
            await ctx.send("You got a {}".format(random.randint(0, int(maximum))))
        elif maximum is None:
            await ctx.send("You got a {}".format(random.randint(0, 10)))
        else:
            await ctx.send("\"{}\" is not a valid input.".format(maximum), delete_after=TEMPORARY_MESSAGE_DURATION)

    @commands.command(name='FLIP')
    async def flip(self, ctx):
        """
        Flips a coin for heads or tails.
        """
        await ctx.send("You got heads!" if random.randint(0, 1) < 1 else "You got tails!")

    @commands.command(name='SAY')
    async def say(self, ctx, say=None):
        """
        Repeats the author's message.
        """
        if say is not None:
            await ctx.message.delete()
            await ctx.send(say)
        else:
            await ctx.send("You want me to say... nothing?", delete_after=TEMPORARY_MESSAGE_DURATION)


def setup(client):
    client.add_cog(General(client))
