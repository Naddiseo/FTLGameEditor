from FTLLib.Ship import Ship

class Game(object):
	
	def __init__(self):
		self.version = 0
		self.difficulty = 0
		self.ships_defeated = 0
		self.jumps = 0
		self.scrap_collected = 0
		self.crew_recuited = 0
		self.ship = Ship()
	
	def __str__(self):
		return '''\
Save Game
Version: {self.version}
Difficulty: {self.difficulty}
Ships Defeated: {self.ships_defeated}
Jumps: {self.jumps}
Scrap Collected: {self.scrap_collected}
Crew Recruited: {self.crew_recuited}
SHIP
{self.ship}
'''.format(self = self)
	
	def read_file(self, save_file):
		self.version = save_file.read_long()
		self.difficulty = save_file.read_long()
		self.ships_defeated = save_file.read_long()
		self.jumps = save_file.read_long()
		self.scrap_collected = save_file.read_long()
		self.crew_recuited = save_file.read_long()
		
		self.ship.read_ship_info(save_file)
