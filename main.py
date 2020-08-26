from discord.ext import commands
import os

from Utils.bot import BotInfo
from Utils.tools import Color


# Client initialization
client = commands.Bot(command_prefix=BotInfo.COMMAND_PREFIX.value)
client.remove_command('help')  
# Remove the default help command so we can make our own


@client.event
async def on_ready():
    """
    When the code runs, this will be the first method to be called.
    This method will initiate any code on startup.
    """
    # Prints a basic message to mark its progress in initialization
    print(Color.BOLD.value + 'Reporting for duty as ' + Color.END.value
          + Color.CYAN.value + '{0}'.format(client.user.name) + Color.END.value)
    print('-------------------------------------')


@client.event
async def on_message(message):
    """
    Initiate any code on a discord message.
    """
    # Processes message as a command if the messages matches any commands' names
    await client.process_commands(message)


if __name__ == '__main__':
    for extension in os.listdir('Cogs')[:-1]:
        try:
            client.load_extension('Cogs.{}'.format(os.path.splitext(extension)[0]))
            print('Loaded {}'.format(extension))
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))
    client.run(BotInfo.TOKEN.value)
