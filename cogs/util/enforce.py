from discord.ext import commands

class Enforce:
    def owner(self):
        return commands.check(self.is_owner)

    def is_owner(self,ctx):
        _id = ctx.message.author.id
<<<<<<< HEAD:util/enforcer.py
        return _id == "352258945995243525" 
=======
        return _id in ctx.bot.settings.getOwners(ctx.guild.id); #owners
>>>>>>> parent of 8ce06f3... Updated while at school:cogs/util/enforce.py
