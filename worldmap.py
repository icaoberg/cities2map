import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import matplotlib.cm

from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize

fig, ax = plt.subplots(figsize=(10,20))

m = Basemap(resolution='i', # c, l, i, h, f or None
            projection='merc',
            lat_0=45, lon_0=-100,
            llcrnrlon=-180, llcrnrlat=-70, urcrnrlon=180, urcrnrlat=80)

m.drawmapboundary(fill_color='#46bcec')
m.fillcontinents(color='#f2f2f2',lake_color='#46bcec')
#m.drawcoastlines()

x, y = m(-122.3, 47.6)
plt.title("Computational Biology Department")
plt.plot(x, y, 'ok', markersize=1)
plt.text(x, y, ' Seattle', fontsize=12);

x, y = m(78.6569, 11.1271)
plt.plot(x, y, 'ok', markersize=1)
plt.text(x, y, ' Tamil Nadu', fontsize=12);

x, y = m(-80.19, 25.76)
plt.plot(x, y, 'ok', markersize=1, color='red', marker='v')
plt.text(x, y, ' Miami', fontsize=12);
plt.savefig('worldmap.png', bbox_inches='tight')
