#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:30:30 2017

@author: psakicki
"""


import geo_files_converter_lib as gfc
import datetime as dt


outfilepath = '/home/psakicki/THESE/TIDE_OPTS_TPXO/OTPS2/geodesea_1704'
tide_model_path = './DATA/Model_atlas'


lat = 43.44196128
lon = 7.83594147

strt = dt.datetime(2015,6,21,18)
end  = dt.datetime(2015,6,22,7)

sec_step=1

# 1) generation des fichiers
gfc.write_latlontime_file_4_OTPS_tide(outfilepath , lat , lon ,
                                      strt , end , sec_step , True , 
                                      tide_model_path)

# 2) on lance le programme en "pipant"
# par ex : predict_tide < geodesea_1704.inp

# 3) on récupère les données
out_file_2_read = "/home/psakicki/Documents/Modif_geodesea_Zcst/geodesea_1704.out"
latlis , lonlis , datlis , hlis = gfc.read_OTPS_tide_file(out_file_2_read)

plt.plot(datlis , hlis)



