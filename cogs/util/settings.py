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
			#print("Detecting Old Settings")
			newSettings = False
			
			for k in self._data:
				#print(k)
				if k not in def_settings:
					#print("Old Settings found")
					newSettings = True
			
			#print("Checking new Settings")
			if newSettings:
			
				with open(self._file_location+"_old_","w",encoding="utf8") as f:
					json.dump(self._data,f,ensure_ascii=False)
					#print("Dumping old Data")
					
				with open(self._file_location+"","w",encoding="utf8") as f:
					json.dump(def_settings,f,ensure_ascii=False)
					#print("Loading New Data")
					
				temp = self._data
				self._data = def_settings
				for k in list(temp):
					if k in self._data:
						self._data[k] = temp[k]
						#print("Loading reloadable data")
						self.save()
						return
						
			#SECTION TWO -- Append any non-existant Setting
			for i in def_settings:
				if i not in self._data:
					self._data[i] = def_settings[i]
					self.save()
				
						
			
				
		old_detector(def_settings)

	def _load(self,def_settings,supplanter):
		"""Reads file data """
		#print("Checking DIRS")
		os.makedirs(self._file_location.replace(supplanter,""), exist_ok=True)
		try:
			#Tries to load the file if the location exists
			with open(self._file_location, encoding="utf8") as f:
				#print("loading data")
				return json.load(f)
		except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
			with open(self._file_location, "w+",encoding="utf8") as f:
				#print("Writing default Data")
				json.dump(def_settings, f, ensure_ascii=False)
				return def_settings

	def get(self,key):
		return self._data[key]

	def store(self,key,data):
		self._data[key] = data
		return data
				
	def save(self):
		with open(self._file_location, "w+", encoding="utf8") as f:
			json.dump(self._data,f,ensure_ascii=False)

