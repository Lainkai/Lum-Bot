import json


#Because I should not make spaghetti code, move all file stuff from settings into here. It should also make settings more better.
class Joho:
	def load(self, loc):
		"""Reads a file in utf-8"""
		with open(loc, encoding="utf8") as f:
			#print("loading data")
			return json.load(f)
			
	def write(self, loc, data):
		"""Writes a new file in utf-8. Takes a location and data"""
		with open(loc, "w+",encoding="utf8") as f:
			#print("Writing default Data")
			json.dump(data, f, ensure_ascii=False)
			return data