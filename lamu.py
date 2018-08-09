import asyncio
from cogs.util.settings import Settings

try:
    import discord
    from discord.ext import commands
except ImportError:
    print("Error Importing Discord, Try Reinstalling")
    input("Press 'Enter' to continue... ")
    exit(1)

class Lum(commands.Bot):
    
    def __init__(self, *args, **kwargs):

        def prefix_man(bot, message):
            return self.settings.prefixes

        self.settings = Settings(form="bot")
        self.version = self.settings.version
        self.intro_played = False

        desc = "Hi I'm Lum-bot! I am the computer version of the character Lum from the amazing anime, Urusei Yatsura!"

        try:
            super().__init__(*args,command_prefix=prefix_man, pm_help=True,description=desc, **kwargs)
        except Exception as e:
            print(e)

    def filter(self, message):
        """This should work"""
        if not message.author == self.user:
            if not message.author.bot:
                return True
        return False
    
    async def restart(self):
        self.settings.restart = True
        await self.logout()
    
    async def shutdown(self):
        self.settings.restart = False
        await self.logout()
    
def setup(Settings):
    print("Setting up Settings")

    first_run = Settings.bot_settings == Settings.default_settings

    if first_run:
        print("Would you like to use a token for your bot? Y/N")
        if input("> ").strip().lower() == "y":
            print("Please Paste Your Token: ")
            preT = input("> ")
            if "@" not in preT and len(preT) >= 50:
                Settings.token = preT
            else:
                print("I don't think that is a valid Token")

    Settings.save()

async def main(bot):
    setup(bot.settings)

    print("Determining if login should do.")
    if not bot.settings.token == "":
        await bot.login(bot.settings.token)
    else:
        raise RuntimeError
    bot.voice = await bot.connect()

def initialize(bot_class=Lum):

    bot = bot_class()
    #insert bot declarations here

    bot.load_extension("cogs.owner")
    bot.load_extension("cogs.general")

    @bot.event
    async def on_ready():
        print("Alive")

    @bot.event
    async def on_member_join(member):
        await member.guild.text_channels.pop(0).send("Hi-dacha! %s"% member.mention)
        print("Greeted %s for the first time!" % member.name)

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
        print("Login error, Type 'Reset' For reset of token")
        if input("> ").lower().strip() == "reset":
            Lamu.settings.bot_settings = Lamu.settings.default_settings
            Lamu.settings.save()

    except Exception as e:
        #Logout of Discord
        print(e)
        loop.run_until_complete(Lamu.logout())

    finally:
        loop.close()
        if Lamu.settings.restart == True:
            exit(86)

        else:
            exit(0)
