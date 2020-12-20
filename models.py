import math
from datetime import datetime as dt

# Reference https://github.com/maurycyp/vincenty
from vincenty import vincenty

class Satellite():

    def __init__(self, id, lat1, lon1, t1, lat2, lon2, t2):
        pt1 = (lat1, lon1)
        pt2 = (lat2, lon2)
        distance = vincenty(pt1, pt2)
        time = dt.fromisoformat(t2) - dt.fromisoformat(t1)
        self.id = id
        self.slope = (lat2 - lat1) / (lon2 - lon1)
        self.Kmps = distance / time.seconds
        self.Kmph = distance / (time.seconds/3600)
        self.total_orbit_hours = 40007.863 / self.Kmph

    def __str__(self):
        return str.format('ID: {0}, Km/s: {1:0.5f}, Km/h: {2:0.5f}, Total Orbit/hrs: {3:0.5f}, Heading: {4:0.5f}'
        , self.id, self.Kmps, self.Kmph, self.total_orbit_hours, self.slope)

if __name__ == '__main__':
    sat1 = Satellite(
        id='247119100'
        , lat1=52.87994
        , lon1=-176.21738
        , t1='2015-01-01T05:36:17'
        , lat2=52.83234
        , lon2=-176.46662
        , t2='2015-01-01T06:28:57'
    )

    sat2 = Satellite(
        id='311072100'
        , lat1=52.77913
        , lon1=-177.81106
        , t1='2015-01-01T11:09:42'
        , lat2=53.18079
        , lon2=-176.86404
        , t2='2015-01-01T07:42:05'
    )

    print(str(sat1))
    print(str(sat2))