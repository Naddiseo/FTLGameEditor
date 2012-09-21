from Crew import Crew

class Ship(object):
	def __init__(self):
		self.name = ''
		self.ship_model = ''
		
		self.unknown_stat1 = 0 # Total (alive+dead) crew recruited?
		self.unknown_stat2 = 0
		
		self.stats = {}
		
		self.name2 = ''
		self.ship_model2 = ''
		self.ship_model3 = ''
		
		self.crew_size = 0
		self.start_crew = {}
		
		self.health = 0
		self.fuel = 0
		self.drone_parts = 0
		self.missiles = 0
		self.spare_parts = 0
		
		self.current_crew_size = 0
		self.current_crew = {}
		
		self.ship_total_power = 0
		self.active_systems_length = 0
		self.shields_power = 0
		self.shields_damage = 0
		self.shields_downtime = 0
		self.unknown_stat3 = 0
	
	def __str__(self):
		return '''\
	Default Name: {self.name}
	Default Model: {self.ship_model}
	
	Unknown Stat1: {self.unknown_stat1}
	Unknown Stat2: {self.unknown_stat2}
	
	Stats: {self.stats}
	
	Name: {self.name2}
	Model: {self.ship_model2}
	Model2: {self.ship_model3}
	
	Starting Crew Size: {self.crew_size}
	Starting Crew: {self.start_crew}
	
	{self.health}
	{self.fuel}
	{self.drone_parts}
	{self.missiles}
	{self.spare_parts}
	
	{self.current_crew_size}
	{self.current_crew}
	
	{self.ship_total_power}
	{self.active_systems_length}
	{self.shields_power}
	{self.shields_damage}
	{self.shields_downtime}
	{self.unknown_stat3}
		'''.format(self = self)
	
	def read_ship_info(self, save_file):
		self.name = save_file.read_string()
		self.ship_model = save_file.read_string()
		
		self.unknown_stat1 = save_file.read_long()
		self.unknown_stat2 = save_file.read_long()
		
		stats_length = save_file.read_long()
		
		for _ in xrange(stats_length):
			self.stats.update(save_file.read_key_value())
		
		self.ship_model2 = save_file.read_string()
		self.name2 = save_file.read_string()
		self.ship_model3 = save_file.read_string()
		
		self.crew_size = save_file.read_long()
		
		# This might be starting crew
		for _ in xrange(self.crew_size):
			crew_species = save_file.read_string()
			crew_name = save_file.read_string()
			
			self.start_crew[crew_name] = Crew(crew_name, crew_species)
		
		self.health = save_file.read_long()
		self.fuel = save_file.read_long()
		self.drone_parts = save_file.read_long()
		self.missiles = save_file.read_long()
		self.spare_parts = save_file.read_long()
		
		self.current_crew_size = save_file.read_long()
		
		for _ in xrange(self.current_crew_size):
			c = Crew()
			c.read_file(save_file)
			self.current_crew[c.name] = c
		
		self.ship_total_power = save_file.read_long()
		self.active_systems_length = save_file.read_long()
		self.shields_power = save_file.read_long()
		self.shields_damage = save_file.read_long()
		self.shields_downtime = save_file.read_long()
		
		self.unknown_stat3 = save_file.read_long()
