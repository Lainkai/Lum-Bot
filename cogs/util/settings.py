import json

class Settings:
"""A file managing class that is pretty trash at the moment. It just handles file writing and data saving."""
	def __init__(self,object, def_settings = {}):
		self._file_location  = "data/settings/"+type(object).__name__+".json"
		self._default_settings = def_settings
		self._data = self._load()
		if self._
		print(self._file_location)

	def _load(self):
		"""Reads file data """
		try:
			with open(file_location) as f:
			return json.load(f)
		except OSError:
			with open(file_location, "w+") as f:
				f.write(json.dump(self._default_settings
	def get(key):
		return self._data[key]
				
	def save(self):
		pass
		
class Lamu:
	def __init__:
		print("oofed")
		
l = Lamu()
s = Settings(l)
