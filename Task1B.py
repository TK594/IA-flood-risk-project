from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    #build list of stations

    stations = build_station_list()
    
    #calculate distance of each station from the city centre
    distances = stations_by_distance(stations, (52.2053, 0.1218))


    #create empty array to store list of tuples
    result = []

    #Create final list
    for station, distance in distances:
        result.append(( station.name, station.town, distance))


    #print 10 closest stations
    print(result[:10])

    #print 10 furthest stations
    print(result[-10:])


    
if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()