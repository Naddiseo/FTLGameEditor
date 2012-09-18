#!/usr/bin/python

import sys
import os
import struct
import argparse

class Program(object):
    def __init__(self):
        self.offset = 0
        
    def main(self):
        self.parse_args()
        self.f = self.args.filename
        self._read_index()
        
    def _read_section(self, multiplier=1):
        length = struct.unpack('<L', self.f.read(4))[0]
        length = length*multiplier
        info = struct.unpack('<'+str(length)+'s', self.f.read(length))[0]
        self.offset += length+4
        return (length, info)
    
    def _read_long(self):
        L = struct.unpack('<L', self.f.read(4))[0]
        self.offset += 4
        return L
    def _read_stat(self):
        stat_length, stat = self._read_section()
        #stat_info_length = struct.unpack('<L', self.f.read(4))[0]
        stat_info = struct.unpack('<L', self.f.read(4))[0]
        return (stat, stat_info)
    
    def _read_crew_basic_info(self):
        #should eventually return a crew member
        species_length, species = self._read_section()
        name_length, name = self._read_section()
        print name + ": " + species
        
    
    def _read_index(self):
        self.f.seek(24, 0)
        self.offset += 24
        #header = struct.unpack('<L', self.f.read(24))[0]
        tittle_length, ship_title = self._read_section()
        #not sure why these repeat 
        print ship_title
        ship_info_length,ship_info = self._read_section()
        print ship_info
        rando_stat_length = struct.unpack('<L', self.f.read(4))[0]
        rando_stat = struct.unpack('<L', self.f.read(4))[0]
        stats_size = self._read_long()
        #print stats_size
        for i in xrange(stats_size):
            stat, stat_info = self._read_stat()
            print "\t"+stat + ": " +str(stat_info)
        tittle_length2, ship_title2 = self._read_section()
        #not sure why these repeat 
        print ship_title2
        ship_info_length2 ,ship_info2 = self._read_section()
        print ship_info2
        lowercase_shipname = self._read_section()
        #now the data makes sense
        crew_size = self._read_long()
        print "Crew size: " + str(crew_size)
        for i in xrange(crew_size):
            self._read_crew_basic_info()
        
        
    def parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('filename', type=argparse.FileType('rb'), help='File to edit')

        self.args=parser.parse_args()

def main():
    return Program().main()


if __name__ == '__main__':
    sys.exit(main())
