import struct

class SaveFile(object):
	'''
	Interface for the actual reading of the file
	'''
	def __init__(self, fp):
		self.fp = fp
		self.offset = 0
	
	def read_long(self):
		L = struct.unpack('<L', self.fp.read(4))[0]
		self.offset += 4
		return L
	
	def read_string(self, count = 1):
		string_length = self.read_long() * count
		char_string = struct.unpack('<{}s'.format(string_length), self.fp.read(string_length))[0]
		
		self.offset += string_length + 4
		
		return char_string
	
	def read_key_value(self):
		key_string = self.read_string()
		value = self.read_long()
		
		return {key_string : value}
		
