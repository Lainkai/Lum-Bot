from .settings import Settings

class GuildManager:
	def __init__(self):
		self._guildId = 0
		self._prefix=";lamu;"
		self.settings = Settings(self,{})
		
		
	def __call__(self, guild_id):
		self._guildId = guild_id
		if self._guildId not in self.settings():
			self.settings(self._guildId, {"prefix":";lamu;","co-owners":None})
		
		return self
		
	def prefix(self, prefix=None):
		if prefix is None:
			return self.prefix
		else:
			self._prefix = prefix
			self.settings("prefix", prefix)
			return prefix
	