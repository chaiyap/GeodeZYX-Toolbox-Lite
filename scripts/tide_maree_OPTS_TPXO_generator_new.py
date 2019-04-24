#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:30:30 2017

@author: psakicki
"""

import geo_files_converter_lib as gfc
import datetime as dt
import geodetik as geok
import genefun as gf

## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
## Config files has to be in the working folder 
## with the DATA and the binaries
## Thus, paths in the configs files has to be relatives 
##
## Basic working directory
## /media/psakicki/Geo1_2To/CALIPSO/psakicki/SOFTWARE_INSTALLED_2/OTPS2
## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


outfilepath = '/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1902_ITEC_Prelim/Ships/TIDES/ITEC_Hawai_tide_01_v8'
tide_model_path = "./DATA/Model_atlas"

outfilepath = '/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1902_ITEC_Prelim/Ships/TIDES/ITEC_Hawai_tide_02_v9'
tide_model_path = "./DATA_v9/Model_atlas"

outfilepath = '/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1902_ITEC_Prelim/Ships/TIDES/ITEC_Hawai_tide_03_v9atlas'
tide_model_path = "./DATA_v9ATLAS/Model_atlas"

outfilepath = '/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1902_ITEC_Prelim/Ships/TIDES/ITEC_Hawai_tide_04_localHawa'
tide_model_path = "./DATA_hawa/Model_haw"

lat = 43.44196128
lon = 7.83594147

strt = dt.datetime(2015,6,21,18)
end  = dt.datetime(2015,6,22,7)
end = None

sec_step=1
TS2 = gf.pickle_loader("/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1902_ITEC_Prelim/Ships/TimeSeries/TS_KM_2.pik")

L = TS2.to_list("FLH")
T = geok.posix2dt(L[3])
Lon  = L[1] 
Lat  = L[0]
strt = T


# 1) generation des fichiers
# Will generate
## a) <outfilepath>.inp
## b) <outfilepath>
gfc.write_latlontime_file_4_OTPS_tide(outfilepath , Lat , Lon ,
                                      strt , end , sec_step , True , 
                                      tide_model_path)

# 2) on lance le programme en "pipant"
# NB : tout marche "en local", dans le meme dossier 
# par ex : predict_tide < geodesea_1704.inp

# 3) on récupère les données
out_file_2_read = "/media/psakicki/Geo1_2To/CALIPSO/psakicki/SOFTWARE_INSTALLED_2/OTPS2/ITEC_Hawai_tide_01_v8.out"
out_file_2_read = "/media/psakicki/Geo1_2To/CALIPSO/psakicki/SOFTWARE_INSTALLED_2/OTPS2/ITEC_Hawai_tide_02_v9.out"
out_file_2_read = "/media/psakicki/Geo1_2To/CALIPSO/psakicki/SOFTWARE_INSTALLED_2/OTPS2/ITEC_Hawai_tide_04_localHawa.out"
latlis , lonlis , datlis , hlis = gfc.read_OTPS_tide_file(out_file_2_read)

plt.figure()
plt.plot(datlis , hlis)



