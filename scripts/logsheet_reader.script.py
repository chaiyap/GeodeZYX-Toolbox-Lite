# -*- coding: utf-8 -*-


import geo_files_converter_lib as gfc
import glob
import genefun
import datetime as dt

station_info_out = '/home/pierre/Documents/aaacstationfo'
lfile_out = '/home/pierre/Documents/bbblfile'
logsheets_dir = '/home/pierre/Téléchargements/logsheets_swiss/'
logsheets_wildcard = '*log*'

#period_lis_lis,stat_lis,loc_lis = gfc.multi_logsheet_read(logsheets_dir,logsheets_wildcard)
#    
#gfc.write_station_info_from_datalists(period_lis_lis,stat_lis,loc_lis,station_info_out) 
#gfc.write_lfile_from_datalists(stat_lis,loc_lis,lfile_out)
#gfc.write_station_file_gins_from_datalists(period_lis,stat_lis,loc_lis,station_info_out)


    
    
rinex_path = '/home/pierre/Téléchargements/telechargement_RGP_40415/recherche_1/lroc092z.15o'
rinex_path = '/home/pierre/Téléchargements/telechargement_RGP_40415/recherche_1/gron092z.15o'

gfc.write_station_file_gins_from_rinex(rinex_path,station_info_out)