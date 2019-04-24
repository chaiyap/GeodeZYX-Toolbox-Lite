#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 14:33:01 2018

@author: psakicki
"""
import gins_runner
import softs_runner
import genefun
import re
import os
import glob
import genefun as gf
import shutil
import subprocess
from io import StringIO
import sys
from bs4 import UnicodeDammit
import geodetik as geok
import datetime as dt
import yaml
import geo_files_converter_lib as gfc
import numpy as np

import time
#print("SLEEP")
#time.sleep(3600*2)

# PART 0
# OPTIONS
stat_file_manu_from_station_info = True
check_if_solution = True
correct_interval  = False
divide_the_jobs   = True
job_slots_total   = 4 # maximum 4 slots
job_slot_id       = 0 # starts at 0

path_station_info = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1811_Repro_Gwada_18/metadata/station.info.ovsg"
path_lfile        = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1811_Repro_Gwada_18/metadata/lfile_gwada"

path_lfile        = '/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/PROCESSING_CONFIGnMETA/meta_gamit_like/lfile_gwada_IPGP_new_1812'
path_station_info = '/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/PROCESSING_CONFIGnMETA/meta_gamit_like/station.info.ovsg_ovsm.custom_1812'

# PART 1
# How many RINEXs will you process ?
# You can give compressed RINEXs if you want
# 1a : It's a RINEX alone => give the path of the RINEX
if 0:
    rnx_inp = "/home/psakicki/SOFTWARE/GINS/gin/TEMP_DATA/yarr0010.16o"
    rnx_inp = "/home/psakicki/aaa_FOURBI/RINEX/yarr0010.16o"
    rnx_inp = "/home/psakicki/aaa_FOURBI/RINEX/houe1340.00d.Z"
    rnx_inp = "/home/psakicki/aaa_FOURBI/RINEX/houe0160.07d.Z"
    rnx_inp = "/home/psakicki/aaa_FOURBI/RINEX/houe1450.00d.Z"
    rnx_inp = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GINS_SOFTWARE/gin/TEMP_DATA/untitledfolder/aber2070.16d.Z"
    rnx_inp = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/GWA2A2018/RINEX/IPGP/houe/2006/houe3580.06d.Z"
    rnx_inp = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/GWA2A2018/RINEX/IPGP/ade0/2004/ade00050.04d.Z"
    rnx_inp = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/GWA2A2018/RINEX/IPGP/fna0/2005/fna00150.05d.Z"

# 1b : It's a list of RINEXs   => make a list
if 0:
    rnx_inp = ['/home/psakicki/THESE/DATA/1702_NAPPE_EP/RINEX/MICR3350.16o',
               '/home/psakicki/THESE/DATA/1702_NAPPE_EP/RINEX/NAPP3350.16o']

# 1c : RINEXs are in a archive => find them, select specific stations and specific period if you want
if 1:
    rinex_archive = '/home/psakicki/GINS/gin/TP/TP_RELAX'
    #### A reprendre a GOSI
    rinex_archive = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/GWA2A2018/RINEX/RENAG_ORPHEON"
    rinex_archive = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/GWA2A2018/RINEX/RGP"
    rinex_archive = "/dsk/eviegas/GWA2A2018/RINEX/RINEX/GOOD/IPGP"

    specific_stats = ['ABD0']
    specific_stats = ['GOSI']
    specific_stats = ['LORI','MAGA','MARI','TRIL']
    specific_stats = ['ADE0','AJB0','AMC0','BIM0']
    specific_stats = ['CBE0'] # lance sans slots sur l'user S
    specific_stats = ['DHS0','DSD0','FFE0','FNA0']
    specific_stats = ["AJB0"] # rerun because of unknow bug  (4 slots)
    specific_stats = ["FNG0"] # lonely for check reasons (4 slots)
    specific_stats = ["FNG0","AJB0"] # lonely for check reasons (4 slots)
    specific_stats = ['FSDC','HOUE','ILAM','LAM0']
    specific_stats = ['MAD0','MGL0','MLM0','MPOM']
    specific_stats = ['PAR1','PDB0','PSA1','SAM0']
    specific_stats = ['SBL0','SOUF','TAR1','TDB0']
    specific_stats = []

    
    # ABD0
    # ADE0
    # AJB0
    # AMC0
    # BIM0
    # CBE0
    # DHS0
    # DSD0
    # FFE0
    # FNA0
    # FNG0
    # FSDC
    # HOUE
    # ILAM
    # LAM0
    # MAD0
    # MGL0
    # MLM0
    # MPOM
    # PAR1
    # PDB0
    # PSA1
    # SAM0
    # SBL0
    # SOUF
    # TAR1
    # TDB0

    invert_selection = False

    # For the period, convert easily a start doy / end doy to a Python datetime object
    start,end = softs_runner.start_end_date_easy(1980,150,2050,200)
    start = dt.datetime(2014,5,30)

    rnx_inp = gins_runner.get_rinex_list(rinex_archive,
                                         specific_stats=specific_stats,
                                         invert=invert_selection,start=start,end=end)

    if divide_the_jobs:
        rnx_inp_slots = genefun.chunkIt(rnx_inp,job_slots_total)
        rnx_inp = rnx_inp_slots[job_slot_id]

if not gf.is_iterable(rnx_inp):
    rnx_inp = [rnx_inp]

# PART 2
# Definition of the working folders
temp_data_folder   = '/home/psakicki/gin/TP/GWADA/RINEX'
temp_data_folder   = None # Best Option
temp_data_folder   = gins_runner.get_temp_data_gins_path()

# PART 3
# Generate the director(s) associated to the input RINEX(s)
#%%
if 1:

    directors_main_dir            = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/PROCESSING_CONFIGnMETA/GINS_data/directeurs/NEW_TEMPLATES_1811/"
    director_generik_path         = directors_main_dir + "DIR_PPP_PS1.yml"
    director_generik_include_path = directors_main_dir + "DIR_REF_PPP_PS1.yml"

    director_name_prefix_proto  = "ADELADEL_GWA2A_OPE_1a_"
    
    if divide_the_jobs:
        director_name_prefix = director_name_prefix_proto + "_slot" + str(job_slot_id) + "_"
    else:
        director_name_prefix = director_name_prefix_proto

    ##### THE GENERIK DIRECTOR HAS TO BE COPIED TO GET THE EXPERIENCE PREFIX
#    director_generik_renamed_path = gins_runner.dirs_copy_generik_2_working(director_name_prefix,
#                                                                            director_generik_path,
#                                                                            temp_data_folder)

director_generik_working_path = os.path.join(temp_data_folder,director_name_prefix+".yml")


if check_if_solution:
    solution_path = os.path.join(gins_runner.get_gins_path(),'gin',
                                 'batch',
                                 'solution')
    #Sol_files_list = list(glob.glob(solution_path + "/*"))
    Sol_files_list = gf.find_recursive(solution_path,'*')
    Sol_files_list = np.array(Sol_files_list)

for irnx , rnx in enumerate(list(sorted(rnx_inp))):
    print("INFO :",irnx+1,"/",len(rnx_inp),"RINEX processed")
    print("INFO :","processing",rnx)

    rnx_work = shutil.copy(rnx,temp_data_folder)
    dt_rinex = geok.rinexname2dt(os.path.basename(rnx_work))
    jjul_rinex = geok.dt2jjulCNES(dt_rinex)
    STAT = os.path.basename(rnx_work)[0:4].upper()

    ############################################################################
    ###### CHECK IF SOLUTION
    if check_if_solution:
        regex = gf.join_improved(".*",director_name_prefix_proto,STAT + "_" + str(jjul_rinex) + "_0")
        print("INFO : looking for regex :",regex)
        print("INFO : ",len(Sol_files_list),"files in",solution_path)
        Sol_files_good_list = [bool(re.search(regex,s)) for s in Sol_files_list]
        #check_regex = lambda x: bool(re.search(regex,x))
        #Sol_files_good_list = list(map(check_regex,Sol_files_list))

        if np.any(Sol_files_good_list):
            print("INFO : solution(s) has been found for this day, skipping ... ")
            print(rnx_work)
            print(np.array(Sol_files_list)[Sol_files_good_list])
            continue

    ############################################################################
    ###### CORRECT RINEX
    ###### Only for Orpheon Antilles stations
    if correct_interval:
        if softs_runner.check_if_compressed_rinex(rnx_work):
            rnx_work_uncomp = softs_runner.crz2rnx(rnx_work)
        else:
            rnx_work_uncomp = rnx_work

        L1 = "     1.000                                                  INTERVAL"
        L2 = "    30.000                                                  INTERVAL"
        ## rnx_work_uncomp = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GINS_SOFTWARE/gin/TEMP_DATA/aber2070b.16o"
        gf.replace(rnx_work_uncomp,L1,L2)
        rnx_work = rnx_work_uncomp
        #os.rename(rnx_work,rnx_work + "_orig")
        #rnx_work = softs_runner.rnx2crz(rnx_work_uncomp,path_of_rnx2crz="/dsk/ggsp_pf/PLAYGROUND/psakicki/scripts_PS/HATANAKA_uptodate/bin/RNX2CRZ")

    ############################################################################
    ###### CHANGE THE ORBITS/CLOCKS path + antex
    director_dic = yaml.load(open(director_generik_path))

    if dt.datetime(1998,1,4) <= dt_rinex <= dt.datetime(2013,12,29):
        gr_gr2 = 'GR2'
        #    elif dt_rinex < dt.datetime(1998,1,4):
        #        gr_gr2 = 'GR1' # obsolete parce que GR1 intégralement inclu dans GR2
    elif dt_rinex < dt.datetime(1998,1,4):
        gr_gr2 = 'IG2'
        print('INFO : no GRG/GR2 orbit available for day',dt_rinex)
        print('       (day before 1998/1/4) => using IG2 orb. instead')
    else:
        gr_gr2 = 'GRG'

    if dt_rinex < dt.datetime(2017,1,29):
        antex = "igs08.atx"
    else:
        antex = "igs14.atx"

    horpath = os.path.join('horloges',gr_gr2,'defaut')
    orbpath = os.path.join('orbites',gr_gr2,'defaut')
    antexpath = os.path.join('ANTEX',antex)

    director_dic['model']['environment']['gnss_clock']         = horpath
    director_dic['observation']['interobject_data'][0]['file'] = orbpath
    director_dic['model']['environment']['gnss_antenna']         = antexpath

    # WRITING THE NEW DIRECTOR
    print('INFO : writing : ', director_generik_working_path)
    with open(director_generik_working_path, 'w+') as outfile:
        outfile.write( yaml.dump(director_dic,default_flow_style=False) )

    # correcting a bug : GINS YAML interpreter can't manage false or true ...
    gf.replace(director_generik_working_path,'false','no')
    gf.replace(director_generik_working_path,'true','yes')

    ###########################################################################
    ######## GENERATE STATION FILE

    #### Station file will be added as a command argument below
    #### (and not in the directeur file)
    if stat_file_manu_from_station_info:
        DIC_stat_date = gfc.read_station_info_solo_date(path_station_info,STAT,dt_rinex,'sopac')

        if DIC_stat_date is None:
            print("ERR : no meta data found for ")
            print(rnx)
            continue

        x,y,z,_,_,_,_ = gfc.read_lfile_solo(path_lfile,STAT)

        station_file_name_out = gf.join_improved("_",STAT,geok.dt2jjulCNES(dt_rinex),".stat")
        station_file_path_out = os.path.join(temp_data_folder ,
                                             station_file_name_out)
        xyz = (x,y,z)
        gfc.stat_file_GINS_new_fmt(station_file_path_out,STAT,
                                   xyz=xyz,
                                   rec=DIC_stat_date["Rec"],
                                   ant=DIC_stat_date["Ant"],
                                   radom=DIC_stat_date["Dome"])

    ############################################################################
    ###### Generate the command
    arg_gene     = "timeout 400 exe_ppp -IPPP -static"
    arg_rin      = "-rin "     + rnx_work
    arg_dir      = "-dir_ref " + director_generik_working_path
    arg_dir_incl = "-incl "    + director_generik_include_path
    if not divide_the_jobs:
        arg_opt_gins = ''
    else:
        slots_list = ["","U","L","R"] #don't forget the space for the per defaut user (" ")
        arg_opt_gins = '-opt_gins="-F' + slots_list[job_slot_id] + '"'

    if stat_file_manu_from_station_info:
        arg_stat = "-sta " + station_file_path_out
    else:
        arg_stat = ""

    kommand      = " ".join((arg_gene,arg_rin,arg_dir,arg_dir_incl,
                             arg_stat,arg_opt_gins))

    print(kommand)

    gins_path = gins_runner.get_gins_path()
    log_path = gf.create_dir(os.path.join(gins_path,'python_logs'))
    log_path = os.path.join(gins_path,'python_logs',director_generik_working_path + ".log")

    #process = subprocess.Popen([kommand], shell=True ,
    bool_job_is_good = False
    while_loop_counter=0
    sol_dir = os.path.join(gins_path,"gin","batch","solution")
    sol_file_wildcard = gf.join_improved("*",director_name_prefix,STAT,jjul_rinex)
    sol_path = os.path.join(sol_dir,sol_file_wildcard)
    while (not bool_job_is_good) and (while_loop_counter < 2) and (len(glob.glob(sol_path)) == 0):
        while_loop_counter += 1
        process = subprocess.Popen([kommand], shell=True ,
                                   stdout=subprocess.PIPE ,
                                   stderr=subprocess.PIPE,
                                   executable='/bin/bash')

        for c in iter(lambda: process.stdout.read(1), b''):
            # https://stackoverflow.com/questions/436220/determine-the-encoding-of-text-in-python4
            # find encoding
            # print(c)
            #print(dammit.original_encoding)
            c_deco = c.decode("iso-8859-1", errors='replace')
            #print(c_deco)
            sys.stdout.write(c_deco)
        
        process.wait()
        returncode = process.returncode
        print("INFO : return code (None = OK, something else = error) :",returncode)
        
        if np.isclose(returncode,124):
            bool_job_is_good = False
        else:
            bool_job_is_good = True
            
    print("INFO : Sleep for 2sec")
    time.sleep(2)

    
        
