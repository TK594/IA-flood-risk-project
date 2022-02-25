# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    station_A = MonitoringStation('ID A', 'Measurement ID A', 'Name A', (0,1), None, 'river 1', 'Town 1')
    station_B = MonitoringStation('ID B', 'Measurement ID B', 'Name B', (5,5), (1,3), 'river 2', 'Town 2')
    station_C = MonitoringStation('ID C', 'Measurement ID C', 'Name C', (6,3), (5,4), 'river 2', 'Town 3')


    assert station_A.typical_range_consistent() == False
    assert station_B.typical_range_consistent() == True
    assert station_C.typical_range_consistent() == False

def test_inconsistent_typical_range_consistent():
    station_A = MonitoringStation('ID A', 'Measurement ID A', 'Name A', (0,1), None, 'river 1', 'Town 1')
    station_B = MonitoringStation('ID B', 'Measurement ID B', 'Name B', (5,5), (1,3), 'river 2', 'Town 2')
    station_C = MonitoringStation('ID C', 'Measurement ID C', 'Name C', (6,3), (5,4), 'river 2', 'Town 3')

    assert inconsistent_typical_range_stations((station_A, station_B, station_C)) == ['Name A', 'Name C']

def test_relative_water_level():
    station_A = MonitoringStation('ID A', 'Measurement ID A', 'Name A', (0,1), None, 'river 1', 'Town 1')
    station_B = MonitoringStation('ID B', 'Measurement ID B', 'Name B', (5,5), (1,3), 'river 2', 'Town 2')
    station_C = MonitoringStation('ID C', 'Measurement ID C', 'Name C', (6,3), (5,4), 'river 2', 'Town 3')
    station_A.latest_level = 0.5
    station_B.latest_level = 2.4
    station_C.latest_level = 4.5

    assert station_A.relative_water_level() == None
    assert station_B.relative_water_level() == 0.7
    assert station_C.relative_water_level() == None
