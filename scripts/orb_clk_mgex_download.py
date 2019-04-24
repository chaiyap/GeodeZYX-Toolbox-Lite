#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 14:48:56 2018

@author: psakicki
"""

from megalib import *
import softs_runner
import itertools
import geo_files_converter_lib


### screen csh -c "pyps /dsk/ggsp_pf/PLAYGROUND/psakicki/scripts_PS/zyx_TOOLBOXs/geodezyx_toolbox_py3/scripts/orb_clk_mgex_download.py"

#### Destination of the products files
orbit_mgex_dir = '/home/mansur/Documents/TEST-DL-MGEX/'
orbit_mgex_dir = "/dsk/ggsp_pf/PLAYGROUND/psakicki/CF-ORB-MGEX/cf_orb/acc_combi/combi/final/orbit_mgex_new"
orbit_mgex_dir = "/dsk/eviegas/public/orbit_mgex_new"
orbit_mgex_dir = "/dsk/ggsp_pf/PLAYGROUND/psakicki/CF-ORB-MGEX/cf_orb/acc_combi/combi/final/orbit_mgex_new_1660-1799"
orbit_mgex_dir = "/dsk/mansur/MGEX/ARCHIVE_PROD_MGEX/products/"

#### Products files type (see doc of fct multi_downloader_orbs_clks())
files_type_list  = ["snx"]
files_type_list  = ["sp3","clk","erp","bia","snx"]

#### 1 STEP : Selection of the ACs
calc_center_list = ["cod"]
calc_center_list = ["wum","sha"]
calc_center_list = ["igs","igr","gbm"]
calc_center_list = ["grm","tum","com","gbm"] + ["COD","JAX"] + ["igs","igr"]
calc_center_list = ["wum","sha"]
calc_center_list = ["SHA"]
calc_center_list = ["wum"]

### reboot for bad wuhan
calc_center_list = ["wum"]

####                standard                    longname        igs for validation  chinese (not on CDDIS)
calc_center_list = ["grm","tum","com","gbm"] + ["COD","JAX"] + ["igs","igr"] + ["SHA","wum"]

### reboot for
calc_center_list = ["COD","JAX"] + ["igs","igr"] + ["SHA","wum"]

### reboot for QZSS old naming
calc_center_list = ["qzs"]


#### 2 STEP : Selects where ACs products are coming from
#### in a dictonnary : select the good server as the dict key, and the goods ACs
#### in an associated list
#### (see doc of fct multi_downloader_orbs_clks())
#### IMPORTANT : ALL ACs in calc_center_list must be in the following archive_dict

archive_dict = dict()
archive_dict["cddis_mgex_longname"] = ["COD","JAX"]
archive_dict["cddis"]               = ["igs","igr"]

archive_dict["ign_mgex"]            = ["wum"]
archive_dict["ign_mgex_longname"]   = ["SHA"]

archive_dict["cddis_mgex"]          = ["wum"]
archive_dict["cddis_mgex"]          = ["gbm","grm","tum","wum","com","sha","qzs"]


bool_uncompress      = False # uncompression of the files
bool_long2short_name = True # convert long name to short name

#### Time range serlection
#s,e = dt.datetime(2018,2,25) , dt.datetime(2018,4,15) #

week_begin = 1660
week_end   = 1799

### reboot for bad wuhan
week_begin = 1773
week_end   = 1825

week_begin = 1800
week_end   = 2000

week_begin = 1660
week_end   = 2000

start = geok.gpstime2dt(week_begin,0)
end   = geok.gpstime2dt(week_end,6)

parallel_download = 4

iter_list = itertools.product(files_type_list , calc_center_list)

for fil , clc in iter_list:

    archive_center = genefun.dic_key_for_vals_list_finder(archive_dict , clc)

    if not archive_center:
        print("ERR : AC " , clc , "is not in the archive dictionary !!!" )
        print("      Define an archive for this AC in the archive dictionary")
        raise Exception

    orblis = softs_runner.multi_downloader_orbs_clks(orbit_mgex_dir , start , end ,
                                                     sp3clk=fil,parallel_download=parallel_download,
                                                     archtype='wkwwww',
                                                     calc_center = clc,
                                                     archive_center = archive_center,
                                                     force_weekly_file = '')

    if bool_uncompress:
        orblis = [geo_files_converter_lib.unzip_gz_Z(e) for e in orblis]

    if bool_long2short_name and (clc in archive_dict["cddis_mgex_longname"]):
	        orblis = [softs_runner.orbclk_long2short_name(e,center_id_last_letter="m",rm_longname_file=False) for e in orblis]
