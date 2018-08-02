from cogs.util.joho import joho
DEFAULT_PATH = "data/Lum/settings.json"

class Settings:
    def __init__(self):
        self.login_cred = None
        self.default_settings = None
        self.bot_settings = joho.load(joho, DEFAULT_PATH)
        self.default_settings = {
            "TOKEN":"",
            "First-Run":"True"
        }
        print(self.bot_settings)