#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 17:11:36 2017

@author: psakicki
"""

from megalib import *
import gins_runner 
import os
import softs_runner
import datetime as dt
import glob

director_generik_path = '/home/psakicki/SOFTWARE_INSTALLED_2/GINS_NEW/gin/data/directeur/operationnel/NEW/DOUBLE_DIFF/DD_NETWORK_OK1'
rnx_path = "/home/psakicki/THESE/DATA/1706_RNX_VANU/RINEX/"

# GENERAL START & END (WIDE PERIOD)
start_general = dt.datetime(2000,1,0o1)
end_general   = dt.datetime(2017,1,25)

# List of stations of interest
stats_list = ['NRMD','KOUC','VANU']
stats_list = ['NRMD','VANU']
stats_list = ['KOUC','VANU']

director_name_prefix  = 'DD_PACIFIC_MK2' + '_'.join(stats_list)

if 0:
    # Find all the rinex files of interest
    rnx_list_all = gins_runner.get_rinex_list(rnx_path             ,
                                          start = start_general,
                                          end   = end_general  ,
                                          specific_stats = stats_list)
    
    # Find the effective date with data
    date_1day_list = list(set([geok.rinexname2dt(rnx) for rnx in rnx_list_all]))
    
    if 1:
        existing_data_path = '/home/cgeisert/GINS/gin/TEMP_DATA/*dd'
        existing_data_lis  = glob.glob(existing_data_path)
        existing_date      = [geok.doy2dt(*reversed([int(ee) for ee in os.path.basename(e).split('_')[0:2]])) for e in existing_data_lis]
        
        date_1day_list = sorted(list(set(date_1day_list) - set(existing_date)))
    
    directors_list = []
    
    for day in date_1day_list: 
        
        rnx_list = gins_runner.get_rinex_list(rnx_list_all,
                                          start = day,
                                          end   = day,
                                          specific_stats = stats_list)
    
        if len(rnx_list) < 2:
            print("WARN : no or only one rinex file for day " + str(day))
            print(rnx_list)
            print("skipping this day ...")
            continue
        try:
            dd_file  = gins_runner.double_diff_multi(rnx_list,
                                                     ignore_glo_gal=False)
        except Exception as e:
            print("ERR : something went wrong during double diff creation")
            print("      day : "    , day)
            print("      RINEXs : " , rnx_list)
            print(e)
            continue
            
        #dd_files_list_in = [dd_file]
        
if 0:
    dd_files_path = '/home/psakicki/SOFTWARE_INSTALLED_2/GINS_NEW/gin/TEMP_DATA/*dd'
    dd_files_list = sorted(glob.glob(dd_files_path))
    directors_list  = gins_runner.gen_dirs_from_double_diff(dd_files_list,
                                                      director_generik_path,
                                                      director_name_prefix,
                                                      out_coords='XYZ')
    
    
# PART 2.5
# directors are already generated
# just find it according to the directors prefix
if 0:
    director_name_prefix  = "DD_PACIFIC"

    wildcard_path = os.path.join(gins_runner.get_gins_path(1),'data', 
                    'directeur',director_name_prefix + '*')
    directors_list = list(reversed(sorted(glob.glob(wildcard_path))))
    
    
    directors_list2 = []
    for e in directors_list:
        ee = os.path.basename(e)
        if 'NRMD' in ee and int(ee.split('_')[-5]) >= 20592:
            continue
        else:
            directors_list2.append(e)
    
    directors_list = list(reversed(sorted(directors_list2)))
    
# PART 3
if 1:
    # Run the directors
    # 3a : on a single slot (most common)
    opts_gins_pc=''
    opts_gins_90='-IPPP'
    opts_gins_90='-nocheck_gnss_products -prepars_seul'
    
    #opts_gins_90=' -IPPP -lM 9000 -lF 100000'
    
    #opts_gins_90=' -IPPP -lM 9000 -lF 100000'
    
    version = 'VALIDE_16_1'
    version = 'VALIDE_15_2_2'
    
    #Version pour le Kalman
    version = 'VALIDE_16_2'


    if 0:
        directors_list = gins_runner.smart_directors_to_run(director_name_prefix + '*')
    
    
    if 0:
        gins_runner.run_directors(directors_list,opts_gins_90=opts_gins_90,
                                  opts_gins_pc=opts_gins_pc,version=version)
    
    if 1:
        fics_list = glob.glob('/home/psakicki/SOFTWARE_INSTALLED_2/GINS_NEW/gin/batch/fic/*PACIFIC*KOUC_VANU_KOUC_VANU_*')
        gins_runner.run_dirs_multislots(fics_list , 7 , 
                                        opts_gins_90=opts_gins_90 ,
                                        opts_gins_pc=opts_gins_pc ,
                                        version=version,
                                        fic_mode = True)
