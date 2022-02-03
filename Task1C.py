from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():
    #Build a list of stations
    stations = build_station_list()

    #generate a list of all stations within 10km of city centre
    in_radius = stations_within_radius(stations,  (52.2053, 0.1218), 10)


    #create empty array to store result
    result = []


    #add the names of all stations in the radius to an array
    for station in in_radius:
        result.append(station.name)

    #return a list of stations in radius in alphabetical order
    print(sorted(result))


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()


    
