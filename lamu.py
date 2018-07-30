try:
    import discord
    from discord.ext import commands
except ImportError:
    print("Whoops! Discord.py not installed! -I")
    input("...")
    exit(1)

class Lum(commands.Bot):

    def __init__(self, *args, **kwargs):
	
        super.__init__(*args, **kwargs)
		
		#Quick mental note the prefix thingy does not prevent the on message event!

def main(bot):
	
	yield from bot.login(token)
		
if __name__ == "__main__":
    print("Test")
    input("Stay On Screen")
	lamu = Lum()
	
	
    exit(0)