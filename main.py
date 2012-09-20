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
        self.offset += 4
        return (stat, stat_info)
    
    def _read_crew_start_info(self):
        #should eventually return a crew member
        species_length, species = self._read_section()
        name_length, name = self._read_section()
        print "\t"+ name + ": " + species
    
    def _read_crew_current_info(self):
        name_length, name = self._read_section()
        species_length, species = self._read_section()
        unsure_info = self._read_long()
        health = self._read_long()
        X = self._read_long()
        Y = self._read_long()
        Room = self._read_long()
        Room_tile = self._read_long()
        unsure_info2 = self._read_long()
        Piloting = self._read_long()
        Engines = self._read_long()
        Shields = self._read_long()
        Weapons = self._read_long()
        Repair = self._read_long()
        Combat = self._read_long()
        Gender = self._read_long()
        stat_repair = self._read_long()
        stat_combat = self._read_long()
        stat_pilot_eva = self._read_long()
        stat_jumps_survived = self._read_long()
        stat_skill_masteries = self._read_long()
        print "\t" + name
        print "\t\tPiloting:" + str(Piloting)
        print "\t\tEngines:" + str(Engines)
        print "\t\tShields:" + str(Shields)
        print "\t\tWeapons:" + str(Weapons)
        
    def print_offset(self):
        print "offset: " + str(self.offset)
    
    def _read_index(self):
        version = self._read_long()
        difficulty = self._read_long()
        ship_defeated = self._read_long()
        jumps = self._read_long()
        scrap_collected = self._read_long()
        crew_recruited = self._read_long()
        print "version: " + str(version)
        print "difficulty: " + str(difficulty)
        print "jumps: " + str(jumps)
        print "total scrap collected: " + str(scrap_collected)
        print "total crew recuited: " + str(crew_recruited)
        #header = struct.unpack('<L', self.f.read(24))[0]
        tittle_length, ship_title = self._read_section()
        #not sure why these repeat 
        print ship_title
        ship_info_length,ship_info = self._read_section()
        print ship_info
        rando_stat_length = struct.unpack('<L', self.f.read(4))[0]
        rando_stat = struct.unpack('<L', self.f.read(4))[0]
        self.offset += 8
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
            self._read_crew_start_info()
        ship_health = self._read_long()
        print "ship health: " + str(ship_health)
        ship_fuel = self._read_long()
        print "ship health: " + str(ship_fuel)
        ship_drone_parts = self._read_long()
        print "drone parts: " + str(ship_drone_parts)
        ship_missiles = self._read_long()
        print "missiles: " + str(ship_missiles)
        spare_parts = self._read_long()
        print "spare parts: " + str(spare_parts)
        
        
        #current crew info
        current_crew_size = self._read_long()
        for i in xrange(current_crew_size):
            self._read_crew_current_info()
        ship_total_power = self._read_long()
        print "ship total power: " + str(ship_total_power)
        active_systems_length = self._read_long()
        print "possible: systems activated: " + str(active_systems_length)
        shields_power = self._read_long()
        #level is else where.  this is just current power
        print "shields power: " + str(shields_power)
        shields_damage = self._read_long()
        print "shields damage: " + str(shields_damage)
        shields_down_time = self._read_long()
        print "shields down time: " + str(shields_down_time)
        not_sure = self._read_long()
        print "unknown: " + str(not_sure)
        
        self.print_offset()
        
    def parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('filename', type=argparse.FileType('rb'), help='File to edit')

        self.args=parser.parse_args()

def main():
    return Program().main()


if __name__ == '__main__':
    sys.exit(main())
