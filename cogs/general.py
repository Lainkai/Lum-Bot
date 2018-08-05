from discord.ext import commands
import discord
import cogs.util.enforce as enforce

class General:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Pong"""
        print("Ponging")
        await ctx.message.channel.send("Pong")

    @commands.command()
    async def greet(self, ctx, user="", last=""):
        """I will greet you if you just say ;greet However, if you add a name after it, I will greet them, even though every new member gets an automatic greeting!
        """

        if not user == "":
            name = user
            if not last == "" :
                name += " "+last
            print(name)
            try:
                await ctx.message.channel.send("Hi-dacha %s" % ctx.message.guild.get_member_named(name).mention)
            except AttributeError:
                await ctx.message.channel.send("ごめんなさい! Sorry! I don't know anyone by that name!")
        else:
            await ctx.message.channel.send("Hi-dacha %s" % ctx.message.author.mention)
        

def setup(bot):
    n = General(bot)
    print("General Cog Added")
    bot.add_cog(n)
    