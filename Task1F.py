from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():

    # build list of stations
    stations = build_station_list()

    # Sort the list of inconsistent stations alphabetically
    sorted_station = sorted(inconsistent_typical_range_stations(stations))

    print(sorted_station)




if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()