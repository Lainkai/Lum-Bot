import json
import os

from .joho import Joho

class Settings:
	"""A file managing class that is pretty trash at the moment. It just handles file writing and data saving."""
	def __init__(self,object, def_settings = {}):
		
		joho = Joho()
		
		supplanter = type(object).__name__+".json"
		dir = "data/settings/"
		self._file_location = dir + supplanter
		
		#Checks if file location is real 
		os.makedirs(dir, exist_ok=True)
		try:
			self._data = joho.load(self._file_location)
		except FileNotFoundError:
			self._data = def_settings
			joho.write(self._file_location, def_settings)
		
		newSettings = False
		
		for k in self._data:
		
			if k not in def_settings and def_settings.__len__() > 0:
				newSettings = True
		
		if newSettings:
			#Saves the old settings for recovery
			joho.write(self._file_location+"_old_", self._data)
				
			#Writes the new Settings
			joho.write(self._file_location, def_settings)	
				
			temp = self._data
			self._data = def_settings
			for k in list(temp):
				if k in self._data:
					self._data[k] = temp[k]
					self.save()
					return
					
		for i in def_settings:
			if i not in self._data:
				self._data[i] = def_settings[i]
				self.save()
		

	def __call__(self, settingName=None, newData=None, remove=False):
		"""Processes Setting data, by iterating over the passed data type, and if newData is set, the selected option will be overwritten."""
		
		if settingName is not None:
			if remove:
				del self._data[settingName]
			else:
				if newData is not None:
					self._data[settingName] = newData
					self.save()
				return self._data[settingName]
		else:
			return self._data

		

		
			
		
				
	def save(self):
		joho = Joho()
		joho.write(self._file_location+"_old_", joho.load(self._file_location))
		joho.write(self._file_location, self._data)
