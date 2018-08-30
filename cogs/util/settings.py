import json
import os

class Settings:
	"""A file managing class that is pretty trash at the moment. It just handles file writing and data saving."""
	def __init__(self,object, def_settings = {}):
		self._file_location  = "data/settings/"+type(object).__name__+".json"
		self._default_settings = def_settings
		self._data = self._load()
		self.default = False
		for k in list(self._data):
			if k not in self._default_settings:
				self._data = self._default_settings
				self.default = True
				break

	def _load(self):
		"""Reads file data """
		os.makedirs(os.path.dirname(self._file_location), exist_ok=True)
		try:
			with open(self._file_location) as f:
				return json.load(f)
		except OSError:
			with open(self._file_location, "w+") as f:
				json.dump(self._default_settings, f)

	def get(self,key):
		return self._data[key]

	def store(self,key,data):
		self._data[key] = data
		return data
				
	def save(self):
		with open(self._file_location, "w+") as f:
			json.dump(self._data,f)
