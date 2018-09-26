from .settings import Settings

class GuildManager:
	def __init__(self):
		self._prefix=";lamu;"
		self.settings = Settings(self,{})
		
		
	def __call__(self, guild_id):
		self.current_guild_id = str(guild_id)
		if str(guild_id) not in self.settings():
			self.settings(guild_id, {"prefix":self._prefix,"co-owners":None})

		return self
		
	def prefix(self, prefix=None):
		if prefix is None:
			return self.settings(str(self.current_guild_id))["prefix"]
		else:
			current_settings = self.settings(self.current_guild_id)
			current_settings["prefix"] = prefix
			self.settings(self.current_guild_id,current_settings)
			return prefix
	