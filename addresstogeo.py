from geopy.geocoders import Nominatim
import pandas
file = 'staff.txt'
df = pandas.read_csv(file)
print(df)

cities = {}
counts = {}
geolocator = Nominatim(user_agent='myapplication')

for bp in df['Birthplace']:
	if str(bp) in cities:
		counts[bp]=counts[bp]+1
	else:
		location=geolocator.geocode(bp)
		if location:
			cities[bp]=[location.longitude,location.latitude]
			counts[bp] = 1
