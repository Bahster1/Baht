# Baht

Baht is a general purpose Discord bot that utilizes the [discord.py](https://github.com/Rapptz/discord.py) library.

## Installation

Make sure you have [Python 3.5](https://www.python.org) or later before installing!


```bash
# MacOS/Linux
python3 -m pip install -U discord.py

# Windows
py -3 -m pip install -U discord.py
```
(Note: these packages do not come with voice support.)

## Additional Information

* If on MacOS, be sure to run the "Install Certificates.command" file that came bundled with your python installation before running this bot. 
* Create a "BotConfig.py" file in the "utils" package and copy/paste the following code:
```python
TOKEN = r'YOUR TOKEN HERE'
OWNER_ID = YOUR ID HERE
CLIENT_ID = CLIENT ID HERE
COMMAND_PREFIX = r'YOUR PREFIX HERE'
TEMPORARY_MESSAGE_DURATION = 5.0
```
(Note: you can obtain this information in the [Discord developer portal](https://discordapp.com/developers/applications/) after creating a bot in your application.)
