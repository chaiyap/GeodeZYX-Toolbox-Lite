# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 15:01:28 2016

@author: psakicki
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
# setup Lambert Conformal basemap.
# set resolution=None to skip processing of boundary datasets.
#m = Basemap(width=12000000,height=9000000,projection='lcc',
#            resolution=None,lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
#m.shadedrelief()
#plt.show()


#m = Basemap(llcrnrlon=-10,llcrnrlat=40.,urcrnrlon=20,urcrnrlat=50,\
#            rsphere=(6378137.00,6356752.3142),\
#            resolution='f',area_thresh=1.,projection='lcc',\
#            lat_1=50.,lon_0=-107.)
#m.shadedrelief()
#plt.show()
#        

def lambert932WGPS(lambertE, lambertN):
    class constantes:
        GRS80E = 0.081819191042816
        LONG_0 = 3
        XS = 700000
        YS = 12655612.0499
        n = 0.7256077650532670
        C = 11754255.4261
    delX = lambertE - constantes.XS
    delY = lambertN - constantes.YS
    gamma = math.atan(-delX / delY)
    R = math.sqrt(delX * delX + delY * delY)
    latiso = math.log(constantes.C / R) / constantes.n
    sinPhiit0 = math.tanh(latiso + constantes.GRS80E * math.atanh(constantes.GRS80E * math.sin(1)))
    sinPhiit1 = math.tanh(latiso + constantes.GRS80E * math.atanh(constantes.GRS80E * sinPhiit0))
    sinPhiit2 = math.tanh(latiso + constantes.GRS80E * math.atanh(constantes.GRS80E * sinPhiit1))
    sinPhiit3 = math.tanh(latiso + constantes.GRS80E * math.atanh(constantes.GRS80E * sinPhiit2))
    sinPhiit4 = math.tanh(latiso + constantes.GRS80E * math.atanh(constantes.GRS80E * sinPhiit3))
    sinPhiit5 = math.tanh(latiso + constantes.GRS80E * math.atanh(constantes.GRS80E * sinPhiit4))
    sinPhiit6 = math.tanh(latiso + constantes.GRS80E * math.atanh(constantes.GRS80E * sinPhiit5))
    longRad = math.asin(sinPhiit6)
    latRad = gamma / constantes.n + constantes.LONG_0 / 180 * math.pi
    longitude = latRad / math.pi * 180
    latitude = longRad / math.pi * 180
    return longitude, latitude


llcrnrlon = -0.5
llcrnrlat = 47.5
urcrnrlon = 3.5
urcrnrlat = 50

def carte_france():
    from mpl_toolkits.basemap import Basemap
    import numpy
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 1, figsize=(8,8))
    m = Basemap(llcrnrlon=llcrnrlon,llcrnrlat=llcrnrlat,urcrnrlon=urcrnrlon,
                urcrnrlat=urcrnrlat,
                resolution='i',projection='cass',lon_0=2.34,lat_0=48,
               ax=axes)
#    m = Basemap(llcrnrlon=-5,llcrnrlat=40,urcrnrlon=20,urcrnrlat=56,
#            resolution='i',projection='cass',lon_0=2.34,lat_0=48,
#           ax=axes)
    m.drawcoastlines()
    m.drawcountries()
    m.fillcontinents(color='lightgrey', lake_color='#AAAAFF')
    m.drawparallels(numpy.arange(-40,61.,2.) ,labels=[1,1,1,1])
    m.drawmeridians(numpy.arange(-20.,21.,2.),labels=[1,1,1,1])
    m.drawmapboundary(fill_color='#BBBBFF')
    return m, axes
   
   
   
m , ax = carte_france()

shp = '/home/psakicki/THESE/DATA/1608_DEPARTEMENT_GEOFLA/GEOFLA/1_DONNEES_LIVRAISON_2015/GEOFLA_2-1_SHP_LAMB93_FR-ED152/DEPARTEMENT/DEPARTEMENT.shp'
from matplotlib.collections import LineCollection
from matplotlib import cm
import shapefile
r = shapefile.Reader(shp)
shapes = r.shapes()
records = r.records()
for record, shape in zip(records,shapes):
    # les coordonnées sont en Lambert 93
    geo_points = [lambert932WGPS(x,y) for x, y in shape.points]
    lons = np.array([_[0] for _ in geo_points]) + 3
    lats = np.array([_[1] for _ in geo_points])
    data = np.array(m(  lons, lats)).T
    if len(shape.parts) == 1:
        segs = [data,]
    else:
        segs = []
        for i in range(1,len(shape.parts)):
            index = shape.parts[i-1]
            index2 = shape.parts[i]
            segs.append(data[index:index2])
        segs.append(data[index2:])
    lines = LineCollection(segs,antialiaseds=(1,))
    # pour changer les couleurs c'est ici, il faudra utiliser le champ records
    # pour les changer en fonction du nom du départements
    #lines.set_facecolors(cm.jet(np.random.rand(1)))
    lines.set_edgecolors('k')
    lines.set_linewidth(0.1)
    ax.add_collection(lines)
    lon_pref , lat_pref = lambert932WGPS(*record[7:9])
    lon_pref , lat_pref = lambert932WGPS(*record[5:7])

    lon_pref = lon_pref + 3
    x,y = m(lon_pref, lat_pref)
    marge_pref = 1
    m.plot(x, y, 'ko', markersize=2)

    #if llcrnrlon + marge_pref < lon_pref < urcrnrlon - marge_pref and llcrnrlat + marge_pref < lat_pref < urcrnrlat - marge_pref:
        #ax.text(x, y, record[4])    
    
    
from megalib import *

refposdic = collections.OrderedDict([('CHPH', (4236233.08156, 110998.26463599999, 4751117.477176)), ('MAN2', (4274275.799144, 11584.521544, 4718386.149148)), ('MLVL', (4201576.823332, 189860.284372, 4779064.903872)), ('SIRT', (4213550.772464001, 162494.69744, 4769661.8907079995)), ('SMNE', (4201791.9088, 177945.66576799998, 4779287.023676001))])
refposdic = dict(collections.OrderedDict([('CHPH', (4236233.08156, 110998.26463599999, 4751117.477176)), ('MAN2', (4274275.799144, 11584.521544, 4718386.149148)), ('MLVL', (4201576.823332, 189860.284372, 4779064.903872)), ('SIRT', (4213550.772464001, 162494.69744, 4769661.8907079995)), ('SMNE', (4201791.9088, 177945.66576799998, 4779287.023676001))]))
for k,v in refposdic.items():
    print gf.join_improved(' , ', k , *geok.XYZ2GEO(*v))
    

ydelta = 12000
xdelta = 3000

for k,v in refposdic.items():
    lat , lon  = geok.XYZ2GEO(*v)[0:2]
    print k  , lon , lat

    x,y = m(lon, lat)  # la conversion opère ici
    if k == 'MLVL':
        coul = 'g'
        k = 'ENSG & \n' +k
        ydelta = -3000
    else:
        coul = 'b'
        ydelta = 12000
    m.plot(x, y, coul + 'o', markersize=10)
    ax.text(x + xdelta , y-ydelta, k,size=15)
    
m.drawmapscale(2.3,47.8,0,49,100,barstyle='fancy')

    






