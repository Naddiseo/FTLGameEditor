

class Crew(object):
	def __init__(self, name = '', species = ''):
		self.name = name
		self.species = species
		
		self.unknown_attr1 = 0
		self.health = 0
		self.x = 0
		self.y = 0
		self.room = 0
		self.room_tile = 0
		self.unknown_attr2 = 0
		
		self.skills = {
			'piloting' : 0,
			'engines' : 0,
			'shields' : 0,
			'weapons' : 0,
			'repair' : 0,
			'combat' : 0,
		}
		
		self.gender = 0
		
		self.stat_repair = 0
		self.stat_combat = 0
		self.stat_pilot_eva = 0
		self.stat_jumps_survived = 0
		self.stat_skill_masteries = 0
	
	def __str__(self):
		return '''
		----------------------------------
		{self.name} ({self.species})
		
		Unknown Attribute1: {self.unknown_attr1}
		Health: {self.health}
		Coords: {self.x}, {self.y}
		Room: {self.room} Tile:	{self.room_tile}
		Unknown Attribute2: {self.unknown_attr2}
		
		Skills = {{
			piloting : {self.skills[piloting]},
			engines : {self.skills[engines]},
			shields : {self.skills[shields]},
			weapons : {self.skills[weapons]},
			repair : {self.skills[repair]},
			combat : {self.skills[combat]},
		}}
		
		Gender: {self.gender}
		
		Stat Repair: {self.stat_repair}
		Stat Combat: {self.stat_combat}
		Stat Pilot: {self.stat_pilot_eva}
		Stat Jumps Survived: {self.stat_jumps_survived}
		Stat Skill Masteries: {self.stat_skill_masteries}
		----------------------------------------'''.format(self = self)
	
	def read_file(self, save_file):
		self.name = save_file.read_string()
		self.species = save_file.read_string()
		#assert self.name == name, '{} != {}'.format(self.name, name)
		#assert self.species == species, '{} != {}'.format(self.species, species)
		
		self.unknown_attr1 = save_file.read_long()
		self.health = save_file.read_long()
		self.x = save_file.read_long()
		self.y = save_file.read_long()
		self.room = save_file.read_long()
		self.room_tile = save_file.read_long()
		self.unknown_attr2 = save_file.read_long()
		self.skills['piloting'] = save_file.read_long()
		self.skills['engines'] = save_file.read_long()
		self.skills['shields'] = save_file.read_long()
		self.skills['weapons'] = save_file.read_long()
		self.skills['repair'] = save_file.read_long()
		self.skills['combat'] = save_file.read_long()
		
		self.gender = save_file.read_long()
		self.stat_repair = save_file.read_long()
		self.stat_combat = save_file.read_long()
		self.stat_pilot_eva = save_file.read_long()
		self.stat_jumps_survived = save_file.read_long()
		self.stat_skill_masteries = save_file.read_long()
		
		
