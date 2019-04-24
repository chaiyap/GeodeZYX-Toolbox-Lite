#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 14:56:41 2018

@author: psakicki
"""

from megalib import *
import matplotlib.pyplot as plt

plt.ioff()
soft = "GINS"
soft = "EPOS"

### ALGEMEINE PATHS
logsheets_path = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1811_Repro_Gwada_18/01_Syncro_Server_TPX1/METADATA/meta_log_sheets"
jump_file_path = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1811_Repro_Gwada_18/01_Syncro_Server_TPX1/METADATA/meta_JUMPS_files/gwada18_manu_mk1.jump"

### SOFTS PATHS
if soft == "GINS":
    main_path = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1811_Repro_Gwada_18/01_Syncro_Server_TPX1/GNSS_RESULTS/GINS/01_GFZorbs"
elif soft == "EPOS":
    main_path = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1811_Repro_Gwada_18/01_Syncro_Server_TPX1/GNSS_RESULTS/EPOS/OK_mk2_good"

#### Define export paths
plots_path = main_path + "/02_plots_raw"
#export_path= "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1811_Repro_Gwada_18/GNSS_RESULTS/EPOS/OK_mk1_dry_run/02_Plots_raws"
#export_latlonfile_path= "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/RAW_NEU/Jordan_latlon.txt"
export_path_hector         = main_path + "/04a_HECTOR_WORK/RAW_NEU"
export_path_midas          = main_path + "/03b_export_coords_MIDAS"
export_path_TS_clean       = main_path + "/TS_clean_dic"
#### Read a simple coordinate file
#p = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/RAW_DATA/PPP_coordinates/2012_307_23_sta_coordinates"
#gcls.read_epos_sta_coords_mono(p)

### Read several coordinate files
#sinex_antenna_path = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/sinex_antenna/sta_antenna.JORDAN"
#DFantenna = gfc.read_sinex_bench_antenna(sinex_antenna_path)
#gf.create_dir(export_path)

if   soft == "GINS":
    pp = main_path + "/01_SOLUTIONS/OK/SORTED"
    L = gf.find_recursive(pp,"*PPP")
    TSdict = gcls.read_gins_solution_multi(L) 
elif soft == "EPOS":
    pp = main_path + "/01_PPP_coordinates/*coord*"
    L = glob.glob(pp)
    TSdict = gcls.read_epos_sta_coords_multi(L,True)  


################################################################
### DISCONT FCTS PROTOTYPE
################################################################
    
#Discont = gfc.read_station_info_time_solo(station_info_path,timeseries.stat)[0]
#Discont = gfc.read_sinex_discontinuity_solo(sinex_discont_path,timeseries.stat)[0][1:]
#Discont = gcls.sinex_bench_antenna_DF_2_disconts(DFantenna,ts.stat)
#MetaData_dico=gfc.multi_logsheet_read(logsheets_path,return_dico=True)
    
    
###### FROM LOGSHEETS
Ant_dico = dict()
Rec_dico = dict()

LogSheets_list = glob.glob(logsheets_path + "/*")

for ls in LogSheets_list:
    Site     = gfc.read_blocks_logsheet(ls,1)
    Rec_list = gfc.read_blocks_logsheet(ls,3)
    Ant_list = gfc.read_blocks_logsheet(ls,4)
    
    Rec_dico[Site[0].Four_Character_ID] = Rec_list
    Ant_dico[Site[0].Four_Character_ID] = Ant_list 
    
###### FROM JUMP FILE
Jump_dict = gcls.read_jump_file(jump_file_path)
    
#############################

#%%


coords_tab_stk = []

TSdict_clean = dict()

for stat , ts in TSdict.items():
    nbday = (ts.enddate() - ts.startdate()).days + 1.
    print(ts.stat , ts.startdate()  , ts.enddate() , nbday , ts.nbpts , ts.nbpts * 100. / nbday )

for stat , ts in TSdict.items():
    
    if 1 and stat != "DHS0":
        print("SKIP",stat)
        continue
    
    if ts.nbpts == 1:
        print(ts.stat,"excluded bc ts.nbpts == 1")
        continue
    
    ts.ENUcalc_from_mean_posi()
    
    if 0:
        if soft == "GINS":
            std_val_lim = 0.15
        elif soft == "EPOS":
            std_val_lim = 0.50
            
        if ts.stat == "GHAJ":
            std_val_lim = 1000000
            tsGHAJ = ts
        
        ts2 = gcls.std_dev_cleaner(ts,std_val_lim,"ENU",verbose=False)
        if ts2.nbpts <=1:
            print(ts.stat,"excluded bc ts2.nbpts == 0")
            continue
    else:
        ts2 = ts
    
    if 1:
        ts3a = gcls.mad_cleaner(ts2,coortype="ENU",
                               detrend_first=True,verbose=True)
        ts3  = gcls.mad_cleaner(ts3a,coortype="ENU",
                               detrend_first=True,verbose=True)
    else:
        ts3 = ts2

    if 1: ### TimeWin
        import pytz
        start = dt.datetime(1980,2,1)
        end   = dt.datetime(2099,12,1)
        
        if stat in Jump_dict.keys():
            if Jump_dict[stat]["S"]:
                start = Jump_dict[stat]["S"][0].replace(tzinfo=None)
                print("INFO : A start from the Jump File is defined :" , start)
            if Jump_dict[stat]["E"]:
                end   = Jump_dict[stat]["E"][0].replace(tzinfo=None) 
                print("INFO : A start from the Jump File is defined :" , end)
        
        ts3 = gcls.time_win(ts3,[(start,end)])

    if 1: ### Add discont
        Discont_Rec  = []
        Discont_Ant  = []
        Discont_Jump = []
        
        ### Discont = gcls.sinex_bench_antenna_DF_2_disconts(DFantenna,ts.stat)
        #Discont_Rec = [Rec.Date_Installed for Rec in Rec_dico[ts3.stat]]
        Discont_Ant = [Ant.Date_Installed for Ant in Ant_dico[ts3.stat]]
        
        if stat in Jump_dict.keys():
            if Jump_dict[stat]["D"]:
                Discont_Jump = Discont_Jump + Jump_dict[stat]["D"]
        
        Discont = sorted(Discont_Rec + Discont_Ant + Discont_Jump)
        
        ts3.set_discont(Discont)

    if 1: ### PLOT
        Fig = plt.figure()
        ts3.plot("ENU",fig=Fig)
        gcls.export_ts_plot(ts3,plots_path)
        
    if 0: # export HECTOR/MIDAS ENU files
        gcls.export_ts_as_neu(ts3, export_path_hector , "")
        gcls.export_ts_as_midas_tenu(ts3, export_path_midas , "")
        
    if 0: # stack lat lon in a QnD file
        coords_tab_stk.append([ts3.stat,ts3.mean_posi().L,ts3.mean_posi().F])

    if 1: #save the clean TS in a new dico
        TSdict_clean[stat] = ts3

if 1:
    gf.pickle_saver(TSdict_clean,export_path_TS_clean,full_path=True)


if 0:
    ### Export stacked lat lon
    F = open(export_latlonfile_path,"w+")
    for l in coords_tab_stk:
        F.write(gf.join_improved(" ",*l) + "\n")
    F.close()
    
  


########
## AREA for Point and Click

#%%
 
if 1:
    plt.ion()
    plt.close("all")
    fig_id = 42
    stat = "TDB0"
    TS_PnC = TSdict_clean[stat]
    plt.figure(fig_id)
    TS_PnC.plot(fig=fig_id)
    
    
    PnC = gcls.point_n_click_plot()
    multi , cid = PnC(fig=fig_id)  
    PnC.selectedX

