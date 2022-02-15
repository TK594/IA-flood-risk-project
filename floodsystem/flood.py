from .utils import sorted_by_key # noqa
from floodsystem.stationdata import update_water_levels

#2B
def stations_level_over_threshold(stations, tol):
    # Update latest level data for all stations

    #A list of latest relative river level
    latest_relative_water_level = []
    for station in stations:
        if station.typical_range_consistent == True:
            latest_relative_water_level.append(station.relative_water_level)

    stations_over_tol = []
    latest_water_level = []

    for i in range(len(latest_relative_water_level)):
        if latest_relative_water_level[i] > tol:
            stations_over_tol.append(station.name)
            latest_water_level.append(station.relative_water_level())
        
    
    stations_over_threshold = list(zip(stations_over_tol, latest_water_level))

    return sorted_by_key(stations_over_threshold, 1)
