from floodsystem.station import *
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def test_stations_level_over_thershold():

    station_A = MonitoringStation('ID A', 'Measurement ID A', 'Name A', (0,1), (1,10), 'river 1', 'Town 1')
    station_B = MonitoringStation('ID B', 'Measurement ID B', 'Name B', (5,5), (1,3), 'river 2', 'Town 2')
    station_C = MonitoringStation('ID C', 'Measurement ID C', 'Name C', (2,5), (4,7), 'river 3', 'Town 3')
    station_D = MonitoringStation('ID D', 'Measurement ID D', 'Name D', (4,9), (2,8), 'river 4', 'Town 4')
    
    station_A.latest_level = 5.8
    station_B.latest_level = 1.7
    station_C.latest_level = 6
    station_D.latest_level = 6.7

    list = stations_level_over_threshold((station_A, station_B, station_C, station_D), 0.4)
    A, B, C, D = 8/15, 0.35, 2/3, 47/60

    assert list == [(station_D, D), (station_C, C), (station_A, A)]

def test_stations_highest_rel_level():
    station_A = MonitoringStation('ID A', 'Measurement ID A', 'Name A', (0,1), (1,10), 'river 1', 'Town 1')
    station_B = MonitoringStation('ID B', 'Measurement ID B', 'Name B', (5,5), (1,3), 'river 2', 'Town 2')
    station_C = MonitoringStation('ID C', 'Measurement ID C', 'Name C', (2,5), (4,7), 'river 3', 'Town 3')
    station_D = MonitoringStation('ID D', 'Measurement ID D', 'Name D', (4,9), (2,8), 'river 4', 'Town 4')
    
    station_A.latest_level = 5.8
    station_B.latest_level = 1.7
    station_C.latest_level = 6
    station_D.latest_level = 6.7 
    list = stations_highest_rel_level((station_A, station_B, station_C, station_D), 2)
    A, B, C, D = 8/15, 0.35, 2/3, 47/60

    assert list == [(station_D, D), (station_C, C)]