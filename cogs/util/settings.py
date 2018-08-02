from cogs.util.joho import joho
DEFAULT_PATH = "data/Lum/settings.json"

class Settings:
    def __init__(self):
        self.bot_settings = joho.load(joho, DEFAULT_PATH)
        self.default_settings = {
            "TOKEN":"",
            "First-Run":"True"
        }
        self.prefixes = "ラム"

    def save(self):

        joho.save(joho, self.bot_settings, DEFAULT_PATH)
