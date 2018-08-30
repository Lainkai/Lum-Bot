import json
import os

class Settings:
	"""A file managing class that is pretty trash at the moment. It just handles file writing and data saving."""
	def __init__(self,object, def_settings = {}):
		supplanter = type(object).__name__+".json"
		self._file_location  = "data/settings/"+ supplanter
		self._data = self._load(def_settings , supplanter)
		self.default = False
		def old_detector(def_settings):
			newSettings = False
			for k in list(self._data):
				if k not in def_settings:
					newSettings = True
			if newSettings:
				with open(self._file_location+"_old_","w+") as f:
					json.dump(def_settings,f)
				temp = self._data
				self._data = def_settings
				for k in list(temp):
					if k in self._data:
						self._data[k] = temp[k]
				
		old_detector(def_settings)

	def _load(self,def_settings,supplanter):
		"""Reads file data """
		#Needs to be made better
		os.makedirs(self._file_location.replace(supplanter,""), exist_ok=True)
		try:
			#Tries to load the file if the location exists
			with open(self._file_location) as f:
				return json.load(f)
		except (FileNotFoundError, json.decoder.JSONDecodeError):
			#Creates a default file location
			with open(self._file_location, "w+") as f:
				json.dump(def_settings, f)
				return def_settings

	def get(self,key):
		return self._data[key]

	def store(self,key,data):
		self._data[key] = data
		return data
				
	def save(self):
		with open(self._file_location, "w+") as f:
			json.dump(self._data,f)

