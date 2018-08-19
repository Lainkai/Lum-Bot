from discord.ext import commands

class Enforce:
    def owner(self):
        return commands.check(self.is_owner)

    def is_owner(self,ctx):
        _id = ctx.message.author.id
        return _id in ctx.bot.settings.getOwners(ctx.guild.id); #owners
