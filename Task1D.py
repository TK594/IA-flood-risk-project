from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river



def run():

    #build a list of stations
    stations = build_station_list()

    #build a list of rivers with at least one station
    rivers = rivers_with_station(stations)

    #sort list of rivers with at least one station alphabetically
    sorted_rivers = sorted(list(rivers))


    print("{} stations have at least one monitoring station".format(len(rivers)))


    print("The first 10 of these stations in alphabetical order are {}".format(sorted_rivers[:10]))

    #build a dictionary that maps rivers to stations on that river
    stations_river = stations_by_river(stations)

    #create an empty array to store stations on the River Aire
    stations_Aire = []

    #add all stattions on the river to an array
    for station in stations_river["River Aire"]:


        stations_Aire.append(station)

    print("Stations on the River Aire ", sorted(stations_Aire))

    #create an empty array to store stations on the River Can
    stations_Cam = []

    #add all stattions on the river to an array
    for station in stations_river["River Cam"]:


        stations_Cam.append(station)

    print("Stations on the River Cam ", sorted(stations_Cam))


    #create an empty array to store stations on the River Thames
    stations_Thames = []

    #add all stattions on the river to an array
    for station in stations_river["River Thames"]:


        stations_Thames.append(station)

    print("Stations on the River Thames ", sorted(stations_Thames))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()





