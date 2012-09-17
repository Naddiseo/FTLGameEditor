#!/usr/bin/python

import sys
import os
import struct
import argparse

class Program(object):
    def main(self):
        self.parse_args()
        self.f = self.args.filename
        self._read_index()
        
    def read_section(self, multiplier=1):
        length = struct.unpack('<L', self.f.read(4))[0]
        length = length*multiplier
        info = struct.unpack('<'+str(length)+'s', self.f.read(length))[0]
        return (length, info)
    
    def _read_index(self):
        self.f.seek(24, 0)
        #header = struct.unpack('<L', self.f.read(24))[0]
        tittle_length, ship_title = self.read_section()
        print ship_title
        ship_info_length,ship_info = self.read_section()
        print ship_info
        a, b = self.read_section(8)
        print b
        a, b = self.read_section()
        print b
        a, b = self.read_section()
        print b
        a, b = self.read_section()
        print b
        crew_size = struct.unpack('<L', self.f.read(4))[0]
        print crew_size
        
        
        
        
    def parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('filename', type=argparse.FileType('rb'), help='File to edit')

        self.args=parser.parse_args()

def main():
    return Program().main()


if __name__ == '__main__':
    sys.exit(main())
