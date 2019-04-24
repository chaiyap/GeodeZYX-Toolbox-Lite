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

latmin = 39
latmax = 43
lonmin = 25
lonmax = 31

latnew , lonnew , Znew = geok.gebco_bathy_grid_extractor(dataset,latmin,
                                                         latmax,lonmin,lonmax)

upper  = tuple(reversed((31 ,42)))
lower  = tuple(reversed((27 ,40)))
centre = tuple(reversed((30 ,41)))

m = Basemap(urcrnrlat=upper[0], urcrnrlon=upper[1] ,
             llcrnrlat=lower[0], llcrnrlon=lower[1] ,
             resolution='f',projection='stere',
             lat_0=centre[0],lon_0=centre[1])




xbathy,ybathy = m(*np.meshgrid(lonnew,latnew))
resol_bathy = np.arange(-7000, 1100, 100) #
#CS = m.contourf(xbathy, ybathy, Znew, levels = resol_bathy)

m.fillcontinents(color='darkgray',lake_color='white');
m.drawcoastlines(color = '0.15')

m.drawparallels(np.arange(9.5,70,1), labels=[1,0,0,0]);
m.drawmeridians(np.arange(-90, 90, 2), labels=[0,0,0,1]);


xpt , ypt = m(-60.50,16.33)
m.scatter(xpt,ypt,s=150,color='r')
