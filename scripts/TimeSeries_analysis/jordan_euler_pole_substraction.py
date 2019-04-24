# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:42:19 2017

@author: CGeisert

THIS SCRIPT IS DISCONTINUED !!!!
Use jordan_euler_pole.py instead

"""


import numpy as np
import geodetik as geok
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import math
from matplotlib.patches import Ellipse
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset
import pylab
import matplotlib
from numpy import ma
import pylab as pl
import genefun as gf
import geodetik as geok
import velo_field_map_plt as vfmp

source = "hector"
source = "midas"

stations_midas  = ['DES1', 'DES3', 'DRAG', 'GHAJ', 'JOR1', 'JOR2', 'JOR3', 'JOR4','JSLM', 'RAMO', 'SALP', 'UJAP', 'YRCM']
stations_hector = ['DES1', 'DRAG', 'JOR1', 'JOR2', 'JOR3', 'JOR4', 'JSLM', 'RAMO','SALP', 'UJAP']
   
stations_common = set(stations_hector).intersection(set(stations_midas))

only_common     = True
clean_outliers  = True
no_incertitudes = False
with_plot = 1


if source == "hector": 
    p = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/HECTOR_WORK/vel_output/mk3b_halfyear_DataFrame.pik"
    
    DForig = gf.pickle_loader(p)    
    DF = DForig.copy()
    
    if clean_outliers:
        DF = DF[DF["V_North"] < 0.1]
    DF.reset_index()
    
    if only_common:
        DF = DF[DF["Station"].isin(stations_common)]

    all_pos_ref = np.column_stack((DF["Latitude"],DF["Longitude"]))
    
    lat_ref   = np.array(DF["Latitude"])
    long_ref  = np.array(DF["Longitude"])
    
    vn_ref    = np.array(DF["V_North"])
    ve_ref    = np.array(DF["V_East"])
    vu_ref    = np.array(DF["V_Up"])
    
    if not no_incertitudes:
        incvn_ref = np.array(DF["sV_North"])
        incve_ref = np.array(DF["sV_East"])
        incvu_ref = np.array(DF["sV_Up"])
    else:
        incvn_ref = None
        incve_ref = None
        incvu_ref = None


    Stations = np.array(DF["Station"])
else:
    p_midas  = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/HECTOR_WORK/vel_output/midas_velo_DataFrame.pik"
    p_midas  = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/MIDAS_WORK/midas_velo_DataFrame.pik"


    DForig = gf.pickle_loader(p_midas)
    DF = DForig.copy()

    if clean_outliers:
        DF        = DF[DF["sV_North"] < 0.1]

    DF.sort_values("Station",inplace=True)
    
    
    if only_common:
        DF = DF[DF["Station"].isin(stations_common)]

    
    p_latlon = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/RAW_NEU/Jordan_latlon.txt"

    DF_latlon = pd.read_table(p_latlon,comment='*',header=-1,delim_whitespace = True)
    DF_latlon.sort_values(0,inplace=True)
        
    DF_latlon_OK =  DF_latlon[DF_latlon[0].isin(DF["Station"])]
    
    long_ref  = np.array(DF_latlon_OK[1])
    lat_ref   = np.array(DF_latlon_OK[2])
    
    vn_ref    = np.array(DF["V_North"])
    ve_ref    = np.array(DF["V_East"])
    vu_ref    = np.array(DF["V_Up"])
    
    if not no_incertitudes:
        incvn_ref = np.array(DF["sV_North"])
        incve_ref = np.array(DF["sV_East"])
        incvu_ref = np.array(DF["sV_Up"])
    else:
        incvn_ref = None
        incve_ref = None
        incvu_ref = None

    Stations = np.array(DF["Station"])


w,wratedeg,wlat,wlong,wwmat,desmat,nrmatinv=geok.euler_pole_calc(lat_ref,long_ref,
                                                       vn_ref,ve_ref,
                                                       incvn_ref,incve_ref)

print("#### Euler pole, Lat , Lon , Rate for ", source )
print(wratedeg,wlat,wlong)

wwmat_norm = wwmat / np.sum(wwmat)

qual_tup = geok.euler_pole_quality(w,vn_ref,ve_ref,
                                   nrmatinv,desmat,wwmat,
                                   pretty_output=1)

sigma_ww,sigma_ww_latlong,dV_topo3,wrmse,wrmse_norm,rmse,apost_sigma = qual_tup

vne_relat = geok.euler_vels_relative_to_ref(w,lat_ref,long_ref,vn_ref,ve_ref,incvn_ref,incve_ref)


GEBCO=0

hw=5000 #largeur fleche
#posl=[25215.4,38689.2]

# DEZOOM
latm=-25 #latitude minimum
latM=-10 # latitude maximum
lonm=160 # longitude minimum
lonM=174 #longitude maximum
scalev=2000 #echelle longueur vecteur VU
scalev=1500
scalev=15000000

latm=30 #latitude minimum
latM=33 # latitude maximum
lonm=34 # longitude minimum
lonM=38 #longitude maximum

path=""
station_etude = Stations
nstation = len(Stations)


if with_plot:
    vfmp.draw_map(station_etude,latm,latM,lonm,lonM,path,
             all_pos_ref,scalev,hw,vne_relat[:,0],vne_relat[:,1],vu_ref,
             incvn_ref,incve_ref,incvu_ref,GEBCO,0)