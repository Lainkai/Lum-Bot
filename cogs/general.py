from discord.ext import commands
import discord
import cogs.util.enforce as enforce
from cogs.util.settings import Settings
from cogs.util.joho import joho
from random import shuffle

class General:
    """Just some  pretty genereal things I do!"""

    def __init__(self, bot):
        self.bot = bot
        self.settings = Settings(form="db")
        joho.sql(joho, creds=self.settings.cred)

    def greeter(self, name):
        return "Hi-dacha %s" % name.mention

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
                await ctx.message.channel.send(self.greeter(ctx.message.guild.get_member_named(name)))
            except AttributeError:
                await ctx.message.channel.send("ごめんなさい! Sorry! I don't know anyone by that name!")
        else:
            await ctx.message.channel.send(self.greeter(ctx.message.author))

    @commands.command()
    async def gif(self, ctx):
        """A place holder for the gif serving command"""
        imgs = joho.select(joho, "*", "images", "tags LIKE \"%'gif'%\"")
        shuffle(imgs)
        embed= discord.Embed(title="どうぞ！")
        embed.set_image(url=imgs.pop()[0])
        await ctx.channel.send(embed = embed)
        

def setup(bot):
    n = General(bot)
    print("General Cog Added")
    bot.add_cog(n)
    