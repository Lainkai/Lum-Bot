import discord
from discord.ext import commands

import cogs.util.enforce as enforce

class Owner:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @enforce.owner()
    async def restart(self, ctx):
        """Restarts Lum-Bot For Updates"""
        await self.bot.restart()
    
    @commands.command()
    @enforce.owner()
    async def shutdown(self, ctx):
        """Shuts Down Lum-Bot"""
        await self.bot.shutdown()

def setup(bot):
    o = Owner(bot)
    bot.add_cog(o)
    