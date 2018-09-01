import asyncio
import logging

import discord
from discord.ext import commands

from cogs.util.settings import Settings

class LumBot(commands.Bot):
    def __init__(self):
        def_settings = {"token":None}
        self.settings = Settings(self, def_settings)		
        def get_prefix(bot, message):
            return message.Guild

        self.restart = False
        self.token = self.settings.get("token")
        super().__init__(get_prefix, pm_help=True)

    async def on_message(self, message):
        await self.process_commands(message)

    async def on_ready(self):
        print("Ready-だちゃ!")


def load_cogs(bot):
    bot.load_extension("cogs.owner")

async def start(bot):
    try:
        await bot.login(bot.token)
    except discord.LoginFailure:
        print("Oops! I think you gave me an invalid token!")
        print("Would you like to reset it?")
    await bot.connect()

def init():
    bot = LumBot()
    load_cogs(bot)
	
	#if bot.

    @bot.command()
    async def ping(ctx):
        """I reply Pong!"""
        await ctx.message.channel.send("Pong!")

    return bot

if __name__ == "__main__":
    #logging.basicConfig(level=logging.INFO)
    bot = init()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(start(bot))
    except KeyboardInterrupt:
        loop.run_until_complete(bot.logout())
    except Exception:
        exit(1)
    finally:
        if bot.restart:
            exit(78)
        else:
            exit(0)