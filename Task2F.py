from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
import datetime



def run():

    #build list of stations     
    stations = build_station_list()
    update_water_levels(stations)
    #get relative levels of stations above a low tolerance
    relative_levels = stations_level_over_threshold(stations, 0)
    #find 5 stations with the highest relative level
    first_5 = relative_levels[:5]


    #get data for 5 stations over past 2 days and plot both actual and best fit values
    for station, relative_level in first_5:

        dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days = 2))

        plot_water_level_with_fit(station, dates, levels, 4)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
