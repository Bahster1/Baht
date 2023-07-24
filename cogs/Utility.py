from discord.ext import commands
from utils.Config import TEMPORARY_MESSAGE_DURATION


class Utility(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='purge')
    @commands.has_guild_permissions(manage_messages=True)
    async def clear(self, ctx: commands.Context, amount: int):
        """
        Deletes a specified amount of messages up 100.
        """
        if amount > 100:
            raise commands.BadArgument
        else:
            await ctx.message.delete()
            await ctx.channel.purge(limit=int(amount))
            await ctx.send("Successfully purged messages.", delete_after=TEMPORARY_MESSAGE_DURATION)


async def setup(bot: commands.Bot):
    await bot.add_cog(Utility(bot))
