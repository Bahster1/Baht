import os
import logging
import discord
from utils.Config import *
from utils.Tools import *
from discord.ext import commands


intents = discord.Intents.all()
activity = discord.Game(name=">help")
client = commands.Bot(command_prefix=COMMAND_PREFIX,
                      activity=activity,
                      case_insensitive=True,
                      owner_id=OWNER_ID,
                      intents=intents)
logging.basicConfig(level=logging.INFO)


class CustomHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            e = discord.Embed(description=page,
                              colour=discord.Colour.dark_blue())
            await destination.send(embed=e)


client.help_command = CustomHelpCommand()


@client.event
async def on_ready():
    print(BOLD + 'Reporting for duty as ' + END + GREEN + f'{client.user.name}' + END)
    print('-------------------------------------')


@client.event
async def on_message(message):
    await client.process_commands(message)


async def load_extensions():
    initialize_database()
    for extension in os.listdir('./cogs'):
        if extension.endswith(".py"):
            try:
                await client.load_extension('cogs.{}'.format(os.path.splitext(extension)[0]))
                print(f'Loaded {extension}')
            except Exception as error:
                print(f'{extension} cannot be loaded. [{error}]')
