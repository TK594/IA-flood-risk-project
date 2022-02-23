from .utils import sorted_by_key # noqa
from floodsystem.stationdata import update_water_levels

#2B
def stations_level_over_threshold(stations, tol):
    # Update latest level data for all stations
    update_water_levels(stations)


    stations_over_threshold = []
    latest_levels = []
    #A list of latest relative river level
    for station in stations:    
        if station.latest_level != None and station.relative_water_level() != None:
            if station.relative_water_level() > tol:
                stations_over_threshold.append(station)
                latest_levels.append(station.relative_water_level())

    stations_levels = list(zip(stations_over_threshold,latest_levels))



    return sorted_by_key(stations_levels, 1, reverse= True)
