from cogs.util.joho import joho
DEFAULT_PATH = "data/Lum/settings.json"

class Settings:
    

    def __init__(self, form):
        if form == "bot":
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
            self.form=form
        elif form == "db":
            self.db = joho.load(joho,"data/DB/settings.json")
            self.img = (self.db["TABLES"][0])
            self.cred = (self.db["host"],self.db["USER"],self.db["PASSWD"],self.db["BASE"])
            self.form = form
        else:
            raise Exception
        
    def save(self):
        spath = ""
        if self.form == "bot":
            spath = DEFAULT_PATH
        elif self.form == "db":
            spath = "data/DB/settings.json" 

        joho.save(joho, self.bot_settings, spath)
