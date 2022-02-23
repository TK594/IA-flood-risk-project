import matplotlib.pyplot as plt
import numpy as np



def plot_water_levels(station, dates, levels):
    """for a given station, list of dates and list of levels plot a graph of relative water level against time with typical range shown in dashed lines"""
    plt.plot(dates,levels)

    plt.plot(dates, station.typical_range[0]*np.ones(len(dates)),'--')
    plt.plot(dates, station.typical_range[1]*np.ones(len(dates)), '--' )



    plt.xlabel(dates)
    plt.xticks(rotation = 90)
    plt.ylabel("relative water level")
    plt.title(station.name)

    plt.tight_layout()

    plt.show()

