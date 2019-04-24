# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:42:19 2017

@author: CGeisert
"""

import numpy as np
import geodetik as geok
from mpl_toolkits.basemap import Basemap
import math
from matplotlib.patches import Ellipse
from netCDF4 import Dataset
import pandas as pd
from netCDF4 import Dataset
import pylab
import matplotlib
from numpy import ma
import pylab as pl
import genefun as gf
import geodetik as geok
import velo_field_map_plt as vfmp

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

import os 
import itertools

from tabulate import tabulate

############ GENERAL PARAMETERS

source = "midas"
source = "hector"

use_cartopy = False

pole_used = "itrf_arab"
pole_used = "midas_sinai"
pole_used = "hector_sinai"

stations_midas  = ['DES1', 'DES3', 'DRAG', 'GHAJ', 'JOR1', 'JOR2',
                   'JOR3', 'JOR4','JSLM', 'RAMO', 'SALP', 'UJAP', 'YRCM']
stations_hector = ['DES1', 'DRAG', 'JOR1', 'JOR2', 'JOR3', 'JOR4',
                   'JSLM', 'RAMO','SALP', 'UJAP']

stations_sinai_reliable = ["SALP","UJAP","YRCM","RAMO"]

stations_common = set(stations_hector).intersection(set(stations_midas))

only_common     = False
only_sinai      = False 
clean_outliers  = True
no_incertitudes = False # incertitudes for pole estimation
with_plot     = False
plot_vertical = 1 # horzontal instead
plot_hi_res   = 1

print_w_for_easy_copy_paste = 1

############ PLOT PARAMETERS
GEBCO=0

hw=5000 #largeur fleche
#posl=[25215.4,38689.2]

# DEZOOM
latm=-25 #latitude minimum
latM=-10 # latitude maximum
lonm=160 # longitude minimum
lonM=174 #longitude maximum
scale_arrow=2000 #echelle longueur vecteur VU
scale_arrow=1500
scale_arrow=10000000
scale_arrow=15000000

latm=30 #latitude minimum
latM=33 # latitude maximum
lonm=34 # longitude minimum
lonM=38 #longitude maximum

path=""
plt.ioff()

source_lis      = ["hector","midas"]
HV_lis          = [True,False]
scale_arrow_lis = [15000000 , int(15000000*.4)]
pole_used_lis   = ["itrf_arab","midas_sinai","hector_sinai"]
pole_used_lis   = ["sadeh_sinai"]


BIG_ITER = itertools.product(source_lis,
                             HV_lis,
                             scale_arrow_lis,
                             pole_used_lis)


##### LOAD THE POSITIONS FOR ALL CASES ####################
p = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/HECTOR_WORK/vel_output/trend_output_halfyear_DataFrame.pik"
DForig = gf.pickle_loader(p)    
DF = DForig.copy()
all_pos_ref = np.column_stack((DF["Latitude"],DF["Longitude"]))
##########################################################


for iiter in BIG_ITER:
    source        = iiter[0]
    plot_vertical = iiter[1]
    scale_arrow   = iiter[2]
    pole_used     = iiter[3]

    if source == "hector": 
        p = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/HECTOR_WORK/vel_output/trend_output_halfyear_DataFrame.pik"
        
        DForig = gf.pickle_loader(p)    
        DF = DForig.copy()
        
        if clean_outliers:
            DF = DF[DF["V_North"] < 0.05]
            DF = DF[DF["V_East"]  < 0.05]
            DF = DF[DF["V_Up"]    < 0.05]

        DF.reset_index()
        
        if only_common:
            DF = DF[DF["Station"].isin(stations_common)]
            
        if only_sinai:
            DF = DF[DF["Station"].isin(stations_sinai_reliable)]
            
    
        pos_ref_select = np.column_stack((DF["Latitude"],DF["Longitude"]))
        
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
        
    elif source == "midas":
        p_midas  = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/MIDAS_WORK/midas_velo_DataFrame.pik"
    
        DForig = gf.pickle_loader(p_midas)
        DF = DForig.copy()
    
        if clean_outliers:
            DF        = DF[DF["sV_North"] < 0.1]
    
        DF.sort_values("Station",inplace=True)
        
        
        if only_common:
            DF = DF[DF["Station"].isin(stations_common)]
        
        if only_sinai:
            DF = DF[DF["Station"].isin(stations_sinai_reliable)]
    
        
        p_latlon = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/RAW_NEU/Jordan_latlon.txt"
    
        DF_latlon = pd.read_table(p_latlon,comment='*',header=-1,delim_whitespace = True)
        DF_latlon.sort_values(0,inplace=True)
            
        DF_latlon_OK =  DF_latlon[DF_latlon[0].isin(DF["Station"])]
        
        long_ref  = np.array(DF_latlon_OK[1])
        lat_ref   = np.array(DF_latlon_OK[2])
        
        pos_ref_select = np.column_stack((lat_ref,long_ref))
        
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
    
    
    
    print("######## Euler pole, Lat , Lon , Rate for ", source )
    print(wratedeg,wlat,wlong)
    
    if print_w_for_easy_copy_paste:
        print(w[0])
        print(w[1])
        print(w[2])
    
    wwmat_norm = wwmat / np.sum(wwmat)
    
    qual_tup = geok.euler_pole_quality(w,vn_ref,ve_ref,
                                       nrmatinv,desmat,wwmat,
                                       pretty_output=1)
    
    sigma_ww,sigma_ww_latlong,dV_topo3,wrmse,wrmse_norm,rmse,apost_sigma = qual_tup
    
    if print_w_for_easy_copy_paste:
        print("## Sigma on Euler pole, rateSigma, latSigma, longSigma [deg/Myr,deg,deg] ", source )
        print(sigma_ww_latlong[0],sigma_ww_latlong[1],sigma_ww_latlong[2])
        print("##  (un)weigthed RMS on Residual , a-posteriori sigma [m] ", source )
        print(rmse,wrmse,apost_sigma)
        
    ####### ITRF 2014 POLE 
    
    if pole_used == "itrf_arab":
        title_midfix_plate = "fixed Arabia"
        #omega_x   omega_y   omega_z
        #-----------DEG/My----------
        w_itrf = np.array([0.3205 ,  -0.0378  ,  0.4011])
        w_itrf = np.deg2rad(w_itrf) * 10**-6
        w      = w_itrf
    
    elif pole_used == "midas_sinai":
        title_midfix_plate = "fixed Sinai (Midas pole)"
        # BAD EARTH RADIUS
        #0.5591411896731705 49.894639435985326 5.611706728704441
        #w_midas = [6.2564783744183545e-09,
        #           6.147437135886801e-10,
        #           7.464168702566363e-09]
        
        #0.5597547609335898 49.89463943594336 5.611706728836726
        w_midas = [6.2633438948686645e-09,
        6.154183000146926e-10,
        7.472359476996156e-09]
        ## Sigma on Euler pole, rateSigma, latSigma, longSigma [deg/Myr,deg,deg]  midas
        # 0.042580776840647976 4.496639798166289 3.2507007310014924
        ##  (un)weigthed RMS on Residual , a-posteriori sigma [m]  midas
        #0.00013164189379943488 0.13127334460348922 0.1660491060060797 
        
        w = w_midas
           
    elif pole_used == "hector_sinai":
        title_midfix_plate = "fixed Sinai (Hector pole)"
        # BAD EARTH RADIUS
        #0.5411929076552336 50.66858942190626 4.021219471723982
        #w_hector = [5.97192912891307e-09,
        #            4.1982053933248823e-10,
        #            7.306102734786919e-09]
        
        #0.5417867834406909 50.66858942192279 4.021219471670157
        w_hector = [5.978482400493381e-09,
        4.2028122764879993e-10,
        7.314120056225935e-09]
        
        ## Sigma on Euler pole, rateSigma, latSigma, longSigma [deg/Myr,deg,deg]  hector
        #0.06599236883183777 7.224857780293517 5.629912195034152
        ##  (un)weigthed RMS on Residual , a-posteriori sigma [m]  hector
        #0.00021936763171957407 0.25225889513747163 0.3190850674687937
        
        w = w_hector
        
    elif pole_used == "sadeh_sinai":
        title_midfix_plate = "fixed Sinai (Sadeh et al.)"
        w = geok.euler_pole_vector_from_latlongrate(56.642,330.836,np.deg2rad(0.35))
        
    
        
    w = np.array(w)
    
    
    
    sigma_ww,sigma_ww_latlong,dV_topo3,wrmse,wrmse_norm,rmse,apost_sigma = qual_tup
    
    vne_relat = geok.euler_vels_relative_to_ref(w,lat_ref,long_ref,vn_ref,
                                                ve_ref,incvn_ref,incve_ref)
    
    
    ############################# TABLE ####################################
    
    
    Lines_stk = []
    
    for iii ,( stat , vne )in enumerate(zip(Stations,vne_relat)):
        Lines_stk.append(( iii+1 , stat , vne[0]*1000 , vne[1]*1000))
        
    TAB = tabulate(Lines_stk, floatfmt=".3f")
    
    print(TAB)
        
    
    
    #############################' PLOT ###################################''
    
    station_etude = Stations
    nstation = len(Stations)
    
    
    if not use_cartopy:
        
        if with_plot:
            
            if plot_vertical:
                legend_position=(0.5,0.08)
                
            else:
                legend_position=(0.5,0.9)
    
            fig , ax , m = vfmp.draw_map(station_etude,latm,latM,lonm,lonM,path,
                     pos_ref_select,hw,vne_relat[:,0],vne_relat[:,1],vu_ref,
                     incvn_ref,incve_ref,incvu_ref,plot_GEBCO=False,
                     plot_vertical=plot_vertical,
                     plot_ellipses=True,plot_topo=plot_hi_res,coarse_lines=(not plot_hi_res),
                     legend_position=legend_position,
                     scale_arrow=scale_arrow)
            
            #### FINITIONS                    
            if not plot_vertical:
                HV_mark = "H"
                title_prefix = "Horizontal"
            else:
                HV_mark = "V"
                title_prefix = "Vertical"
    
            path_pb = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/plate_bound/sinai_fault_extract.txt"
            PBpb = np.loadtxt(path_pb)
    
            Xplate, Yplate = m(PBpb[:,0],PBpb[:,1])
            m.plot(Xplate,Yplate,
                   color='red',
                   linewidth = 2)
            
            title = title_prefix + " velocities w.r.t. " + title_midfix_plate + " \n using " + source
            
            plt.suptitle(title)
            
            
            export_dir  = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/EXPORT_MAPS"
    
            export_path = os.path.join(export_dir,"_".join(("vel_map",
                                                           source,
                                                           HV_mark,
                                                           pole_used,
                                                           str(scale_arrow))))
            
            for ext in (".png",".svg",".pdf"):
                plt.savefig(export_path + ext)
            
            
    
    else:
        
        ##### CARTOPY MARCHE PAS POUR DES CHAMPS DE VECTEURS IRREGULIERS !!!!!!
        
        latm=30 #latitude minimum
        latM=33 # latitude maximum
        lonm=34 # longitude minimum
        lonM=38 #longitude maximum
        
        coords_area = [lonm, lonM, latm, latM]
        
        crs=ccrs.PlateCarree()
        
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1, projection=crs)
        ax.set_extent(coords_area, crs=crs)
        
        ax.add_feature(cfeature.LAND)
        ax.add_feature(cfeature.OCEAN)
        ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(cfeature.BORDERS, linestyle=':')
        ax.add_feature(cfeature.LAKES, alpha=0.5)
        ax.add_feature(cfeature.RIVERS)
        
        ax.coastlines('10m')
        
        x = all_pos_ref[:,0]
        y = all_pos_ref[:,1]
        
        k = 1000000
        u = vne_relat[:,0] * k
        v = vne_relat[:,1] * k
        
        ax.quiver(x, y, u, v, transform=crs)
        
    
    





