from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    #build list of stations
    stations = build_station_list()

    #build list of river with the number of stations
    river_with_number = rivers_by_station_number(stations, 9)

    #print the result
    print(river_with_number)

       
if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run() 


