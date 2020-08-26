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

    @commands.command(name='ping')
    async def ping(self, message):
        """
        A user end test command to confirm the bot's ability to respond and to measure its ping in milliseconds.
        """
        before = time.monotonic()
        ping = round((time.monotonic() - before) * 1000, 1)

        # Bot response
        await message.channel.send("Pong!" + " `{0}ms`".format(ping))

    @commands.command(name='roll')
    async def roll(self, message, maximum=None):
        """
        A simple command that sends a random number between one and a set maximum.
        All custom maximums are checked to validate whether or not it is an integer before it proceeds.
        If the custom maximum is not an integer, an error message will let the user know that it was not a valid input.
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

    @commands.command(name='flip')
    async def flip(self, message):
        """
        Generates a random integer between one and two.
        One equalling heads and two equalling tails.
        This will notify the user what the result is.
        """
        coin_side = random.randint(1, 2)
        if coin_side == 1:
            # Bot response
            await message.channel.send("You got heads!")
        elif coin_side == 2:
            # Bot response
            await message.channel.send("You got tails!")

    @commands.command(name='say')
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

    @commands.command(name='clear')
    async def clear(self, message, amount=None):
        """
        Deletes a specified amount, or targetable amount, of messages.
        """
        if amount is None:
            # Bot response
            my_response = await message.channel.send("I cannot delete nothing.")
            await my_response.edit(delete_after=BotSettings.MESSAGE_DURATION.value)
        elif represents_int(amount):
            amount = int(amount)
            if amount > 100:
                # Bot response
                my_response = await message.channel.send("I cannot delete more than 100 messages at a time.")
                await my_response.edit(delete_after=BotSettings.MESSAGE_DURATION.value)
            else:
                # Bot response
                await message.channel.purge(limit=amount + 1)
                my_response = await message.channel.send("Successfully cleared {0} messages.".format(amount))
                await my_response.edit(delete_after=BotSettings.MESSAGE_DURATION.value)
        else:
            # Bot response
            my_response = await message.channel.send("That is not a valid input.")
            await my_response.edit(delete_after=BotSettings.MESSAGE_DURATION.value)

def setup(client):
    client.add_cog(General(client))
