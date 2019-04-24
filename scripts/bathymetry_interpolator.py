# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 22:04:29 2016

@author: psakicki
"""

from netCDF4 import Dataset
import numpy as np
import scipy.interpolate
from mpl_toolkits.basemap import Basemap , shiftgrid, cm
from megalib import *
import matplotlib.pyplot as plt
import vincenty

path = '/home/psakicki/THESE/DATA/1608_GEBCO/2D/GEBCO_2014_2D.nc'
path_map = "/home/psakicki/THESE/DATA/1608_GEBCO/2008_1min/2D/GRIDONE_2D.nc"

export_dir = '/home/psakicki/THESE/RENDU/1608_BATHY_GWADA/'

fh     = Dataset(path, mode='r')
fh_map = Dataset(path, mode='r')


# ========= POUR LA CARTE BATHY ===========
latmin = 12
latmax = 19
lonmin = -64
lonmax = -56

latmin = 10
latmax = 21
lonmin = -70
lonmax = -52


latnew , lonnew , Znew = geok.gebco_bathy_grid_extractor(fh_map,latmin,latmax,lonmin,lonmax)
    
I = scipy.interpolate.RegularGridInterpolator((fh['lat'][:],fh['lon'][:]),
                                              fh['elevation'][:])

lonstk = []
latstk = []

figbathy , axbathy = plt.subplots()
figbathy.set_size_inches((figbathy.get_size_inches()*1.35))

PBgmt      = np.loadtxt('/home/psakicki/THESE/DATA/1610_PLATE_BOUND/Caribbean.txt')
PBgmt[:,0] = PBgmt[:,0] - 360

PBtexas = np.loadtxt('/home/psakicki/THESE/DATA/1610_PLATE_BOUND/plate_boundaries/antilles.txt')

PBpb  = np.loadtxt('/home/psakicki/THESE/DATA/1610_PLATE_BOUND/CA_Bird.txt',delimiter=',')
PBpb2 = np.loadtxt('/home/psakicki/THESE/DATA/1610_PLATE_BOUND/CA-NA_Bird.txt',delimiter=',')

boolpb = (11 <= PBpb[:,1]) * (PBpb[:,1] <= 19)
PBpb   = PBpb[boolpb]
Ipb    = scipy.interpolate.interp1d(PBpb[:,0],PBpb[:,1])

boolgmt = (11 <= PBgmt[:,1]) * (PBgmt[:,1] <= 19) * (-63 <= PBgmt[:,0]) * (PBgmt[:,0] <= -59)
PBgmt   = PBgmt[boolgmt]
Igmt    = scipy.interpolate.interp1d(PBgmt[:,1],PBgmt[:,0])


with_backstop = 0


lat_iles_lis = np.array([ 14.3,  15.1,  15.9,  16.7,  17.5]) - 0.5
lat_trench_lis = lat_iles_lis + 0.6

lat_iles_lis = np.array([ 14.3,  15.1,  15.9,  16.7,  17.5]) - 0.6
lat_iles_lis[-1] = lat_iles_lis[-1] + 0.1
lat_trench_lis = lat_iles_lis + 1.2

lon1_lis = [-62] * len(lat_iles_lis)
lon2_lis = [-57] * len(lat_iles_lis)

colorlis = []
mean_lat = []

for lon1 , lat1 , lon2 , lat2  in zip(lon1_lis,lat_iles_lis,
                                      lon2_lis,lat_trench_lis):
                                          
    lon , lat = geok.line_maker(lon1 , lat1 , lon2 , lat2)
    #lon = np.linspace(-62, -57,10000)
    #lat = np.array([llat - 0.4] * 10000)
    lonstk.append(lon)
    latstk.append(lat)
    
    mean_lat.append(np.mean(lat))
    
    Iprofile     = scipy.interpolate.interp1d(lon , lat)
    Iprofile_lat = scipy.interpolate.interp1d(lat , lon)

    def fct_minim_wrp_pb(lon):
        return Ipb(lon) - Iprofile(lon) 

    def fct_minim_wrp_gmt(lat):
        return Igmt(lat) - Iprofile_lat(lat)
        
    lon_intersec_pb = scipy.optimize.root(fct_minim_wrp_pb,-59).x
    lat_intersec_pb = Iprofile(lon_intersec_pb)
    lat_intersec2   = Ipb(lon_intersec_pb)
    
    if with_backstop:
        try:
            lat_intersec_gmt = scipy.optimize.root(fct_minim_wrp_gmt,np.mean(lat)).x
            lon_intersec_gmt = Iprofile_lat(lat_intersec_gmt)
        except:
            pass
    
    E = I(np.column_stack((lat,lon)))
    
    d_lon = vincenty.vincenty((lat1,0),(lat2,1))
    
    label='mean lat. = ' + str(np.mean(lat)) + ', 1° of lgtd. = ' + str(np.round(d_lon,1)) + 'km'
    outplot = axbathy.plot(lon,E,label=label)
    color = outplot[0].get_color()
    axbathy.scatter(lon_intersec_pb,
                    I(np.column_stack((lat_intersec_pb,
                                       lon_intersec_pb))),
                    marker='o',color=color,s=70)
    if with_backstop:
        try:
            axbathy.scatter(lon_intersec_gmt,
                            I(np.column_stack((lat_intersec_gmt,
                                               lon_intersec_gmt))),
                            marker='d',color=color,s=70)
        except:
            pass
        
    colorlis.append(color)

axbathy.legend()
axbathy.set_xlabel('longitude (°)')
axbathy.set_ylabel('depth (m)')

for ext in ('.png','.pdf','.svg'):
    figbathy.savefig(export_dir +'/bathy_profiles' + ext )

plt.figure()
figmap = plt.gcf() 
figmap.set_size_inches((figmap.get_size_inches()*1.35))

upper  = (18.5,-56.5)
lower  = (13,-63)
centre = (16,-61.2)

upper  = (18.5,-57)
lower  = (12,-63)
centre = (16.2,-60)

# pour le petint point 
#upper  = (17,-58)
#lower  = (14,-62)
#centre = (16,-61.2)

mp = Basemap(urcrnrlat=upper[0], urcrnrlon=upper[1] ,
             llcrnrlat=lower[0], llcrnrlon=lower[1] ,
             resolution='f',projection='tmerc',
             lat_0=centre[0],lon_0=centre[1])

parallels = np.arange(0.,90,1)
mp.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
# draw meridians
meridians = np.arange(180.,360.,1.)
mp.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)
x,y = mp(*np.meshgrid(lonnew,latnew))

resol_bathy = np.arange(-7000, 1100, 100) #

CS = mp.contourf(x, y, Znew, levels = resol_bathy)
mp.drawcoastlines(color = '0.15')
#mp.fillcontinents(color='tan',lake_color='aqua') #, zorder = 0)
#mp.drawmapboundary(fill_color='aqua')

for ext in ('.png','.pdf','.svg'):
    figmap.savefig(export_dir +'/bathy_maps_naked' + ext )

Xplate, Yplate = mp(PBpb[:,0],PBpb[:,1])
mp.plot(Xplate,Yplate,
        color='k',
        linewidth = 3)

#Xplate, Yplate = mp(PBtexas[:,0],PBtexas[:,1])
#mp.plot(Xplate,Yplate,
#        color='darkgrey',
#        linewidth = 3)




if with_backstop:
    Xplate2, Yplate2 = mp(PBgmt[:,0],PBgmt[:,1])
    mp.plot(Xplate2,Yplate2,
            color='grey',
            linewidth = 3)

for lon , lat , color in zip(lonstk,latstk,colorlis):
    X, Y = mp(lon,lat)
    mp.plot(X,Y,color=color,linewidth = 2.5)   
    
#for PB , cooll in zip((PBpb2,),('k',)):
#    Xplate, Yplate = mp(PB[:,0],PB[:,1])
#    mp.plot(Xplate,Yplate,
#            color=cooll  ,
#            linewidth = 4)



#X, Y = mp(-58.6668,16.0998)
#mp.scatter(X,Y,color='r',s=150)   

resol_colorbar = np.arange(-7000, 1100, 1000)
CB = plt.colorbar(CS, shrink=0.8, extend='both',ticks=resol_colorbar)
CB.set_label('depth (m)')

for ext in ('.png','.pdf','.svg'):
    figmap.savefig(export_dir +'/bathy_maps' + ext )






