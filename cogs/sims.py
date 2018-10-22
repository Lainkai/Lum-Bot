import discord
from discord.ext import commands

class Sims:
    def __init__(self, bot):
        self.bot = bot

    def angryResponse(self):
        pass

def setup(bot):
    s = Sims(bot)
    bot.add_cog(s)
