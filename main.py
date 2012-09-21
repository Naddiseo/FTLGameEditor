#!/usr/bin/python

import sys
import argparse

from FTLLib.SaveFile import SaveFile
from FTLLib.Game import Game

class Program(object):
	def __init__(self):
		self.offset = 0
		
	def main(self):
		self.parse_args()
		self.save = SaveFile(self.args.filename)
		#self._read_index()
		self.game = Game()
		self.game.read_file(self.save)
		print str(self.game)
		
	def parse_args(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('filename', type = argparse.FileType('rb'), help = 'File to edit')

		self.args = parser.parse_args()

def main():
	return Program().main()


if __name__ == '__main__':
	sys.exit(main())
