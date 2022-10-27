#a function that finds conjuctions* between two objects 
#*conjunctions are more art than scince 

#i probably have to have a function for each sattalite to get things into the right shape
import numpy as np
import DateTimeTools as TT
from datetime import datetime
#Arase and RBSP both use hours since 1950
def utc_to_datetime(time):
    """
    Convert unix time array to datetime array
    """
    datetime_array = []
    for unix_time in time:
        datetime_array.append(datetime.fromtimestamp(unix_time))
    dt= datetime_array
    return dt 
# Haversine formula example in Python
# Author: Wayne Dyck

import math

def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

def equalize(object_1, object_2, start_time, end_time):
    n=2#the smaller number of moblie
    if len(object_2)==3:#if object_2 is stationary
        object_2=np.repmat(object_2,1,n)
def conjuction_finder(object_1, object_2, start_time, end_time):
    print ("too sooooon")
#objects can either be mobile or staionary (use the second entry for sationary things pleas)  and 
#should be made up of n entries of datetime objects with corrosponing lat and lon vaues  

