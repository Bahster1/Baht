# Baht

Baht is a general purpose Discord bot that utilizes the [discord.py](https://github.com/Rapptz/discord.py) library.

## Main Features
- Assign, record, and modify user credit scores on a per-server basis.
	- Social credit can only be assigned and previewed for the server the bot is in. It cannot fetch or modify a user's social credit score from other servers besides your own.
	- Only admin users can modify and set other users' social credit scores.
	- Social credit does nothing. It is merely a number that goes up and down at the discretion of the server admins.
- Mass purge messages (for admin users only.)
- Other silly commands that are *totally* unique (not really.)

## Commands
- **add \<user_id\>**
	- Add to a specified user's social credit score. Can only be used by admins. If a user is not specified it will default to yourself.
- **profile \<user_id\>**
	- View a specified user's profile, which will display their current credit score. If a user is not specified it will default to yourself.
- **set \<user_id\> \<integer\>**
	- Set a user's social credit score to a specified number. Can only be used by admins.
- **ding \<user_id\>**
	- Pings a specified user once.
- **flip**
	- Flips a coin. Either heads or tails.
- **ping**
	- Will measure the bot's response ping.
- **pingme \<user_id\> \<integer\>**
	- Will ping a specified user a specified amount of times.
- **roll \<integer\>**
	- Will roll a 10 sided die if an upper limit is not specified.
- **say \<string\>**
	- Will repeat a message you specify. Will delete the message the invokes this command.
- **purge \<integer\>**
	- Will erase a specified amount of messages in the channel. Can only be used by admins.
- **help \<string\>**
	- Will display the help command. Additionally, it will provide extra details of a specified command.
- **join**
  - Will join a voice channel you are currently in.
- **play \<string\>**
  - Will start playing audio from a given url.
- **pause**
  - If playing audio, will pause.
- **resume**
  - If paused, will resume playing audio.
- **leave**
  - Will leave a voice channel if it is in one.

## Installation

Make sure you have [Python 3.5](https://www.python.org) or later before installing!

```bash
# MacOS/Linux
python3 -m pip install -U "discord.py[voice]"

# Windows
py -3 -m pip install -U discord.py[voice]
```

## Configuration

You will need to make this file yourself to input all of your personal tokens and such. It should look like this:
```python
# Baht/utils/Config.py

TOKEN = r'TOKEN HERE'
OWNER_ID = YOUR_ID_HERE
CLIENT_ID = YOUR_BOT_ID_HERE
COMMAND_PREFIX = r'YOUR PREFIX HERE'
TEMPORARY_MESSAGE_DURATION = CUSTOM_DURATION_HERE
```

<br>

If you're not running this bot on a MacOS machine, comment out line 8 in Cogs/Music.py:
```python
discord.opus.load_opus("/opt/homebrew/Cellar/opus/1.4/lib/libopus.dylib")
```
You will not need this on Linux and Windows machines. If you do not comment out or remove this line you will get an error loading the music cog.

## Additional Information

* If you're on MacOS, be sure to run the "Install Certificates.command" file that came bundled with your python installation before running this bot.

(Note: you can obtain this information in the [Discord developer portal](https://discordapp.com/developers/applications/) after creating a bot in your application.)
