# PyBaht

PyBaht is a general purpose Discord bot that utilizes the [discord.py](https://github.com/Rapptz/discord.py) library.

## Installation

Make sure you have [Python 3.5](https://www.python.org) or higher before installing!


```bash
# OSX
python3 -m pip install -U discord.py

# Windows
py -3 -m pip install -U discord.py
```
(Note: these packages do not come with voice support.)

## Additional Information

* If on OSX, be sure to run the "Install Certificates.command" file that came bundled with your python installation before running this bot. 
* Create a "bot.py" file in the "Utils" package and copy/paste the following code:
```python
from enum import Enum


class BotInfo(Enum):
    TOKEN = r'BOT-TOKEN-HERE'
    OWNER_ID = YOUR-ID-HERE
    CLIENT_ID = CLIENT-ID-HERE
    COMMAND_PREFIX = r'COMMAND-PREFIX-HERE'
```
(Note: you can obtain this information in the [Discord developer portal](https://discordapp.com/developers/applications/) after creating a bot in your application.)
