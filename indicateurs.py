from geopy.geocoders import Nominatim
from geopy.distance import geodesic
geolocator = Nominatim(user_agent='my-application')

def distance(x1,y1,x2,y2,unit):
    if unit == 'm':
        return geodesic(x1,y1,x2,y2).m
    elif unit =='km':
        return geodesic(x1,y1,x2,y2).m
    elif unit =='miles':
        return geodesic(x1,y1,x2,y2).m

def list_of_distances(lx1,ly1,lx2,ly2,unit):
    return list(distance(lx1[i],ly1[i],lx2[i],ly2[i],unit) for i in range(lx1))

def speed(dist,time):
    return dist/time

def ms_to_kmh(speed):
    return speed*3.6

def kmh_to_ms(speed):
    return speed/3.6