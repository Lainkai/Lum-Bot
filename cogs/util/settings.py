from cogs.util.joho import joho
DEFAULT_PATH = "data/Lum/settings.json"

class Settings:
    def __init__(self):
        self.bot_settings = joho.load(joho, DEFAULT_PATH)
        self.default_settings = {
            "version":"0.1.0a",
            "TOKEN":"",
            "First-Run":"True",
            "OWNER":""
        }
        self.prefixes = ";"
        self.token = self.bot_settings['TOKEN']
        self.restart = False
        self.owner = self.bot_settings['OWNER']
        self.version = self.bot_settings['VERSION']
        
    def save(self):

        joho.save(joho, self.bot_settings, DEFAULT_PATH)
