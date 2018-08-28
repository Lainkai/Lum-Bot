import re
import json


class Settings:

    def __init__(self, object):
		"""Loads json data to the Settings object, If not found, creates new file."""
		self._file_location = "data/settings/"+object.__name__
		try:
			self._data = self._load()
		except OSError:
			self._data = object._default_settings 
			with open(file_location, "w") as f:
				f.write(self._data)
	
	def load(self, data):
		data = self._load(self._file_location)
		return[data]
	
	def set(self,set_name, data):
		self._data[set_name] = data
		self.save()
		
    def _load(self,file_location):
        """Loads the JSON file for use"""
        if file_location.endswith(".json"):
            with open(file_location) as f:
                return json.load(f)
		
		
	def save(self):
		with open(self._file_location) as f:
			f.write(json.dumps(self._data))