#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 17:09:10 2018

@author: psakicki
"""

import geo_files_converter_lib as gfc

statinfoin  = "/home/psakicki/aaa_FOURBI/stationinfoVB/station.info_gamit_ULR6" #path station.info
coordfilein = "/home/psakicki/aaa_FOURBI/stationinfoVB/lfile_gamit_ULR6" #path coordinates file
outfile     = "/home/psakicki/aaa_FOURBI/stationinfoVB/station_gins_4_VB_v_beta1" #path GINS station file output
coordfile_type = 'lfile' #  'lfile' or 'pbovelfile'



gfc.station_info_2_gins(statinfoin,coordfilein,outfile,coordfile_type,
                        station_info_columns_type = "ulr")
