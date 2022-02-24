from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():

    # build list of stations
    stations = build_station_list()
    
    # Update latest level data for all stations
    update_water_levels(stations)

    #creating empty array to store stations with consistent data
    consistent_stations = []

    for station in stations:
        if station.typical_range_consistent:
            consistent_stations.append(station)
    
    #list of 10 stations at which the current relative level is highest
    list_of_10_stations = stations_highest_rel_level(consistent_stations, 10)

    for a, b in list_of_10_stations:
        print(a.name, b)
            
if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()