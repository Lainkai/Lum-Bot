from discord.ext import commands

class Enforce:#Add some doodad that does a thing so that I can automatically update the owners
		def __init__(bot):
			self.bot = both
		def owner(self):
				#Something that calls a callable so that it calls for a fresco list of a guilds owners
				return commands.check(self.is_owner)

		def is_owner(self,ctx):
				_id = ctx.message.author.id
				if len(self.settings["guilds"]) > 1:
					return _id == ctx.bot.owner.id
				else:
					try:
						#Temporary Solution
						owner = ctx.guild.owner
						return owner == _id
					except AttributeError:
						return ctx.bot.owner.id == _id
				
				
				
