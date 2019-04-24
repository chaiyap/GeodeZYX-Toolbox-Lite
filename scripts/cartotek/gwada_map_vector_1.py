# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:23:57 2015

@author: psakicki
"""

from __future__ import division
import pandas as pd
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

import pylab
import numpy
import genefun
import tabulate

from matplotlib.patches import Polygon , Circle ,Ellipse
from mpl_toolkits.basemap import pyproj
from mpl_toolkits.basemap import Basemap , shiftgrid, cm
import matplotlib.transforms as transforms
import geodetik as geok
from netCDF4 import Dataset

fil = "/media/psakicki/666D848C7A623E41/OLD3/GWADA/WORKING_MK2/vel_output/after_epc_ep_sopac_ss_guat.2016.csv"
fil = "/media/psakicki/666D848C7A623E41/OLD3/GWADA/WORKING_MK2/vel_output/after_epc_ep_sopac_ss_guat.csv"
fil = "/home/psakicki/THESE/GWADA/WORKING_MK2/vel_output/after_epc_ep_sopac_ss_guat.2016.csv"
fil = "/home/psakicki/THESE/GWADA/WORKING_MK2/vel_output/after_epc_ep_sopac_ss_guat.csv"


fil2        = "/media/psakicki/666D848C7A623E41/OLD3/GWADA/WORKING_MK2/vel_output/mk2a_halfyear.vel.neu"
fil2_globk  = "/media/psakicki/666D848C7A623E41/OLD3/GWADA/WORKING_MK2/vel_output/mk2a_halfyear.vel"
stat_instit = '/media/psakicki/666D848C7A623E41/OLD3/GWADA/WORKING_MK2/vel_output/stats_institute.list'

df_globk = pd.read_table(open(fil2_globk),sep=r"\s*",header=None,skiprows=[0,1,2])

df2 = pd.read_table(open(fil2),sep=' ',header=None)

print 'aaaa'

df_stat_instit = pd.read_table(open(stat_instit),sep=' ',header=None)

stat_list = list(np.array(df_stat_instit[0]))
instit_list = list(np.array(df_stat_instit[1]))

def get_institute_and_color_of_stat(statin,stat_list,instit_list,color_list=['b','g','r']):
    instit_list_uniq = list(set(list(instit_list)))
    i = stat_list.index(statin)
    instit = instit_list[i]
    color = color_list[instit_list_uniq.index(instit)]
    return color , instit
    
get_institute_and_color_of_stat('ABMF',stat_list,instit_list)


df = pd.read_csv(open(fil),skiprows=2)
lats = np.array(df['  Lat(deg)'])
lons = np.array(df['   Long(deg)'])
Vn   = np.array(df['      dVn(m/yr)'])
Ve   = np.array(df['      dVe(m/yr)'])
#sVn = np.array(df['       Sigma Vn']) 
#sVe = np.array(df['      Sigma Ve'])
#sVne = np.array(df['       Sigma Vne'])
sVn  = np.array(df2[5])
sVe  = np.array(df2[6])
sVne = np.array(df2[7])
Vh = np.array(df_globk[9]) / 1000.
sVh = np.array(df_globk[11]) / 1000.

speed = np.sqrt(np.array(Vn) ** 2 + np.array(Ve) ** 2)

#mp = Basemap(width=140000,height=100000,projection='llc',
#            resolution='l',lat_1=10.,lat_2=20,lat_0=16.2,lon_0=-61.5)


upper =  (15.020486, -60.548101)    
lower =  (14.356285, -61.534124)  
centre = (14.667382, -60.984807)

upper = (17.089298, -58.430127)
lower = (12.480515, -62.517041)
centre = (14.435700, -61.319531)

upper = (16.616457,-60.755428)
lower = (15.740714,-62.161678)
centre = (16,-61)

mp = Basemap(urcrnrlat=upper[0], urcrnrlon=upper[1] ,llcrnrlat=lower[0], 
             llcrnrlon=lower[1], resolution='l'     ,projection='tmerc',
             lat_0=centre[0],lon_0=centre[1])

print 'bbb'

url = '/home/psakicki/Téléchargements/ETOPO1_Bed_c_gdal.grd'
url = '/home/psakicki/Téléchargements/socal_3as_hs.nc'
url = 'http://ferret.pmel.noaa.gov/thredds/dodsC/data/PMEL/etopo5.nc'

etopodata = Dataset(url)

topoin    = etopodata.variables['ROSE'][:]
lons_topo = etopodata.variables['ETOPO05_X'][:]
lats_topo = etopodata.variables['ETOPO05_Y'][:]
# shift data so lons go from -180 to 180 instead of 20 to 380.
topoin,lons_topo = shiftgrid(180.,topoin,lons_topo,start=False)


nx = int((mp.xmax-mp.xmin)/5000.)+1
ny = int((mp.ymax-mp.ymin)/5000.)+1
topodat = mp.transform_scalar(topoin,lons_topo,lats_topo,nx,ny)
im = mp.imshow(topodat,cm.GMT_haxby)


mp.drawmapboundary(fill_color='aqua')
#mp.fillcontinents(color='#cc9955', lake_color='aqua', zorder = 0)
mp.fillcontinents(color='tan',lake_color='aqua', zorder = 0)
mp.drawcoastlines(color = '0.15')

parallels = np.arange(0.,20.,1)
mp.drawparallels(parallels,labels=[False,True,True,False])
meridians = np.arange(-70.,-60.,1)
mp.drawmeridians(meridians,labels=[True,False,False,True])


# lons lat => proj => X Y
X, Y = mp(lons,lats)

# Horizontal
#scale_arrows = 1000000 * 3
scale_arrows = 1000000 * 3
scale_elipse = 1000000 * 3
# Vertical
#scale_arrows = 2500000 * 3
#scale_elipse = 1000000 * 3
nsig   = 1 # sigma for the confidence interval
len_qk = 5 # len in cm of the quiverkey (the arrow in legend)

# ploting the points 
for x,y,st in zip(X,Y,stat_list):
#    col , _ = get_institute_and_color_of_stat(st,stat_list,instit_list)
#    mp.plot(x, y, 'o' , markersize=10,color = col)# ,label =legendlabel[i])
    plt.text(x,y,st)





# ploting the arrows
# Horizontal
Q = mp.quiver(X, Y, Vn * scale_arrows , Ve * scale_arrows , scale =1, scale_units='xy', color='k',width=0.005)
# Vertical
#Q = mp.quiver(X, Y, np.zeros(len(Vh)) , Vh * scale_arrows , scale =1, scale_units='xy', color='k',width=0.005)
# ploting end of the arrows (for control)
#mp.plot(X_end_arrows,Y_end_arrows,'go')

#Ploting the ellipses Horiz
# "end" of the arrows in XY
X_end_arrows = X+Vn*scale_arrows
Y_end_arrows = Y+Ve*scale_arrows
# virtual lat long of the end of the arrows
lons_end_arrows , lats_end_arrows = mp(X_end_arrows,Y_end_arrows,inverse=True)
for x,y,sve,svn,svne in zip(X_end_arrows,Y_end_arrows , sVe , sVn , sVne):
    XX , YY , dXX , dYY = geok.error_ellipse(x,y,sve,svn,svne,scale = 1,nsig=nsig)
    poly = Polygon(np.vstack((x + dXX*scale_elipse, y + dYY*scale_elipse)).T,fill=False)
    plt.gca().add_patch(poly)

#Ploting the ellipses Vert
# "end" of the arrows in XY
#X_end_arrows = X+Vh*0
#Y_end_arrows = Y+Vh*scale_arrows
## virtual lat long of the end of the arrows
#lons_end_arrows , lats_end_arrows = mp(X_end_arrows,Y_end_arrows,inverse=True)
#for x,y,svh in zip(X_end_arrows,Y_end_arrows , sVh):
#    XX , YY , dXX , dYY = geok.error_ellipse(x,y,svh,svh,0,scale = 1,nsig=nsig)
#    poly = Polygon(np.vstack((x + dXX*scale_elipse, y + dYY*scale_elipse)).T,fill=False)
#    plt.gca().add_patch(poly)
    
fig = plt.gcf()

#==== ploting a legend ===
xy_qk = (.1, .2)
xy_ell_lgd = (.1,.1)
xy_ell_txt_lgd = (0.01,.08)
fontsize = 16

ell_lgd_txt = '$\pm'+ str((5))+ 'mm ,$ \n  $'+str(nsig)+'\sigma$'

# quiverkey : optimized legend for a quiver field
qk = plt.quiverkey(Q, xy_qk[0],xy_qk[1], scale_arrows*len_qk / 1000., '$' + str(len_qk) +' mm/yr$', labelpos='S',
               fontproperties={'weight': 'bold','size':fontsize} )
# more difficult for ellpise
# pos of the ellispe itself
ax = plt.gca()
xy_ell_lgd_Data_CS     = genefun.axis_data_coords_sys_transform(ax,*xy_ell_lgd)
xy_ell_txt_lgd_Data_CS = genefun.axis_data_coords_sys_transform(ax,*xy_ell_txt_lgd)
# pos of the associated text
elli = Ellipse(xy_ell_lgd_Data_CS, scale_elipse * .01 ,scale_elipse * .01, angle=0.0,fill=False)#,transform=ax.transAxes)
ax.add_patch(elli)
ell_txt = ax.text(xy_ell_txt_lgd[0],xy_ell_txt_lgd[1],ell_lgd_txt,fontsize=fontsize,transform=ax.transAxes)

fig.set_size_inches(16.53,11.69) 
fig.savefig('/home/psakicki/foo.pdf')


# Tableau vitesse


Ltab = zip( stat_list ,
           Ve * 1000  ,
           sVe * 1000 , 
           Vn * 1000  ,
           sVn * 1000 ,
           Vh * 1000  , 
           sVh * 1000 )
     
Lheader = ['(mm/an)',
           'V. Est',
           '$\sigma$V. Est',
           'V. Nord',
           '$\sigma$V. Nord',
           'V. Vert.' ,
           '$\sigma$V. Vert.']
           
tab = tabulate.tabulate(Ltab,headers=Lheader,
                        tablefmt='latex',floatfmt=".2f")
print tab

    

