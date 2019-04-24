#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:21:05 2018

@author: psakicki
"""

from megalib import *
import glob
import os
import shutil
import softs_runner
import gins_runner

path_orig       = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GINS_SOFTWARE/gin/batch/solution/"
path_raw        = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GINS_SOFTWARE/gin/batch/solution/OK"
path_sorted     = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GINS_SOFTWARE/gin/batch/solution/OK/SORTED"
path_duplicated = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GINS_SOFTWARE/gin/batch/solution/OK/DUPLICATED"

#path_listing_raw    = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GINS_SOFTWARE/gin/batch/solution/OK"
#path_listing_sorted = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GINS_SOFTWARE/gin/batch/solution/OK/SORTED"
#path_duplicated     = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GINS_SOFTWARE/gin/batch/solution/OK/DUPLICATED"


wildcard_raw = "*GWA2A_OPE_1a*"
wildcard_raw = "*GWA2A_OPE_2a*"

rinex_archive = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/GWA2A2018/RINEX/"
rinex_archive = "/wrk/sakic_xchg/GWA2A2018/RINEX/"
rinex_archive = "/wrk/sakic_xchg/GWA2A2018/RINEX/RINEX/GOOD"
specific_stats = []
start,end = softs_runner.start_end_date_easy(1980,150,2050,200)


del_duplicated = True

def extract_stat_date(fil):
    fil_base = os.path.basename(fil)
    fil_base_splited = fil_base.split(".yml")[0].split("_")
    jjul = int(fil_base_splited[-2])
    STAT = fil_base_splited[-3]
    dt = geok.jjulCNES2dt(jjul)
    doy , yyyy = geok.dt2doy_year(dt)
    return STAT,jjul,dt,yyyy,doy


############ MOVE SOL FILE INTO DEDICATED FOLDER
if 1:
    print("INFO : move solutions in the OK folder")
    print("WARN : This operation is risky, you have 4sec to cancel")
    komand ="mv -v " + path_orig + "/" + wildcard_raw + " " + path_raw
    print(komand)
    time.sleep(4)
    gf.create_dir(path_raw)
    os.system(komand)
    
########### MOVE SOL FILE INTO DEDICATED FOLDER
Files_raw = sorted(glob.glob(os.path.join(path_raw,wildcard_raw)))
if 1:
    for fil in Files_raw:
        STAT,jjul,dt,yyyy,doy = extract_stat_date(fil)
        print("INFO : move ",  STAT,jjul)
        path_out = os.path.join(path_sorted,STAT)
        gf.create_dir(path_out)
        print("INP :", fil )
        print("OUT :", path_out )
        shutil.move(fil,path_out)


############ GIVE PRETTY NAMES to SOL FILES
### STAT_JJUL_YYYY_DOY_<the_rest_of_the_file>
if 1:  
    Files_sorted = sorted(gf.find_recursive(path_sorted,wildcard_raw))
    for fil in Files_sorted:
        print(fil)
        STAT,jjul,dt,yyyy,doy = extract_stat_date(fil)
        fil_base = os.path.basename(fil)
        #print(STAT,jjul,dt,yyyy,doy)
        regex_pretty = "^\w{4}_\d{5}_\d{4}_\d{3}"
        if not re.search(regex_pretty,fil_base):
            stat_jjul_yyyy_doy = gf.join_improved("_",STAT,jjul,yyyy,doy)
            fil_new = os.path.join(os.path.dirname(fil),stat_jjul_yyyy_doy + '_' + os.path.basename(fil))
            print("OLD :", fil)
            print("NEW :", fil_new)
            os.rename(fil,fil_new)
            

############ CHECK CONSISTENCY

if 1:
    print("############ CHECK CONSISTENCY")
    Files_sorted = sorted(gf.find_recursive(path_sorted,wildcard_raw))
    for fil in Files_sorted:
        bool_consistent = True
        STAT_filename,jjul,dt,yyyy,doy = extract_stat_date(fil)
        Pt_obj = gcls.read_gins_solution(fil,"static")
        if not Pt_obj:
            print("WARN : solution file is empty")
            bool_consistent = False
        elif Pt_obj.name != STAT_filename:
            print("WARN : STAT in solution file != filename")
            print(Pt_obj.name , STAT_filename)
            bool_consistent = False
        else:
            bool_consistent = True
        
        if not bool_consistent:
            print("      removing : ",fil)
            os.remove(fil)

############ CHECK for DOUBLES
if 1:
    Files_sorted = sorted(gf.find_recursive(path_sorted,wildcard_raw))
    
    L_sol = [(os.path.basename(f).split("_")[0],
          int(os.path.basename(f).split("_")[1])) for f in Files_sorted]
    
    L_sol = pd.DataFrame(L_sol).sort_values([0,1])

    Bool = L_sol.duplicated([0,1],False)
    
    L_dup_simple = L_sol[Bool]
    
    L_dup_tmp1 = sorted(list(set([gf.join_improved("",*row) for row in L_dup_simple.values])))    
    L_dup_uniq  = pd.DataFrame([(e[0:4],int(e[4:])) for e in L_dup_tmp1])
    
    L_dup_opera = L_dup_simple
    L_dup_opera = L_dup_uniq

    print(len(L_sol),np.sum(Bool))
    
    print("DUPLICATED :")
    for l in L_dup_opera.values:
        print(l)
    ################## MOVE DUPLICATED
    if 1:
        gf.create_dir(path_duplicated)
        timstp_gins = lambda f: geok.datestr_gins_filename_2_dt("".join(f.split(".")[-3]))
        for i_l , l in enumerate(L_dup_opera.values):
            print("INFO : duplicated file",i_l,*l)
            ### Really dirty : we reload all the files at each iter in Files_sorted since L_dup is not uniquified
            ### Files_sorted = sorted(gf.find_recursive(path_sorted,wildcard_raw))
            dupl_regex    = gf.join_improved("_",*l)
            Dupl_files    = [e for e in Files_sorted if re.match(dupl_regex,os.path.basename(e))]
            print("INFO :",len(Dupl_files),"files founds")
            ### We move the most recent files to the DUPLICATE folder
            Dupl_files_time = [timstp_gins(e) for e in Dupl_files]
            ##Dupl_files_mv   = [e for (e,etime) in zip(Dupl_files,Dupl_files_time) if etime != np.min(Dupl_files_time)]
            for fil in Dupl_files:
                print("INFO : min timestamp",np.min(Dupl_files_time))
                print("INFO : cur timestamp",timstp_gins(fil))
                if timstp_gins(fil) != np.min(Dupl_files_time):  
                    del_duplicated = True
                    if not del_duplicated:
                        print("INFO : MOVE to duplicated : ",fil)
                        shutil.move(fil,path_duplicated)
                    else:
                        print("INFO : RM duplicated : ",fil)
                        os.remove(fil)
                        
                    
                    
############ DETERMINE THE RATIO OF THE PROCESSED FILES
if 1:
    Files_sorted = sorted(gf.find_recursive(path_sorted,wildcard_raw))
    
    L_sol = [(os.path.basename(f).split("_")[0],
          int(os.path.basename(f).split("_")[1])) for f in Files_sorted]
    
    L_sol = pd.DataFrame(L_sol)
    
    Rnx_inp = gins_runner.get_rinex_list(rinex_archive,
                                     specific_stats=[],
                                     invert=False,start=start,end=end)
    
    L_rnx = [(os.path.basename(rnx)[:4].upper(),
          geok.dt2jjulCNES(geok.rinexname2dt(os.path.basename(rnx)))) for rnx in Rnx_inp]
    
    L_rnx = pd.DataFrame(L_rnx)
    
    for stat in L_rnx[0].unique():
        L_rnx_stat = L_rnx[L_rnx[0] == stat]
        L_sol_stat = L_sol[L_sol[0] == stat]
        n_rnx_stat = len(L_rnx_stat)
        n_sol_stat = len(L_sol_stat)
        ratio = n_sol_stat / n_rnx_stat
        print(stat,n_sol_stat,n_rnx_stat,ratio)


