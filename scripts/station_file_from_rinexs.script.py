# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 16:22:56 2015


From a list of rinexs, generate :
1) Lists of Antennas, Receivers , & Periods Objects lists
2) from thoses objects, generate a GINS station file 


@author: psakicki
"""

import gins_runner
import geo_files_converter_lib as gfc
import glob



rinexs_dir_path = '/home/psakicki/gin/TP/GWADA/RINEX/pointO/*o' 
# Don't forget the Wildcard !!! (eg *o)
station_file_gins_output = '/home/psakicki/gin/TP/GWADA/RINEX/pointO/toto.gins'
station_file_gamit_output = '/home/psakicki/gin/TP/GWADA/RINEX/pointO/toto.gamit'


rinex_lis = sorted(glob.glob(rinexs_dir_path))


# PART 1
Antobj_lis = []
Recobj_lis = []
Siteobj_lis = []
Locobj_lis = []

for rnx in rinex_lis:    
    Antobj , Recobj , Siteobj , Locobj = gfc.read_rinex_2_dataobjts(rnx)
    Antobj_lis.append(Antobj)
    Recobj_lis.append(Recobj)
    Siteobj_lis.append(Siteobj)
    Locobj_lis.append(Locobj)
    
Period_lis = []
for ant , rec in zip(Antobj_lis , Recobj_lis):
    Period_lis.append([(ant.Date_Installed,ant.Date_Removed,ant,rec)])



# PART 2
gfc.write_station_file_gins_from_datalists(Period_lis ,Siteobj_lis,
                                       Locobj_lis, station_file_gins_output)
                                       
# PART 3
gfc.write_station_info_from_datalists(Period_lis ,Siteobj_lis,
                                       Locobj_lis, station_file_gamit_output)                                       
                                       
                                       
