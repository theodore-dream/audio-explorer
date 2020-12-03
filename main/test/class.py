#!/usr/bin/python3

class Tune:
  
    def __init__(self, name):
        self.name = name
        self.station = []

    def add_station(self, station):
        self.station.append(station)

e = Tune('BonIver')
e.add_station('skinny_love')
print(e.station)   
