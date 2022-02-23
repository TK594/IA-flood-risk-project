import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from .analysis import polyfit

#2E
def plot_water_levels(station, dates, levels):
    """for a given station, list of dates and list of levels plot a graph of relative water level against time with typical range shown in dashed lines"""
    plt.plot(dates,levels)

    plt.plot(dates, station.typical_range[0]*np.ones(len(dates)),'--')
    plt.plot(dates, station.typical_range[1]*np.ones(len(dates)),'--')



    plt.xlabel(dates)
    plt.xticks(rotation = 90)
    plt.ylabel("relative water level")
    plt.title(station.name)

    plt.tight_layout()

    plt.show()


#2F

def plot_water_level_with_fit(station,dates,levels,p):
    """for a given station, list of dates, list of levels and order of polynomial plot a graph of 
    relative water level against time with typcal range shown in dashed lines. also plot best fit polynomial on the same axes"""
    plt.plot(dates,levels, label = 'from data')

    plt.plot(dates, station.typical_range[0]*np.ones(len(dates)),'--')
    plt.plot(dates, station.typical_range[1]*np.ones(len(dates)),'--')

    poly, d0 = polyfit(dates,levels,p)

    x = matplotlib.dates.date2num(dates)

    plt.plot(dates,poly(x-x[0]), label = 'best fit polynomial')


    plt.xlabel(dates)
    plt.xticks(rotation = 90)
    plt.ylabel("relative water level")
    plt.title(station.name)
    plt.legend()
    plt.tight_layout()

    plt.show()

