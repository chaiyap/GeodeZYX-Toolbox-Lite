#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:07:23 2017

@author: psakicki
"""

import geo_files_converter_lib as gfc
import glob
import geodetik as geok
import softs_runner
import os
import numpy as np
import genefun


# Read a RINEX and return 4 "DataObjects" : 
# Antenna Object
# Reciever Object
# Site Object
# Location Object

rinex_path = '/home/psakicki/Téléchargements/transfer_397074_files_6ca51ea5/IGNTEST_1sec/smne/2017/MERGED/smne0010.17o'
Antobj , Recobj , Siteobj , Locobj = gfc.read_rinex_2_dataobjts(rinex_path)


# Read RINEXs in a directory in order to find material changes

rnx_dir = '/home/psakicki/THESE/DATA/1702_RINEX_GWA2A_REBOOT/ORPHEON'
rnx_dir = '/home/psakicki/THESE/DATA/1702_RINEX_GWA2A_REBOOT/OVSGM'
rnx_dir = '/home/psakicki/THESE/DATA/1702_RINEX_GWA2A_REBOOT/'

stat_lis = list(set([e[0:4] for e in geok.rinex_lister(rnx_dir)]))

rnx_objts_lis = []

stat_dico = dict()

for stat in stat_lis:
    rnx_path_lis = softs_runner.multi_finder_rinex(rnx_dir           ,
                                                   rinex_types=('d',),
                                                   specific_stats = (stat,))
    
    if len(rnx_path_lis) == 0:
        continue        
    
    Ants_Type = []
    Recs_Type = []
    Dates = []
       
    for rnx in rnx_path_lis:
        print(os.path.basename(rnx))
        if softs_runner.check_if_compressed_rinex(rnx):    
            rnx_uncompressed = softs_runner.crz2rnx(rnx,path_of_crz2rnx='CRZ2RNX')
            rm_rnx = False
        else:
            rnx_uncompressed = rnx
            rm_rnx = False
        Objts = gfc.read_rinex_2_dataobjts(rnx_uncompressed)
        if Objts[0] == None:
            continue
        #rnx_objts_lis.append(Objts)
        Ants , Recs , Sites , Locs = Objts
        Ants_Type.append(Ants.Antenna_Type)
        Recs_Type.append(Recs.Receiver_Type)
        Dates.append(Ants.Date_Installed)
        
        if rm_rnx:
            os.remove(rnx_uncompressed)
        
    Ants_Type = np.array(Ants_Type)
    Recs_Type = np.array(Recs_Type)
    Dates     = np.array(Dates)
    
    Dates,Ants_Type,Recs_Type = genefun.sort_multinom_list(Dates    ,
                                                           Ants_Type,
                                                           Recs_Type)
    
    stat_dico[stat] = (Dates , Ants_Type , Recs_Type)


stat_change_dico = dict()

for stat , (Dates , Ants_Type , Recs_Type) in stat_dico.items():
    Dates_Devices_List = list(zip(Dates , Ants_Type , Recs_Type))
    
    Dates_Device_Change_Lis = []
    
    Dates_Device_Change_Lis.append(Dates_Devices_List[0])
    
    for iDD in range(len(Dates_Devices_List) -1):
        if  Dates_Devices_List[iDD+1][1:3] == Dates_Devices_List[iDD][1:3]:
            continue
        else:
            Dates_Device_Change_Lis.append(Dates_Devices_List[iDD+1])
    
    stat_change_dico[stat] = Dates_Device_Change_Lis
    
    print("**********",stat,"**********")
    for  dat , rec , ant in Dates_Device_Change_Lis:
        print(dat , rec , ant)


genefun.pickle_saver(stat_dico,
                     '/home/psakicki/THESE/DATA/1702_RINEX_GWA2A_REBOOT/STAT_CHANGE_CRAWLER',
                     'stat_dico')

        
genefun.pickle_saver(stat_change_dico,
                     '/home/psakicki/THESE/DATA/1702_RINEX_GWA2A_REBOOT/STAT_CHANGE_CRAWLER',
                     'stat_change_dico')


# Read Logsheets
if 0:
    path_mono = '/home/psakicki/THESE/DATA/1702_RINEX_GWA2A_REBOOT/fichiers_stations/LOGSHEET_RENAG/liste_log/ARGR_2015-09-17.log'   
    A = gfc.mono_logsheet_read(path_mono, return_lists = False)
    
    path = '/home/psakicki/THESE/DATA/1702_RINEX_GWA2A_REBOOT/fichiers_stations/LOGSHEET_RENAG/liste_log/'
    stations_dico = gfc.multi_logsheet_read(path,'*log',return_dico=True)













