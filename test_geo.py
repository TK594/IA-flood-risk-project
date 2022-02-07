from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river
from floodsystem.station import *
from floodsystem.stationdata import build_station_list

def test_stations_by_distance():
    station_A = MonitoringStation('ID A', 'Measurement ID A', 'Name A', (0,1), None, 'river 1', 'Town 1')
    station_B = MonitoringStation('ID B', 'Measurement ID B', 'Name B', (1,5), None, 'river 2', 'Town 2')
    station_C = MonitoringStation('ID C', 'Measurement ID C', 'Name C', (3,16), None, 'river 3', 'Town 3')


    list = stations_by_distance((station_C, station_A, station_B), (0,0))

    assert list[0][0] == station_A
    assert list[2][0] == station_C
    assert list[1][0] == station_B



def test_stations_within_radius():
    station_A = MonitoringStation('ID A', 'Measurement ID A', 'Name A', (52.197227,0.087527), None, 'river 1', 'Town 1')
    station_B = MonitoringStation('ID B', 'Measurement ID B', 'Name B', (5,5), None, 'river 2', 'Town 2')
    station_C = MonitoringStation('ID C', 'Measurement ID C', 'Name C', (6,16), None, 'river 3', 'Town 3')


    in_radius = stations_within_radius((station_A, station_B, station_C), (52.2053, 0.1218), 5) 

    assert station_A in in_radius
    assert station_B not in in_radius
    assert station_C not in in_radius


def test_rivers_with_station():
    list = build_station_list()

    assert len(rivers_with_station(list)) == 950


def test_stations_by_river():
    station_A = MonitoringStation('ID A', 'Measurement ID A', 'Name A', (0,1), None, 'river 1', 'Town 1')
    station_B = MonitoringStation('ID B', 'Measurement ID B', 'Name B', (5,5), None, 'river 2', 'Town 2')
    station_C = MonitoringStation('ID C', 'Measurement ID C', 'Name C', (6,16), None, 'river 3', 'Town 3')
    station_D = MonitoringStation('ID D', 'Measurement ID D', 'Name D', (0,1), None, 'river 1', 'Town 1')
    station_E = MonitoringStation('ID E', 'Measurement ID E', 'Name E', (5,5), None, 'river 2', 'Town 2')
    station_F = MonitoringStation('ID F', 'Measurement ID F', 'Name F', (6,16), None, 'river 3', 'Town 3')


    list = stations_by_river((station_A,station_B,station_C,station_D,station_E, station_F))

    assert list['river 1'] == ['Name A', 'Name D']
    assert list['river 2'] == ['Name B', 'Name E']