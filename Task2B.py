from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():

    # build list of stations
    stations = build_station_list()
    
    # Update latest level data for all stations
    update_water_levels(stations)

    #printing stations with level over 0.8
    tol = 0.8

    for station in stations:
        if station.typical_range_consistent == True:
            print(len(stations_level_over_threshold(stations, tol)))
            
if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()