### click ###
import click
@click.command()
@click.option("-f", "--file", help="name of input file (.txt)", default = "staff.txt")
@click.option("-o", "--output", help="name of output file (.eps)", default = "worldmap.eps")
@click.option("-t", "--title", help="title of the map", default = "Computational Biology Department")
@click.option("-c", "--color", help="color of the markers", default = "red")
@click.option("-m", "--marker", help="shape of the markers", default = "o")

def fug(file,output,title,color,marker):
	
	print("Importing libraries...")
	
	### world map ###
	import matplotlib
	matplotlib.use("TkAgg")
	import matplotlib.pyplot as plt
	import matplotlib.cm
	import math
	from mpl_toolkits.basemap import Basemap
	from matplotlib.patches import Polygon
	from matplotlib.collections import PatchCollection
	from matplotlib.colors import Normalize
	
	### address to geo ###
	from geopy.geocoders import Nominatim
	import pandas
	
	### map setup ###
	print("Setting up map...")
	fig, ax = plt.subplots(figsize=(10,20))
	
	m = Basemap(resolution='i', # c, l, i, h, f or None
		projection='merc',
		lat_1=45.,lat_2=55,lat_0=50,lon_0=-107,llcrnrlon=-180, llcrnrlat=-70, urcrnrlon=180, urcrnrlat=80)
	
	m.drawmapboundary(fill_color='#45bcec')
	m.fillcontinents(color='#f2f2f2',lake_color='#46bcec')
	
	### addresses setup ###
	print("Locating cities...")
	df = pandas.read_csv(file)
	#print(df)
	
	cities = {}
	counts = {}
	geolocator = Nominatim(user_agent='myapplication')
	
	for bp in df['City']:
		if str(bp) in cities:
			#print('Found',bp,'again')
			counts[bp]=counts[bp]+1
		else:
			location=geolocator.geocode(bp)
			if location == None:
				print("Couldn't locate",bp)
			else:
				#print('New city',bp)
				cities[bp]=[location.longitude,location.latitude]
				counts[bp] = 1
	
	### drawing map ###
	print('Preparing plot...')
	scale = 1
	plt.title(title)
	for bp in cities:
		#print(bp)
		print('Adding to (lat,lon):(' + str(cities[bp][0]) + ',' + str(cities[bp][1]) + ') with marker size ' + str(scale*counts[bp])); 
		x, y = m(cities[bp][0], cities[bp][1])
		plt.plot(x, y, markersize=scale*counts[bp], color=color, marker=marker)
		#plt.text(x,y, bp, fontsize=8);
	
	plt.savefig(output, bbox_inches='tight', format='eps', dpi=1200)
	
	print("Done! Created",output,"in the current directory.")
	
if __name__ == '__main__':
    fug()