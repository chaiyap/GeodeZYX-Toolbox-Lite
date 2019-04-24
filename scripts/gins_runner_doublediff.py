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


director_generik_path = '/home/psakicki/GINS/gin/data/directeur/DD_NETWORK_OK1'
director_name_prefix = 'DD_PACIFIC'
rnx_path = "/home/psakicki/THESE/RINEX_PACIFIC_GINS"

# GENERAL START & END (WIDE PERIOD)
start_general = dt.datetime(2000,1,0o1)
end_general   = dt.datetime(2016,12,31)

#List of stations of interest
stats_list = ['NRMD','KOUC','PTVL']


# Find all the rinex files of interest
rnx_list = gins_runner.get_rinex_list(rnx_path             ,
                                      start = start_general,
                                      end   = end_general  ,
                                      specific_stats = stats_list)


# Find the effective date with data
date_1day_list = list(set([geok.rinexname2dt(rnx) for rnx in rnx_list]))

for day in date_1day_list:
    
    
    rnx_list = gins_runner.get_rinex_list(rnx_path,
                                      start = day,
                                      end   = day,
                                      specific_stats = stats_list)

    if len(rnx_list) < 2:
        print("WARN : no or only one rinex file for day " + str(day))
        print(rnx_list)
        print("skipping this day ...")
        continue
    try:
        dd_file  = gins_runner.double_diff_multi(rnx_list)
    except Exception as e:
        print("ERR : something went wrong during double diff creation")
        print("      day : "    , day)
        print("      RINEXs : " , rnx_list)
        print(e)
        continue
        
    
    dd_files_list_in = [dd_file]
    
    dirs_list = gins_runner.gen_dirs_from_double_diff(dd_file,
                                                      director_generik_path,
                                                      director_name_prefix,
                                                      out_coords='XYZ')
