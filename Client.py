import os
import logging
import discord
from utils.BotConfig import *
from utils.Tools import *
from discord.ext import commands

intents = discord.Intents(messages=True)

client = commands.Bot(command_prefix=COMMAND_PREFIX, case_insensitive=True, owner_id=OWNER_ID, intents=intents)
logging.basicConfig(level=logging.INFO)
client.remove_command('help')


@client.event
async def on_ready():
    print(BOLD + 'Reporting for duty as ' + END + GREEN + '{}'.format(client.user.name) + END)
    print('-------------------------------------')


@client.event
async def on_message(message):
    await client.process_commands(message)


def run():
    for extension in os.listdir('cogs')[:-1]:  # Remove the last item in the list to ignore the __pycache__ directory
        try:
            client.load_extension('cogs.{}'.format(os.path.splitext(extension)[0]))
            print('Loaded {}'.format(extension))
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))
    client.run(TOKEN)
