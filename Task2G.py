import numpy as np
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
import datetime
from floodsystem.analysis import polyfit
import matplotlib.dates


def run():
    

    #build list of stations     
    stations = build_station_list()
    #get relative levels of stations above a low tolerance
    update_water_levels(stations)
    relative_levels = stations_level_over_threshold(stations, 0.6)



    low = [] #stations with a relative level of 0.6 or higher with a decreasing or constant relative level
    moderate = [] #stations with a relative level of 0.8 or larger that have an increasing relative level
    high = [] #stations with a relative level between 1 and 1.5
    severe = [] #stations with a relative level above 1.5

    for station, level in relative_levels:

        
        if level>1.5:
            severe.append(station.name)

        elif level>1:
            high.append(station.name)
            dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days =2))
            try:
                x = matplotlib.dates.date2num(dates)     
                poly, d0 = polyfit(dates, levels, 4)
                dydx = poly.deriv()
            except:
                continue

        
        
        elif dydx(x[-1]-d0) > 0 and level >0.8:
            moderate.append(station.name)

        else:
            low.append(station.name)

        
    print("Severe risk stations are ", severe)
    print("High risk stations are: ", high)
    print("Moderate risk stations are: ", moderate)
    print("Low risk stations are:", low )



if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()



