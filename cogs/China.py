import typing
import discord
from discord.ext import commands
from utils.Tools import *


# TODO Make special gifs for positive and negative social credit scores
# TODO Large numbers are weird. Set a max and a min or find some way to make large numbers consistent in arithmetic
class China(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(name='add')
	@commands.has_guild_permissions(administrator=True)
	async def add_social_credit(self, ctx: commands.Context, user: typing.Optional[discord.User], social_credit: int):
		"""
		Add to one's or your own social credit score.
		Admin use only.
		"""
		user_id = user.id if user is not None else ctx.author.id
		user_name = user.display_name if user is not None else ctx.author.display_name
		user_display_avatar = user.display_avatar if user is not None else ctx.author.display_avatar

		add_social_credit(user_id, ctx.guild.id, social_credit)
		social_credit = get_social_credit(user_id, ctx.guild.id)

		embed = discord.Embed(colour=discord.Colour.red(),
		                      description=f"**{user_name}'s** social credit is now **{social_credit}**",
		                      title="ADDING SOCIAL CREDIT")
		embed.set_thumbnail(url=user_display_avatar)

		await ctx.send(embed=embed)

	@commands.command(name='set')
	@commands.has_guild_permissions(administrator=True)
	async def set_social_credit(self, ctx: commands.Context, user: typing.Optional[discord.User], social_credit: int):
		"""
		Set one's or your own social credit score.
		Admin use only.
		"""
		user_id = user.id if user is not None else ctx.author.id
		user_name = user.display_name if user is not None else ctx.author.display_name
		user_display_avatar = user.display_avatar if user is not None else ctx.author.display_avatar

		set_social_credit(user_id, ctx.guild.id, social_credit)
		social_credit = get_social_credit(user_id, ctx.guild.id)

		embed = discord.Embed(colour=discord.Colour.red(),
		                      description=f"**{user_name}'s** social credit is now **{social_credit}**",
		                      title="SETTING SOCIAL CREDIT")
		embed.set_thumbnail(url=user_display_avatar)

		await ctx.send(embed=embed)

	@commands.command('profile')
	async def profile(self, ctx: commands.Context, user: typing.Optional[discord.User]):
		"""
		Display one's or your own profile.
		"""
		user_id = user.id if user is not None else ctx.author.id
		user_name = user.display_name if user is not None else ctx.author.display_name
		user_display_avatar = user.display_avatar if user is not None else ctx.author.display_avatar

		social_credit = get_social_credit(user_id, ctx.guild.id)

		embed = discord.Embed(colour=discord.Colour.red(),
		                      title=user_name,
		                      description=f"SOCIAL CREDIT: **{social_credit}**")
		embed.set_thumbnail(url=user_display_avatar)
		embed.set_author(name=ctx.guild, icon_url=ctx.guild.icon)

		await ctx.send(embed=embed)


async def setup(client):
	await client.add_cog(China(client))
