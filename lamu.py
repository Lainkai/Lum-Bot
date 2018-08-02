import asyncio
from cogs.util.settings import Settings
try:
    import discord
    from discord.ext import commands
except ImportError:
    print("Error Importing Discord, Try Reinstalling")
    input("Press 'Enter' to continue... ")
    exit(1)

BOT_VERSION = "0.0.0b" #Remember to Change this

class Lum(commands.Bot):
    
    def __init__(self, *args, **kwargs):

        def prefix_man(bot, message):
            return self.settings.prefixes

        self.settings = Settings()
        self.version = BOT_VERSION
        self.intro_played = False
        try:
            super().__init__(*args,command_prefix=prefix_man, **kwargs)
        except Exception as e:
            print(e)

    def filter(self, message):
        """This should work"""
        return False
        

def playIntro():
    import cogs.util.intro as intro
    intro.play(BOT_VERSION)
    
def setup(Settings):
    print("Setting up Settings")

    first_run = Settings.bot_settings == Settings.default_settings

    if first_run:
        print("Would you like to use a token for your bot? Y/N")
        if input("> ").strip().lower() == "y":
            print("Please Paste Your Token: ")
            preT = input("> ")
            if "@" not in preT and len(preT) >= 50:
                Settings.bot_settings["TOKEN"] = preT
            else:
                print("I don't think that is a valid Token")

    Settings.save()

def main(bot):
    setup(bot.settings)

    print("Determining if login should do.")
    if not bot.settings.bot_settings["TOKEN"] == "":
        yield from bot.login(bot.settings.bot_settings["TOKEN"])

    yield from bot.connect()  #--Support for Voice Channels

def initialize(bot_class=Lum):

    bot = bot_class()
    #insert bot declarations here

    @bot.event
    async def on_ready():
        if not bot.intro_played:
            playIntro()
            bot.intro_played = True

    @bot.event
    async def on_message(message):
        if bot.filter(message):
            print("wah")
    
    return bot


if __name__ == "__main__":
    print("Running "+discord.__version__)
    loop = asyncio.get_event_loop()
    #Initialize lum here
    Lamu = initialize()
    try:
        loop.run_until_complete(main(Lamu))
    except KeyboardInterrupt:
        #Logout of discord
        print("Keyboard Interrupt Acknowledged")
        loop.run_until_complete(Lamu.logout())
    except discord.LoginFailure:
        print("Login error, would you like to reset?")
        if input("> ").lower().strip() == "reset":
            Lamu.settings.login_cred = None
    except Exception as e:
        #Logout of Discord
        print(e)
        loop.run_until_complete(Lamu.logout())

    finally:
        loop.close()
        exit(0)
