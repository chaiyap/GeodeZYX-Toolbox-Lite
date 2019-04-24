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


llcrnrlon = -5
llcrnrlat = 40
urcrnrlon = 20
urcrnrlat = 56

llcrnrlon = -2
llcrnrlat = 45
urcrnrlon = 3.2
urcrnrlat = 49

def carte_france():
    from mpl_toolkits.basemap import Basemap
    import numpy
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 1, figsize=(8,8))
    m = Basemap(llcrnrlon=llcrnrlon,llcrnrlat=llcrnrlat,urcrnrlon=urcrnrlon,
                urcrnrlat=urcrnrlat,
                resolution='f',projection='cass',lon_0=2.34,lat_0=48,
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

refposdic     = collections.OrderedDict([('ANGL', (4404491.463891803, -108110.74519999999, 4596491.369008197)), 
                                         ('AUNI', (4429451.702603825, -73344.22005901638, 4573322.050031694)),
                                         ('BRES', (4370725.68305082, -36125.112323497255, 4629768.617508197)),
                                         ('CHPH', (4236233.126345355, 110998.20365901639, 4751117.440314207)), 
                                         ('ILDX', (4436670.968227869, -91137.98939453551, 4566018.180908743)), 
                                         ('MAN2', (4274275.839450819, 11584.458500000006, 4718386.110908197)), 
                                         ('ROYA', (4466458.820191803, -79862.86325300546, 4537304.7706551915)),
                                         ('SMNE', (4201791.951862842, 177945.60513551912, 4779286.986814207))])
for k,v in refposdic.items():
    print gf.join_improved(' , ', k , *geok.XYZ2GEO(*v))

ydelta = 18000 # ATTENTION A CHANGER EN BAS AUSSI
xdelta = 3000

for k,v in refposdic.items():
    lat , lon  = geok.XYZ2GEO(*v)[0:2]
    print k  , lon , lat

    x,y = m(lon, lat)  # la conversion opère ici
    if k == 'ILDX':
        coul = 'g'
        k = 'UMRB & \n' +k
        ydelta = -3000
    else:
        coul = 'b'
        ydelta = 18000
    m.plot(x, y, coul + 'o', markersize=10)
    ax.text(x + xdelta , y-ydelta, k,size=15)
    
m.drawmapscale(1,45.5,0,45.5,200,barstyle='fancy')

    






