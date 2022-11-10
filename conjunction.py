#a function that finds conjuctions* between two objects 
#*conjunctions are more art than scince 

#i probably have to have a function for each sattalite to get things into the right shape
import numpy as np
import DateTimeTools as TT
from datetime import datetime
from scipy import interpolate
import Arase
import RBSP.RBSP as vap
#Arase and RBSP both use hours since 1950
#hardcoding some positions
tromsoM=[66.72,102.18]
tromso=[69,19]
def Within(x,x0,x1):
	
	return (x > x0) & (x < x1)

def WithinInc(x,x0,x1):
	
	return (x >= x0) & (x <= x1)

def unix_to_datetime(time):
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
def utc_to_unix(utc_obj):
    date,ut=TT.ContUTtoDate(utc_obj.utc)
    obj_unix=TT.UnixTime(date,ut)
    return obj_unix 
    
import math

def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km
    print(lat1, lon1, lat2, lon2)

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d
def arase_prep():
    arase_read=Arase.Pos.ReadFieldTraces([20170101,20180101])#these might not be optimal dates but im gonna use them for now
    arase_unix=utc_to_unix(arase_read)
    arase_obj=[arase_unix,arase_read.MlatN,arase_read.MlonN]
    return arase_obj
def vap_prep():
    vap_read=vap.Pos.ReadAllFootprintTraces()
    vap_unix=utc_to_unix(vap_read)
    vap_obj=[vap_unix,vap_read.MlatN,vap_read.MlonN]
    return vap_obj
 
def common_time_axis(obj, start_time, end_time,resolution=60):
    new_resolution = np.arange(start_time,end_time,resolution)
    good_index=WithinInc(obj[0],start_time,end_time)
    flat = interpolate.interp1d(obj[0][good_index], obj[1][good_index])
    flon = interpolate.interp1d(obj[0][good_index], obj[2][good_index])
    lat_new=flat(new_resolution)
    lon_new=flon(new_resolution)
    return new_resolution,lat_new,lon_new


def conjuction_finder(object_1, object_2, start_time, end_time):
    origin=common_time_axis(object_1,start_time, end_time)
    seperation=np.zeros(np.shape(origin)[1])
    if len(object_2)==2:#if object_2 is stationary
        #seperation=distance(origin,object_2)
        
        for i in range(0,np.shape(origin)[1]):
            seperation[i]=distance([origin[1][i],origin[2][i]],object_2)
        conjunction=origin[0][np.where(seperation<200)[0]]
        dt_conjunction=unix_to_datetime(conjunction)
        print( min(seperation))
        return dt_conjunction,seperation
    else:
        destination=common_time_axis(object_2,start_time, end_time)
        for i in range(0,np.shape(origin)[1]):
            seperation[i]=distance([origin[1][i],origin[2][i]],[destination[1][i],destination[2][i]])
        conjunction=origin[0][np.where(seperation<200)[0]]
        dt_conjunction=unix_to_datetime(conjunction)
        print( min(seperation))
        return dt_conjunction,seperation
#objects can either be mobile or staionary (use the second entry for sationary things pleas)  and 
#should be made up of n entries of datetime objects with corrosponing lat and lon vaues  

