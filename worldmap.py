import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.cm
import math
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize

fig, ax = plt.subplots(figsize=(10,20))

m = Basemap(resolution='i', # c, l, i, h, f or None
	projection='merc',
	lat_1=45.,lat_2=55,lat_0=50,lon_0=-107,
        llcrnrlon=-180, llcrnrlat=-70, urcrnrlon=180, urcrnrlat=80)

m.drawmapboundary(fill_color='#46bcec')
m.fillcontinents(color='#f2f2f2',lake_color='#46bcec')
#m.drawcountries()
#m.drawstates()
#m.drawcoastlines()

exec(open("addresstogeo.py").read())

print('Preparing plot')
scale = 5
plt.title("Computational Biology Department Staff")
for bp in cities:
	print(bp)
	print('Adding to (lat,lon):(' + str(cities[bp][0]) + ',' + str(cities[bp][1]) + ') with marker size ' + str(counts[bp])); 
	x, y = m(cities[bp][0], cities[bp][1])
	plt.plot(x, y, markersize=scale*int(math.sqrt(counts[bp])), color='red', marker='o')
	#plt.text(x,y, bp, fontsize=8);

plt.savefig('worldmap.png', bbox_inches='tight')
