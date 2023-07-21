from discord.ext import commands
from utils.Config import *


class ErrorHandler(commands.Cog):
    """
    Cog for global error handling.
    """
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.MissingRequiredArgument):
            message = "Error: missing required arguments."
        elif isinstance(error, commands.UserInputError):
            message = "Error: bad arguments."
        elif isinstance(error, commands.MissingPermissions):
            message = "You do not have permission to use this command."
        else:
            message = str(error)

        print(error)
        await ctx.send(message, delete_after=TEMPORARY_MESSAGE_DURATION)
        await ctx.message.delete(delay=TEMPORARY_MESSAGE_DURATION)


async def setup(bot: commands.Bot):
    await bot.add_cog(ErrorHandler(bot))
