import asyncio
import logging

import discord
from discord.ext import commands

from util.settings import Settings

#REMEMBER! THIS BOT IS ONLY FOR SMALL SERVER NETWORKS, NOT LARGE SCALE INVITING.
class LumBot(commands.Bot):
    def __init__(self):
		self._default_settings = {"token":None}
        self._settings = Settings(LumBot.__class__)
        self.restart = False
		self._data
		
		def get_prefix(bot, message):
			pass
			#fill void with something that retrieves prefix for server, incase they use their bot account for multiple servers.
		
        super().__init__(get_prefix, pm_help=True)

    async def on_message(self, message):
        await self.process_commands(message)

    async def on_ready(self):
        print("Ready-だちゃ!")

	def getSetting(set_name):
		return self._settings.load(set_name)
		
	def setSetting(set_name, data):
		self._settings.set(set_name, data)
		return data

def load_cogs(bot):
    bot.load_extension("core.owner")

async def start(bot):
	try:
		await bot.login(bot.getSetting(["token"]))
	except discord.LoginFailure:
		print("Oops! I think gave me an invalid token!")
		print("Would you like me to reset it?")
		if input("> ").strip().lower() == "y":
			bot.setSetting("token", None)
		
	await bot.connect()
		

def init():
    bot = LumBot()
    load_cogs(bot)
	
	if 

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
		exit(1)
    except Exception:
        exit(1)
    finally:
        if bot.restart:
            exit(78)
        else:
            exit(0)
			