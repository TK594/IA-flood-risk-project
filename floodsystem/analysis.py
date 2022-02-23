import numpy as np
import matplotlib.dates


#2F

def polyfit(dates,levels,p):

    """for a list of dates, levels and an order, return a tuple of the least squares polynomial fit
    of specified order and the shift of date axis"""

    x = matplotlib.dates.date2num(dates)

    p_coeff = np.polyfit(x-x[0], levels, p)

    poly = np.poly1d(p_coeff)

    poly_shift = (poly,x[0])

    return poly_shift
