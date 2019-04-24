#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 18:54:04 2018

@author: psakicki
"""

from megalib import *
import geo_files_converter_lib as gfc


p = "/home/psakicki/aaa_FOURBI/testdir"

period_lis_lis , stat_lis , loc_lis = gfc.multi_logsheet_read(p)

gfc.write_station_info_from_datalists(period_lis_lis,stat_lis,loc_lis,p + "/station.info.from_semisys_logsheets_1812")
gfc.write_lfile_from_datalists(stat_lis,loc_lis,p + "/lfile.from_semisys_logsheets_1812")
