from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='myapplication')
location=geolocator.geocode("Miami Florida")
location.raw['lat']
location.raw['lon']
