# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine

from .utils import sorted_by_key # noqa

#1B
def stations_by_distance(stations, p):
    """For a list of MonitoringStation objects, and a coordinate return a list of
    MonitoringStation objects and their distance from the point in order of distance"""
     
    coords = []

    for station in stations:
        coords.append(station.coord)



    distances = []

    for a in coords:
        distances.append(haversine(a,p))


    stations_distances = list(zip(stations,distances))


    return sorted_by_key(stations_distances, 1)
    
#1C
def stations_within_radius(stations, centre, r):
    """For a list of MonitoringStation objects, a coordinate, and a radius, 
    return a list of MonitoringStation objects within a radius"""



    distances = stations_by_distance(stations, centre)

    in_radius = []
    for station, distance in distances:
        if distance < r:
            in_radius.append(station)

    return in_radius

#1D
def rivers_with_station(stations):
    """For a list of MonitoringStation objects, return a set of rivers which have a monitoring station"""
  
  
    rivers = []
  
  
    for station in stations:
        rivers.append(station.river)

    
    return set(rivers)


def stations_by_river(stations):
    """For a list of monitoring station objects, return a dictionary that maps river names
    to stations """

    river_dict = {}

    for station in stations:
        if station.river not in river_dict:
            river_dict[station.river] = station.name

        elif type(river_dict[station.river]) == list:
            river_dict[station.river].append(station.name)

        else:
            river_dict[station.river] = [river_dict[station.river], station.name]

    return river_dict
     