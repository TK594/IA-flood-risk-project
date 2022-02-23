from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
import datetime

def run():
    #build list of stations     
    stations = build_station_list()
    #get relative levels of stations above a low tolerance
    relative_levels = stations_level_over_threshold(stations, 0)
    #find 5 stations with the highest relative level
    first_5 = relative_levels[:5]

    #get data for each of the 5 stations over the past 10 days and plot
    for station, relative_level in first_5:

        dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days = 10))

        plot_water_levels(station, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()

