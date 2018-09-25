from discord.ext import commands

import cogs.util.joho as joho

async def is_owner(ctx):
		_id = ctx.message.author.id
		if len(_readSettings("GuildManager")) > 1:
			print("multiserver bot owner checked")
			return _id == ctx.bot.owner_id
		else:
			print("single server bot owner checked")
			try:
				#Temporary Solution
				owner = ctx.guild.owner_id
				return owner == _id
			except AttributeError:
				return ctx.bot.owner_id == _id

def owner():
	#Something that calls a callable so that it calls for a fresco list of a guilds owners
	return commands.check(is_owner)

def _readSettings(objectString):
	reader = joho.Joho()
	return reader.load("data/settings/"+objectString+".json")