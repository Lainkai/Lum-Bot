try:
    import discord
    from discord.ext import commands
except ModuleNotFoundError:
    print("Whoops! Installation Failed")
    exit(1)

class Bot(commands.Bot):

    def __init__(self, *args, **kwargs):
        pass

if __name__ == "__main__":
    print("Test")
    input("Stay On Screen")
    exit(0)