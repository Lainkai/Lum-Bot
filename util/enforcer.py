from discord.ext import commands

class Enforcer:
    def owner(self):
        return commands.check(self.is_owner)

    def is_owner(self,ctx):
        _id = ctx.message.author.id
        return _id in ctx.bot.settings. #owners