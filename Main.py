import asyncio
import Bot
from utils.Config import TOKEN


async def main():
	async with Bot.client:
		await Bot.load_extensions()
		await Bot.client.start(TOKEN)

asyncio.run(main())
