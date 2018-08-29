import re
import json


class Settings:

    def __init__(self, object):
		"""Loads json data to the Settings object, If not found, creates new file."""
		self._file_location = "data/settings/"+object.__name__
		try:
			self._data = self._load()
		except OSError:
			self._data = object.default_settings 
			with open(file_location, "w") as f:
				f.write(self._data)
		
	
	def load(self, guild, data):
		data = self._load(self._file_location)
		return[guild][data]
	
	

    def _load(self,file_location):
        """Returns 'ded' at the moment"""
        if file_location.endswith(".json"):
            with open(file_location) as f:
                return json.load(f)
		