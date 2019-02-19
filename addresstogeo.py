from geopy.geocoders import Nominatim
import pandas
file = 'staff.txt'
df = pandas.read_csv(file)
print(df)

cities = {}
counts = {}
geolocator = Nominatim(user_agent='myapplication')
for bp in df['Birthplace']:
	print(bp)
	
	if str(bp) in cities:
		print('City is already present in dictionary')
		counts[bp]=counts[bp]+1
	else:
		print('Added new city to dictionary')
		location=geolocator.geocode(bp)
	
		if location:
			cities[bp]=[location.raw['lat'],location.raw['lon']]
			counts[bp] = 1
			#print('lat:' + str(location.raw['lat']))
			#print('lon:' + str(location.raw['lon']))

	print(cities)
	print(counts)

