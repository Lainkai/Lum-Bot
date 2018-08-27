import json

class Settings:
    def __init__(self, file_location):
        self._data = self._load("settings/"+file_location)
		

    def _load(self,file_location):
        """Returns 'ded' at the moment"""
        if file_location.endswith(".json"):
            with open(file_location) as f:
                return json.load(f)
				
	def get(data):
		self._data[data]
		