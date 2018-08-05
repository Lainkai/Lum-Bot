from discord.ext import commands

def owner():
    return commands.check(is_owner)

def is_owner(ctx):
    _id = ctx.message.author.id
    return _id == ctx.message.guild.get_member_named(ctx.bot.settings.owner).id #or _id in ctx.bot.settings.co_owners

    