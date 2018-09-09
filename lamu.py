import asyncio
import logging

import discord
from discord.ext import commands

from cogs.util.settings import Settings

class LumBot(commands.Bot):
	def __init__(self):
		self.awaiting_response = False
		#add a guild settings manager
		def_settings = {"token":None,"guilds":{},"bot-interactive":False}
		self.settings = Settings(self, def_settings)		
		def get_prefix(bot, message):
		
			try:
				return self.getGuildSettings(message)["prefix"]
			except KeyError:
				return ";lamu; "

		self.restarting = False
		
		super().__init__(get_prefix, pm_help=True)

	async def on_message(self, message):
		if not self.settings("bot-interactive"):
			if not message.author.bot:
				print("Verified not a bot!")
				await self.process_commands(message)	
		else:
			await self.process_commands(message)

	async def on_ready(self):
		print("Ready-だちゃ!")
		
	def getGuildSettings(self, message):
		return self.settings("guilds")[message.guild.id]
		
	def token(self, token=None):
		if token is None:
			return self.settings("token")
		
		if len(token)>=50:
			self.settings("token", token)
			return True
		else:
			#cls
			print("I don't think that is a valid token. Please try again.")
			return False

def load_cogs(bot):
	bot.load_extension("cogs.owner")

async def start(bot):
	try:
		await bot.login(bot.token())
	except discord.LoginFailure:
		print("Oops! I think you gave me an invalid token!")
		print("Would you like to reset it?")
	await bot.connect()

def init():
	bot = LumBot()
	load_cogs(bot)
	
	if bot.token() is None:
		valid = False
		while not valid:
			print("Can I have my token please?")
			token = input(": ")
			print(bot.token(token))
			valid = bot.token(token)

	@bot.command()
	async def ping(ctx):
		"""I reply Pong!"""
		await ctx.message.channel.send("Pong!")

	return bot

if __name__ == "__main__":
	#logging.basicConfig(level=logging.INFO)
	bot = init()
	loop = asyncio.get_event_loop()
	try:
		loop.run_until_complete(start(bot))
	except KeyboardInterrupt:
		loop.run_until_complete(bot.logout())
	except Exception:
		exit(1)
	finally:
		if bot.restarting:
			exit(81)
		else:
			exit(0)