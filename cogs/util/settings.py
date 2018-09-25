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
		
			if k not in def_settings:
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
		

	def __call__(self, settingName=None, newData=None):
		"""Processes Setting data, if newData is set, it overwrites (and saves) the new settings"""
		if newData is None and settingName is not None:
			return self._data[settingName]
		elif newData is not None and settingName is not None:
			self._data[settingName] = newData
			self.save()
			return newData
		else:
			return self._data
			
		
				
	def save(self):
		joho = Joho()
		joho.write(self._file_location+"_old_", joho.load(self._file_location))
		joho.write(self._file_location, self._data)
