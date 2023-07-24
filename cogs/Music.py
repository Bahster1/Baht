import asyncio
import discord
import yt_dlp as youtube_dl
from discord.ext import commands


# for macos - brew install opus
discord.opus.load_opus("/opt/homebrew/Cellar/opus/1.4/lib/libopus.dylib")

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
	'format': 'bestaudio/best',
	'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
	'restrictfilenames': True,
	'noplaylist': True,
	'nocheckcertificate': True,
	'ignoreerrors': False,
	'logtostderr': False,
	'quiet': True,
	'no_warnings': True,
	'default_search': 'auto',
	'source_address': '0.0.0.0'  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
	'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
queue = []


class YTDLSource(discord.PCMVolumeTransformer):
	def __init__(self, source, *, data, volume=0.5):
		super().__init__(source, volume)

		self.data = data

		self.title = data.get('title')
		self.url = data.get('url')

	@classmethod
	async def from_url(cls, url, *, loop=None, stream=False):
		loop = loop or asyncio.get_event_loop()
		data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

		if 'entries' in data:
			# take first item from a playlist
			data = data['entries'][0]

		filename = data['url'] if stream else ytdl.prepare_filename(data)
		return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="join")
	async def join(self, ctx):
		"""
		Joins a voice channel.
		"""
		if ctx.author.voice is None or ctx.author.voice.channel is None:
			return await ctx.send('You need to be in a voice channel to use this command!')

		voice_channel = ctx.author.voice.channel
		if ctx.voice_client is None:
			vc = await voice_channel.connect()
		else:
			await ctx.voice_client.move_to(voice_channel)
			vc = ctx.voice_client

	@commands.command(name="play")
	async def play(self, ctx, *, url):
		"""
		Streams music.
		"""
		async with ctx.typing():
			player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
			ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
		await ctx.send('Now playing: {}'.format(player.title))

	@commands.command(name="leave")
	async def leave(self, ctx):
		"""
		Stops and disconnects the bot from voice.
		"""
		await ctx.voice_client.disconnect()

	@commands.command(name="pause")
	async def pause(self, ctx):
		"""
		Pauses a playing video.
		"""
		if ctx.voice_client is not None and ctx.voice_client.is_playing():
			ctx.voice_client.pause()
			await ctx.send("Paused!")
		else:
			await ctx.send("There is nothing to pause.")

	@commands.command(name="resume")
	async def resume(self, ctx):
		"""
		Resumes a paused video.
		"""
		if ctx.voice_client is not None and ctx.voice_client.is_paused():
			ctx.voice_client.resume()
			await ctx.send("Resuming")
		else:
			await ctx.send("There is nothing to resume.")

	@play.before_invoke
	async def ensure_voice(self, ctx):
		if ctx.voice_client is None:
			if ctx.author.voice:
				await ctx.author.voice.channel.connect()
			else:
				await ctx.send("You are not connected to a voice channel.")
				raise commands.CommandError("Author not connected to a voice channel.")
		elif ctx.voice_client.is_playing():
			ctx.voice_client.stop()


async def setup(bot: commands.Bot):
	await bot.add_cog(Music(bot))
