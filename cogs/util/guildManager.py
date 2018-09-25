from .settings import Settings

class GuildManager:
	def __init__(self):
		#self._guildId = 0
		self._prefix=";lamu;"
		self.settings = Settings(self,{})
		
		
	def __call__(self, guild_id):
		if guild_id not in self.settings():
			self.settings(guild_id, {"prefix":self._prefix,"co-owners":None})
		
		return self
		
	def prefix(self, prefix=None):
		if prefix is None:
			return self.prefix
		else:
			self._prefix = prefix
			self.settings("prefix", prefix)
			return prefix
	