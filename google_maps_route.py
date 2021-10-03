import googlemaps
import json
import requests
from requests.api import request
from requests.models import Response
from config import API_KEY
from urllib.parse import urlencode
from geographiclib.geodesic import Geodesic
import geopy
import geopy.distance
import pyproj

def get_bearing(lat2, lat1, long2, long1):
    brng = Geodesic.WGS84.Inverse(lat1, long1, lat2, long2)['azi1']
    return brng


gmaps = googlemaps.Client(key = API_KEY)
<<<<<<< HEAD
origin = "4800 Calhoun Rd, Houston, TX"
dest = "16026 Green Manor Drive, Houston, TX"
=======
geodesic = pyproj.Geod(ellps='WGS84')
origin = "106 Zephyr Bend Place, The Woodlands, TX"
dest = "4800 Calhoun Rd, Houston, TX"
>>>>>>> 7aa7e79e79de9094ef59bf95b1fe80bc2a9826fc

# data_type = 'json'
# base_geocode_url = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
# parameters = {
#     'key' : API_KEY,
#     'address' : address
# }
# url_params = urlencode(parameters)
# url = f"{base_geocode_url}?{url_params}" #url is equal to base_geocode_url + ? + urlparams
# print (url)

def extract_lat_long(address, data_type = 'json'):
    base_geocode_url = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    parameters = {
        "address" : address,
        "key" : API_KEY
    }
    url_params = urlencode(parameters)
    url = f"{base_geocode_url}?{url_params}"
    print(url)
    r = requests.get(url)
    if r.status_code not in range (200,299):
        return {}
    return r.json()
    
def extract_directions(origin, dest, data_type = 'json'):
    base_geocode_url = f"https://maps.googleapis.com/maps/api/directions/{data_type}"
    parameters = {
        "origin" : origin,
        "destination" : dest,
        "alternatives" : "true",
        "key" : API_KEY
    }
    url_params = urlencode(parameters)
    url = f"{base_geocode_url}?{url_params}"
    print(url)
    r = requests.get(url)
    if r.status_code not in range (200,299):
        return {}
    return r.json()

def getMatrixDisance(origin, dest, data_type = 'json'):
    base_matrix_url = f"https://maps.googleapis.com/maps/api/distancematrix/{data_type}"
    parameters = {
        "origin": origin,
        "destination": dest,
        "key": API_KEY
    }

    url_params = urlencode(parameters)
    url = f"{base_matrix_url}?{url_params}"
    print(url)
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return {}
    return r.json()
    
# def getMarkersEveryNMeters(path, distance):
#     # res = []
#     # res.append(p0)
#     # path_copy = path
#     if len(path) > 2:
#         tmp = 0
#         prev = path[0]
#         i = 0
#         path_len = len(path)
#         while i < path_len:
#             tmp = gmaps.distance_matrix(prev, path[i], mode='driving')['rows'][0]['elements'][0]['distance']['value']
#             print(tmp)
#             if tmp <= distance:
#                 prev = path[i]
#                 i += 1
#             else:
#                 heading = get_bearing(prev[0], path[i][0], prev[1], path[i][1])
#                 origin = geopy.Point(path[i][0], path[i][1])
#                 destination = geopy.distance.distance(meters=distance).destination(origin, bearing=heading) # May need to invert heading
#                 # print(destination)
#                 path.insert(i, (destination.latitude, destination.longitude))
#                 prev = path[i]
#                 i += 1
#                 path_len += 1
#             # print(i)
#     return path

def get_coordinate_path(routes):
    return [[(step['start_location']['lat'], step['start_location']['lng']) if step != route['legs'][0]['steps'][-1] else (step['end_location']['lat'], step['end_location']['lng']) for step in route['legs'][0]['steps']] for route in routes]

#print (extract_lat_long(origin))
#print (extract_lat_long(dest))
output = extract_directions(origin, dest)
cood_path = get_coordinate_path(output['routes'])
marked_path = getMarkersEveryNMeters(cood_path[0], 50)
print(marked_path, len(marked_path), len(cood_path[0]))
# print(json.dumps(output["routes"], indent=4))

# result = gmaps.distance_matrix((30.1843866,-95.46908049999999), (30.1764351,-95.4664414), mode='driving')
# out = getMatrixDisance(, )
# print(result)

# with open("output.json", "w") as file :
#     file.write(json.dumps(output, indent=4))