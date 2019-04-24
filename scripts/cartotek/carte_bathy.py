# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 13:09:38 2016

@author: psakicki
"""

import netCDF4
from mpl_toolkits.basemap import Basemap


from megalib import *


path = "/home/psakicki/THESE/DATA/1608_GEBCO/2008_1min/2D/GRIDONE_2D.nc"
# Load data
dataset = netCDF4.Dataset(path)

latmin = 12
latmax = 19
lonmin = -63
lonmax = -55

latnew , lonnew , Znew = geok.gebco_bathy_grid_extractor(dataset,latmin,
                                                         latmax,lonmin,lonmax)
    
upper  = (17.5,-56.5)
lower  = (13,-62)
centre = (16,-61.2)

upper  = (17,-60)
lower  = (15,-62)
centre = (16,-61)


m = Basemap(urcrnrlat=upper[0], urcrnrlon=upper[1] ,
             llcrnrlat=lower[0], llcrnrlon=lower[1] ,
             resolution='f',projection='stere',
             lat_0=centre[0],lon_0=centre[1])


xbathy,ybathy = m(*np.meshgrid(lonnew,latnew))
resol_bathy = np.arange(-7000, 1100, 100) #
CS = m.contourf(xbathy, ybathy, Znew, levels = resol_bathy)

#m.fillcontinents(color='grey');
m.drawcoastlines(color = '0.15')

m.drawparallels(np.arange(10,70,1), labels=[1,0,0,0]);
m.drawmeridians(np.arange(-80, 5, 1), labels=[0,0,0,1]);


xpt , ypt = m(-60.50,16.33)
m.scatter(xpt,ypt,s=150,color='r')
