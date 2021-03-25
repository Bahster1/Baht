from discord.ext import commands

from Utils.config import BotSettings
from Utils.tools import represents_int


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='CLEAR')
    async def clear(self, message, amount=None):
        """
        Deletes a specified amount or targetable amount of messages.
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
    client.add_cog(Utility(client))
