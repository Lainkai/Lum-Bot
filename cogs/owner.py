import discord
from discord.ext import commands

import cogs.util.checks as checks
from cogs.util.settings import Settings

class Owner:	

	def __init__(self, bot):
		self.bot = bot
		
	@commands.command()
	@checks.owner()
	async def restart(self,ctx):
		"""Restarts Lum-Bot For Updates"""
		self.bot.restarting = True
		await self.bot.logout()
	
	@commands.command()
	@checks.owner()
	async def shutdown(self, ctx):
		"""Shuts Down Lum-Bot"""
		await ctx.message.channel.send("Bye! :wave: ")
		await self.bot.logout()
		
	@commands.command()
	@checks.owner()
	async def set_prefix(self,ctx,arg):
		"""Sets my prefix for the guild"""
		print(arg)
		self.bot.guildManager(ctx.guild.id).prefix(arg)
		await ctx.message.channel.send("The prefix is now set to %s !" % self.bot.guildManager(ctx.guild.id).prefix())
		

"""
	@commands.command()
	@enforce.owner()
	async def tag_check(self, ctx):
		async with ctx.message.channel.typing():
			print("Checking Tags")
			joho.sql(joho, creds=self.settings.cred)
			self.imgs = joho.select(joho, "*", "images")
			self.im_len = len(self.imgs)
			for i in self.imgs:
				print("%s | %s | %s" % (i[0], i[1], i[2]))

		await ctx.message.channel.send("Ready!")
	

	@commands.command()
	@enforce.owner()
	async def tag(self, ctx, **kwargs):
		self.current_img = self.imgs.pop(0)
		embed = discord.Embed(title="Gif "+str(self.im_len-len(self.imgs)))
		embed.set_image(url=self.current_img[0])
		embed.add_field(name ="Tags:",value =self.current_img[1])
		embed.add_field(name ="ID", value =self.current_img[2])
		await ctx.message.channel.send(embed=embed)
"""

def setup(bot):
	o = Owner(bot)
	bot.add_cog(o)
	