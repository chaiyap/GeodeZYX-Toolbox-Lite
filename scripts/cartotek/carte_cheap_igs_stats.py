# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 16:07:42 2016

@author: psakicki
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

F = open('/home/psakicki/aaa_FOURBI/igs_stat_list')
F2 = open('/home/psakicki/aaa_FOURBI/DataHoldings.txt')

import pandas as pd
df = pd.read_csv(F,sep=';')
df.convert_objects(convert_numeric=True)

df2 = pd.read_table(F2,header = 0 , delim_whitespace=True)

if 0:
    lon = df['lon'][df['dormant'] == 0] 
    lat = df['lat'][df['dormant'] == 0]
else:
    lon =  df2['Long(deg)']
    lat =  df2['Lat(deg)' ]
               
    #lon[lon < 0] = lon[lon < 0] - 180

l0 = 0
map = Basemap(projection='cyl',lon_0 = l0,resolution='h')

if 0:
    BOOL = (lon < l0 - 180)
    lon2 = lon + BOOL * 360

lon2 = lon


map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='tan',lake_color='aqua')
map.drawcoastlines()

x,y = map(lon2,lat)
map.plot(x, y, '*g')

plt.show()
plt.gcf().set_size_inches((10,10))