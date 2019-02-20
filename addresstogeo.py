from geopy.geocoders import Nominatim
import pandas
file = 'staff.txt'
df = pandas.read_csv(file)
print(df)

cities = {}
counts = {}
geolocator = Nominatim(user_agent='myapplication')

for bp in df['City']:
	print(bp)
	if str(bp) in cities:
		print('City was found. Increasing counter.')
		counts[bp]=counts[bp]+1
	else:
		location=geolocator.geocode(bp)
		print('Adding new city. Setting counter to 1.')
		cities[bp]=[location.longitude,location.latitude]
		counts[bp] = 1
