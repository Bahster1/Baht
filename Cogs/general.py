import discord
from discord.ext import commands
import random
import time

from Utils.config import BotSettings
from Utils.bot import BotInfo
from Utils.tools import represents_int


class General(commands.Cog):
    """
    General commands that offer little primary bot use.
    """
    def __init__(self, client):
        self.client = client

    @commands.command(name='PING')
    async def ping(self, message):
        """
        Check how long it takes for me to respond to a command.
        """
        before = time.monotonic()
        ping = round((time.monotonic() - before) * 1000, 1)

        # Bot response
        await message.channel.send("Pong!" + " `{0}ms`".format(ping))

    @commands.command(name='ROLL')
    async def roll(self, message, maximum=None):
        """
        Rolls a number between 1 and 10 or another specified maximum.
        """
        if maximum is None:
            number = random.randint(0, 10)
            # Bot response
            await message.channel.send("You got a " + str(number))
        elif represents_int(maximum):
            maximum = int(maximum)
            number = random.randint(0, maximum)
            # Bot response
            await message.channel.send("You got a " + str(number))
        else:
            # Bot response
            my_response = await message.channel.send("That is not a valid number!")
            await my_response.edit(delete_after=BotSettings.MESSAGE_DURATION.value)
            
    @commands.command(name='FLIP')
    async def flip(self, message):
        """
        Flips a coin for heads or tails.
        """
        coin_side = random.randint(1, 2)
        if coin_side == 1:
            # Bot response
            await message.channel.send("You got heads!")
        elif coin_side == 2:
            # Bot response
            await message.channel.send("You got tails!")

    @commands.command(name='SAY')
    async def say(self, message, say=None):
        """
        Repeats the author's message.
        """
        await message.channel.purge(limit=1)
        if say is not None:
            # Bot response
            await message.channel.send(say)
        else:
            # Bot response
            my_response = await message.channel.send("You want me to say... nothing?")
            await my_response.edit(delete_after=BotSettings.MESSAGE_DURATION.value)


def setup(client):
    client.add_cog(General(client))
