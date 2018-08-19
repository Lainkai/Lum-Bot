import asyncio
import logging

import discord
from discord.ext import commands

from cogs.util.settings import Settings

class LumBot(commands.Bot):
    def __init__(self):
        self.settings = Settings()
        self.restart = False
        super().__init__(";", pm_help=True)

    async def on_message(self, message):
        await self.process_commands(message)

    async def on_ready(self):
        print("ready")
        await self.change_presence(status=discord.Status.online)


def load_cogs(bot):
    bot.load_extension("cogs.owner")

async def start(bot):
    try:
        await bot.login(bot.settings.token)
    except Exception:
        #Add A smarter thing that tells you that you didn't provide a good token
    await bot.connect()

def init():
    bot = LumBot()
    load_cogs(bot)

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