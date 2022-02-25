from floodsystem.analysis import polyfit
from datetime import datetime
import matplotlib.dates
import numpy as np

def test_polyfit():
    t = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1),
     datetime(2017, 1, 2), datetime(2017, 1, 3), datetime(2017, 1, 4),
     datetime(2017, 1, 5)]

    levels = [1,4,9,16,25,36,49]

    poly, d0 = polyfit(t,levels, 2)

    assert d0 == matplotlib.dates.date2num(datetime(2016,12,30))