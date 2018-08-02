import asyncio
from cogs.util.settings import Settings
try:
    import discord
    from discord.ext import commands
except ImportError:
    print("Error Importing Discord, Try Reinstalling")
    input("Press 'Enter' to continue... ")
    exit(1)

BOT_VERSION = "0.0.0a" #Remember to Change this

class Lum(commands.Bot):
    def __init__(self, *args, **kwargs):
        print("Class Lum: Constructing")
        self.settings = Settings()
        self.version = BOT_VERSION
        self.intro_played = False
        print("Class Lum: Constructed")

    def filter(self, message):
        return False
        

def playIntro():
    import cogs.util.intro as intro
    intro.play(BOT_VERSION)
    
def setup(Settings):
    print("Setting up Settings")

    first_run = Settings.bot_settings == Settings.default_settings

    if first_run:
        #Todo add a token info adder
        pass

def main(bot):
    print("Infiniloop started")
    setup(bot.settings)

    print("Determining if login should do.")
    if Lum.settings.login_cred:
        print("Logging in!")
        yield from Lum.login(*Lum.settings.login_cred)
    #yield from Lum.connect()  --Support for Voice Channels

def initialize(bot_class=Lum):
    print("Initializing Bot!")
    bot = bot_class()
    #insert bot declarations here

    @bot.event
    async def on_ready():
        if not bot.intro_played:
            playIntro()
            bot.intro_played = True

    @bot.event
    async def on_message(message):
        if bot.fliter(message):
            pass
    
    print("Returning initialized lum!")
    return bot


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    print("Gotten Loop")
    #Initialize lum here
    Lamu = initialize()
    try:
        print("Starting infinite loop!")
        loop.run_until_complete(main(Lamu))
    except KeyboardInterrupt:
        #Logout of discord
        loop.run_until_complete(Lamu.logout())
    except discord.LoginFailure:
        print("Login error, would you like to reset?")
        if input("> ").lower().strip() == "reset":
            Lamu.settings.login_cred = None
    except Exception:
        #Logout of Discord
        pass
        loop.run_until_complete(Lamu.logout())

    finally:
        loop.close()
        exit(0)
