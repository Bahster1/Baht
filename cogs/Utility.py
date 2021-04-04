from discord.ext import commands
from utils.Tools import represents_int
from utils.BotConfig import *


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='CLEAR')
    async def clear(self, ctx, amount=None):
        """
        Deletes up to amount or an accessible amount of messages.
        """
        if represents_int(amount) and 100 >= int(amount) > 0:
            await ctx.channel.purge(limit=int(amount) + 1)
            # TODO: count how many messages were actually cleared
            await ctx.send("Successfully cleared {} messages.".format(amount), delete_after=TEMPORARY_MESSAGE_DURATION)
        else:
            await ctx.send("I cannot delete nothing." if amount is None else
                           "\"{}\" is not a valid input.".format(amount), delete_after=TEMPORARY_MESSAGE_DURATION)


def setup(client):
    client.add_cog(Utility(client))
