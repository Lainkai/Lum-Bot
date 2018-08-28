import json

class Settings:
    def __init__(self):
        self._custom = self.load("data/Lamu.json")
        self.token = self._custom["token"]

    def getOwners(self,guild_id):
        pass

    def load(self,file_location):
        """Returns 'ded' at the moment"""
        if file_location.endswith(".json"):
            with open(file_location) as f:
                return json.load(f)                        